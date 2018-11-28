#include <bits/stdc++.h>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

/*** START OF TEMPLATE CODE ***/

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) begin(x), end(x)
#define FE(i, x) for (auto i = begin(x); i != end(x); ++i)
#define SZ(x) ((int) (x).size())

template<class T>
vector<T> splitstr(const string &s)
{
    istringstream in(s);
    vector<T> out;
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
    return out;
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

static void redirect(int argc, const char **argv)
{
    if (argc > 1)
    {
        int fd = open(argv[1], O_RDONLY);
        if (fd == -1) { perror(argv[1]); exit(1); }
        if (-1 == dup2(fd, 0)) { perror(argv[1]); exit(1); }
        if (-1 == close(fd)) { perror(argv[1]); exit(1); }
    }

    if (argc > 2)
    {
        int fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
        if (fd == -1) { perror(argv[2]); exit(1); }
        if (-1 == dup2(fd, 1)) { perror(argv[2]); exit(1); }
        if (-1 == close(fd)) { perror(argv[2]); exit(1); }
    }

    ios::sync_with_stdio(false);
    cin.exceptions(ios::failbit | ios::badbit);
}

template<typename EdgeType>
struct SimpleNode
{
    typedef EdgeType Edge;
    std::vector<Edge> edges;
};

struct SimpleEdge
{
    int trg;

    SimpleEdge() {}
    explicit SimpleEdge(int trg) : trg(trg) {}
};

template<typename T = int>
struct WeightedEdge
{
    typedef T weight_type;

    int trg;
    T weight;
    WeightedEdge() {}
    WeightedEdge(int trg, T weight) : trg(trg), weight(weight) {}
};

template<typename EdgeType, typename NodeType = SimpleNode<EdgeType> >
class GraphBase
{
public:
    typedef EdgeType Edge;
    typedef NodeType Node;

    std::vector<Node> nodes;

    int size() const { return nodes.size(); }

    int size(int id) const
    {
        assert(0 <= id && id < size());
        return nodes[id].edges.size();
    }

    NodeType &operator[](int id)
    {
        assert(0 <= id && id < size());
        return nodes[id];
    }

    const NodeType &operator[](int id) const
    {
        assert(0 <= id && id < size());
        return nodes[id];
    }

    explicit GraphBase(std::size_t size = 0) : nodes(size) {}
};

// Unweighted graph with arbitrary node type
template<typename NodeType = SimpleNode<SimpleEdge> >
class UGGraph : public GraphBase<SimpleEdge, NodeType>
{
public:
    // Add unidirectional edge
    void add1(int a, int b)
    {
        assert(0 <= a && a < this->size());
        assert(0 <= b && b < this->size());
        this->nodes[a].edges.push_back(SimpleEdge(b));
    }

    // Add bidirected edge
    void add2(int a, int b)
    {
        add1(a, b);
        add1(b, a);
    }

    explicit UGGraph(std::size_t size = 0) : GraphBase<SimpleEdge, NodeType>(size) {}
};

// Unweighted graph
typedef UGGraph<> UGraph;

// Weighted graph
template<typename T = int, typename NodeType = SimpleNode<WeightedEdge<T> > >
class WGraph : public GraphBase<WeightedEdge<T>, NodeType>
{
public:
    typedef typename GraphBase<WeightedEdge<T>, NodeType>::Edge::weight_type weight_type;
    typedef typename GraphBase<WeightedEdge<T>, NodeType>::Edge Edge;
    typedef typename GraphBase<WeightedEdge<T>, NodeType>::Node Node;

    // Add unidirectional edge
    void add1(int a, int b, T weight)
    {
        assert(0 <= a && a < this->size());
        assert(0 <= b && b < this->size());
        this->nodes[a].edges.push_back(Edge(b, weight));
    }

    // Add bidirectional edge
    void add2(int a, int b, T weight)
    {
        add1(a, b, weight);
        add1(b, a, weight);
    }

    explicit WGraph(std::size_t size = 0) : GraphBase<WeightedEdge<T>, NodeType>(size) {}
};

template<typename T = int>
struct MFEdge
{
    typedef T flow_type;

    int trg;
    T flow;
    T cap;
    int dual;

    MFEdge() {}
    MFEdge(int trg, T cap, int dual) : trg(trg), flow(0), cap(cap), dual(dual) {}
};

template<typename T = int>
class MFGraph : public GraphBase<MFEdge<T> >
{
private:
    struct pqitem
    {
        int trg;
        T prio;

        pqitem() {}
        pqitem(int trg, T prio) : trg(trg), prio(prio) {}

        bool operator<(const pqitem &b) const
        {
            return prio < b.prio;
        }
    };
public:
    typedef typename MFEdge<T>::flow_type flow_type;
    typedef typename GraphBase<MFEdge<T> >::Edge Edge;
    typedef typename GraphBase<MFEdge<T> >::Node Node;

    void add(int a, int b, T cap, T rcap)
    {
        assert(a >= 0 && a < this->size() && b >= 0 && b < this->size());
        if (a == b)
            return; // no use in network flow, and complicates this function
        int da = this->size(a);
        int db = this->size(b);
        this->nodes[a].edges.push_back(Edge(b, cap, db));
        this->nodes[b].edges.push_back(Edge(a, rcap, da));
    }

    T augment(int source, int sink)
    {
        const int N = this->size();
        const T big = std::numeric_limits<T>::max();

        std::vector<T> prio(N);
        std::vector<int> preve(N);
        std::priority_queue<pqitem> q;

        prio[source] = big;
        q.push(pqitem(source, big));
        while (!q.empty())
        {
            int cur = q.top().trg;
            T p = q.top().prio;
            q.pop();
            if (p != prio[cur])
                continue;
            if (cur == sink)
                break;
            for (int i = 0; i < this->size(cur); i++)
            {
                const Edge &e = this->nodes[cur].edges[i];
                T p2 = std::min(p, e.cap - e.flow);
                if (p2 > prio[e.trg])
                {
                    prio[e.trg] = p2;
                    preve[e.trg] = e.dual;
                    q.push(pqitem(e.trg, p2));
                }
            }
        }

        T up = prio[sink];
        if (up > 0)
        {
            int cur = sink;
            while (cur != source)
            {
                Edge &ed = this->nodes[cur].edges[preve[cur]];
                Edge &e = this->nodes[ed.trg].edges[ed.dual];
                e.flow += up;
                ed.flow -= up;
                cur = ed.trg;
            }
        }
        return up;
    }

    T make_flow(int source, int sink)
    {
        for (int i = 0; i < this->size(); i++)
            for (int j = 0; j < this->size(i); j++)
                this->nodes[i].edges[j].flow = 0;

        T flow = 0;
        T up;
        while ((up = augment(source, sink)) != 0)
            flow += up;
        return flow;
    }

    // Returns all vertices on the source side of the cut. Call this
    // immediately after make_flow
    std::set<int> cut_vertices(int source) const
    {
        std::stack<int> st;
        st.push(source);
        std::set<int> reach;
        reach.insert(source);
        while (!st.empty())
        {
            int cur = st.top();
            st.pop();
            for (int i = 0; i < this->size(cur); i++)
            {
                const Edge &e = this->nodes[cur].edges[i];
                if (e.flow != e.cap && !reach.count(e.trg))
                {
                    st.push(e.trg);
                    reach.insert(e.trg);
                }
            }
        }
        return reach;
    }

    explicit MFGraph(std::size_t size = 0) : GraphBase<MFEdge<T> >(size) {}
};

/*** END OF TEMPLATE CODE ***/

static int getword(map<string, int> &ids, int &pool, const string &word)
{
    if (ids.count(word))
        return ids[word];
    else
    {
        ids[word] = pool++;
        return ids[word];
    }
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int N;
        cin >> N >> ws;
        vector<vi> sents;
        map<string, int> ids;
        int pool = 0;
        for (int i = 0; i < N; i++)
        {
            string line;
            getline(cin, line);
            vs words = splitstr<string>(line);
            vi sent;
            for (string word : words)
            {
                sent.push_back(getword(ids, pool, word));
            }
            sents.push_back(sent);
        }

        int src = 0;
        int sink = 1;
        int word_off = 2;
        int sent_off = 2 + 2 * pool;
        int V = sent_off + 2 * N;
        MFGraph<ll> g(V);
        ll big = 1000000;
        ll huge = big * big;
        for (int i = 0; i < pool; i++)
        {
            int base = word_off + 2 * i;
            g.add(src, base, 1, 0);
            g.add(base, base + 1, huge, 0);
            g.add(base + 1, sink, 1, 0);
        }
        for (int i = 0; i < N; i++)
        {
            int base = sent_off + 2 * i;
            g.add(src, base, (i == 0) ? huge : big, 0);
            g.add(base, base + 1, huge, 0);
            g.add(base + 1, sink, (i == 1) ? huge : big, 0);
            for (int j : sents[i])
            {
                int trg = word_off + 2 * j;
                g.add(base, trg + 1, huge, 0);
                g.add(trg, base + 1, huge, 0);
            }
        }

        ll flow = g.make_flow(src, sink);
        ll ans = flow % big - pool;
        cout << "Case #" << cas + 1 << ": " << ans << "\n";
    }
    return 0;
}
