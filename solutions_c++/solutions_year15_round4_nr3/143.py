#include <bits/stdc++.h>
using namespace std;
#define ulong uint64_t
#define mt make_tuple
#define eb emplace_back
#define all(u) begin(u),end(u)
#define _overload3(_1,_2,_3,name,...) name
#define _rep(i,n) _repi(i,0,n)
#define _repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define rep(...) _overload3(__VA_ARGS__,_repi,_rep,)(__VA_ARGS__)
template<class C>void uniq(C&c){c.erase(unique(all(c)),end(c));}
template<class T>bool chmin(T&a,const T&b){return a>b&&(a=b,1);}
template<class T>bool chmax(T&a,const T&b){return a<b&&(a=b,1);}

struct edge {
    int to, cap, rev;
    edge(int to, int cap, int rev) : to(to), cap(cap), rev(rev) {}
};
typedef vector<vector<edge>> graph;
const int inf = 1e9;
void add_uedge(graph& G, int from, int to, int cap) {
    G[from].emplace_back(to, cap, G[to].size());
    G[to].emplace_back(from, cap, G[from].size() - 1);
}
class maxflow {
    const int n;
    graph& G;
    vector<int> level, iter;
    void bfs(int s) {
        level.assign(n, -1);
        queue<int> q;
        level[s] = 0, q.push(s);
        while (not q.empty()) {
            const int v = q.front();
            q.pop();
            for (const edge& e : G[v]) {
                if (e.cap > 0 and level[e.to] < 0) {
                    level[e.to] = level[v] + 1;
                    q.push(e.to);
                }
            }
        }
    }
    int dfs(int v, int t, int f) {
        if (v == t) return f;
        for (int& i = iter[v]; i < int(G[v].size()); ++i) {
            edge& e = G[v][i];
            if (e.cap > 0 and level[v] < level[e.to]) {
                const int d = dfs(e.to, t, min(f, e.cap));
                if (d > 0) {
                    e.cap -= d, G[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }
public:
    maxflow(graph& G) : n(G.size()), G(G) {}
    int pour(int s, int t) {
        int ret = 0;
        while (bfs(s), level[t] >= 0) {
            iter.assign(n, 0);
            int d;
            while ((d = dfs(s, t, inf)) > 0) {
                ret += d;
            }
        }
        return ret;
    }
};

graph G;

void input()
{
    int n;
    cin >> n >> ws;
    map<string, int> mem;
    vector<pair<int, int>> E;
    rep(i, n) {
        string sentence;
        getline(cin, sentence);
        istringstream in(sentence);
        string word;
        while (in >> word) {
            const int t = mem.size();
            const int id = mem.find(word) == mem.end() ? mem[word] = t : mem[word];
            E.eb(i, n + id);
        }
    }
    G.assign(n + mem.size(), vector<edge>());
    for (auto e : E) {
        int u, v;
        tie(u, v) = e;
        add_uedge(G, u, v, 1);
    }
}

void solve()
{
    cout << maxflow(G).pour(0, 1) << endl;
}

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        input();
        cout << "Case #" << i << ": ";
        solve();
    }
}
