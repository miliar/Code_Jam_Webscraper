#include <bits/stdc++.h>

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define in(x) int (x); input((x));
#define x first
#define y second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)

typedef int itn;

//#define next next12345
//#define prev prev12345
#define left lefdsf232
#define right rig43783
#define x1 x12345
#define y1 y12345

using namespace std;

template<typename T>
T gcd(T x, T y) {
    while (y > 0) {
        x %= y;
        swap(x, y);
    }
    return x;
}

template<class T>
T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}


template<class _T>
inline _T sqr(const _T &x) {
    return x * x;
}

template<class _T>
inline string tostr(const _T &a) {
    ostringstream os("");
    os << a;
    return os.str();
}

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
const ld PI = 3.1415926535897932384626433832795L;

template<typename T>
inline void input(T &a) {
    static int ed;
    a = 0;
    while (!isdigit(ed = getchar()) && ed != '-') { }
    char neg = 0;
    if (ed == '-') {
        neg = 1;
        ed = getchar();
    }
    while (isdigit(ed)) {
        a = 10 * a + ed - '0';
        ed = getchar();
    }
    if (neg) a = -a;
}

template<typename T = int>
inline T nxt() {
    T res;
    input(res);
    return res;
}

void myassert(bool v) {
    assert(v);
    //cout << "FAIL\n";
    //exit(0);
}

mt19937 generator;

bool check(int v) {
    if (v < 2) return false;
    for (int i = 2; i * i <= v; ++i) {
        if (v % i == 0) {
            return false;
        }
    }
    return true;
}

long long pw(long long a, long long n, long long m) {
    ll res = 1;
    while (n) {
        if (n & 1ll) {
            res = res * a % m;
        }
        a = a * a % m;
        n >>= 1;
    }
    return res;
}

long long inv(long long a, long long p) {
    long long res = 1;
    while (a > 1) {
        res = res * (p - p / a) % p;
        a = p % a;
    }
    return res;
}

const int N = 2222;

struct minCostFlow {
    struct edge {
        int from, to;
        long long cap, flow, cost;
    };

    vector <edge> edges;
    vector<int> g[N];
    int vsize;

    int p[N];
    char used[N];
    long long dist[N];
    long long pi[N];
    int q[N];

    void addEdge(int from, int to, long long cap, long long cost) {
        g[from].pb(edges.size());
        edges.push_back(edge{from, to, cap, 0, cost});
        g[to].pb(edges.size());
        edges.pb(edge{to, from, 0, 0, -cost});
    }


    bool fb(int s, int t) {
        memset(p, 0xff, vsize * sizeof(int));
        memset(dist, 0x3f, vsize * sizeof(long long));
        memset(used, 0, vsize * sizeof(char));
        dist[s] = 0;
        int q1 = 0, q2 = 0;
        q[q2++] = s;
        used[s] = 1;
        while (q1 != q2) {
            int v = q[q1++];
            used[v] = 0;
            if (q1 == vsize) {
                q1 = 0;
            }
            for (int ed : g[v]) {
                edge &e = edges[ed];
                int to = e.to;
                long long len = e.cost;
                if (e.cap > e.flow && dist[to] > dist[v] + len + pi[to] - pi[v]) {
                    dist[to] = dist[v] + len + pi[to] - pi[v];
                    p[to] = ed;
                    if (!used[to]) {
                        used[to] = 1;
                        q[q2++] = to;
                        if (q2 == vsize) {
                            q2 = 0;
                        }
                    }
                }
            }
        }
        return p[t] != -1;
    }

    int cost;
    int flow;

    long long pushFlow(int s, int t, long long need) {
        long long addFlow = need;
        for (int cur = t, e = p[cur]; cur != s; cur = edges[e].from, e = p[cur]) {
            addFlow = min(addFlow, edges[e].cap - edges[e].flow);
        }
        cost += (dist[t] - pi[t]) * addFlow;
        flow += addFlow;
        for (int cur = t, e = p[cur]; cur != s; cur = edges[e].from, e = p[cur]) {
            edges[e].flow += addFlow;
            edges[e ^ 1].flow -= addFlow;
        }
        for (int i = 0; i < vsize; ++i) {
            pi[i] -= dist[i];
        }
        return addFlow;
    }

    void calcMinCostFlow(int s, int t, long long needFlow) {
        while (needFlow && fb(s, t)) {
            needFlow -= pushFlow(s, t, needFlow);
        }
    }

    minCostFlow(int vertices) {
        flow = 0;
        vsize = vertices;
        cost = 0;
        memset(pi, 0, vsize * sizeof(long long));
    }
};


struct solution {
    int test;
    string a, b;
    int n;

    map <string, int> l, r;
    int L, R;

    vector <pair <string, string>> q;

    void read() {
        cin >> n;
        forn(i, n) {
            string u, v;
            cin >> u >> v;
            q.pb(mp(u, v));
        }
    }

    int getL(string s) {
        if (l.count(s)) {
            return l[s];
        } else {
            return l[s] = L++;
        }
    }

    int getR(string s) {
        if (r.count(s)) {
            return r[s];
        } else {
            return r[s] = R++;
        }
    }

    int ans;

    void solve() {
        L = 0, R = 0;
        for(auto x : q) {
            getL(x.x);
            getR(x.y);
        }

        int s = L + R;
        int t = L + R + 1;

        int s0 = t + 1;
        int t0 = s0 + 1;


        minCostFlow mcf(t0 + 1);

        for (int i = 0; i < L; ++i) {
            mcf.addEdge(s, i, 1e9, 0);
            mcf.addEdge(s0, i, 1, 0);
            mcf.addEdge(s, t0, 1, 0);
        }

        for (int i = 0; i < R; ++i) {
            mcf.addEdge(i + L, t, 1e9, 0);
            mcf.addEdge(s0, t, 1, 0);
            mcf.addEdge(i + L, t0, 1, 0);
        }



        for(auto x : q) {
            mcf.addEdge(getL(x.x), L + getR(x.y), 1, 1);
        }

        mcf.addEdge(t, s, 1e9, 0);

        mcf.calcMinCostFlow(s0, t0, 1e9);
        ans = q.size() - mcf.cost;
    }


    void print() {
        cout << "Case #" << test << ": ";
        cout << ans << "\n";
    }


} * solutions;

void solve(int test) {
    solutions[test].solve();
}


int main(int argc, char ** argv) {

#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define fname "sequence"
    //freopen(fname".in", "r", stdin);
    //freopen(fname".out", "w", stdout);
#endif
    int tests = nxt();

    solutions = new solution[tests];


    for (int i = 0; i < tests; ++i) {
        solutions[i].test = i + 1;
        solutions[i].read();
    }

    thread threads[tests];

    for (int i = 0; i < tests; ++i) {
        threads[i] = thread(solve, i);
    }

    for (int i = 0; i < tests; ++i) {
        threads[i].join();
        solutions[i].print();
    }
#ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC * 1000 << " ms." << endl;
#endif
    return 0;
}