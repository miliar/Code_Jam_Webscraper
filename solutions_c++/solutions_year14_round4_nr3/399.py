// Rain Dreamer MODEL
// Create @ 23:32 05-31 2014
// Comment - 

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>

using namespace std;

// Self Template Code BGEIN

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define all(x) (x).begin(), (x).end()
#define RD(x) freopen (x, "r", stdin)
#define WT(x) freopen (x, "w", stdout)
#define clz(x) memset (x, 0, sizeof(x))
#define cln(x) memset (x, -1, sizeof(x))
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)
#define repeach(i,x) for (__typeof((x).begin()) i = (x).begin(); i != (x).end(); ++i)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void ckmin(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void ckmax(T &a, const T b) { if (b > a) a = b; }

// Self Template Code END

const int maxn = 100 * 500 * 2 + 10;
const int inf = (-1u) >> 1;

struct graph {
    struct Adj {
        int v, c, b;
        Adj(int _v, int _c, int _b): v(_v), c(_c), b(_b) {}
        Adj() {};
    };
    int i, n, S, T, h[maxn], cnt[maxn];
    vector <Adj> adj[maxn];
    void clear() {
        for (i = 0; i < n; ++i)
            adj[i].clear();
        n = 0;
    }
    void insert(int u, int v, int c, int d = 0) {
        n = max(n, max(u, v) + 1);
        adj[u].push_back(Adj(v, c, adj[v].size()));
        adj[v].push_back(Adj(u, c * d, adj[u].size() - 1));
    }
    int maxflow(int _S, int _T) {
        S = _S, T = _T;
        fill(h, h + n, 0);
        fill(cnt, cnt + n, 0);
        int flow = 0;
        while (h[S] < n)
            flow += dfs(S, inf);
        return flow;
    }
    int dfs(int u, int flow) {
        if (u == T)
            return flow;
        int minh = n - 1, ct = 0;
        for (vector<Adj>::iterator it = adj[u].begin(); flow && it != adj[u].end(); ++it) {
            if (it -> c) {
                if (h[it -> v] + 1 == h[u]) {
                    int k = dfs(it -> v, min(it -> c, flow));
                    if (k) {
                        it -> c -= k;
                        adj[it -> v][it -> b].c += k;
                        flow -= k;
                        ct += k;
                    }
                    if (h[S] >= n)
                        return ct;
                }
                minh = min(minh, h[it -> v]);
            }
        }
        if (ct)
            return ct;
        if (--cnt[h[u]] == 0)
            h[S] = n;
        h[u] = minh + 1;
        ++cnt[h[u]];
        return 0;
    }
};

graph g;

int n, m, b, x1[12], x2[12], ya[12], yb[12];

bool is_inside(int x, int y, int i) {
    return x >= x1[i] && x <= x2[i] && y >= ya[i] && y <= yb[i];
}

int get_id(int x, int y, int flag) {
    return (x * m + y) * 2 + flag;
}

bool is_valid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

bool can_move(int x, int y) {
    if (!is_valid(x, y)) return false;
    rep (i, b) if (is_inside(x, y, i)) return false;
    return true;
}

const int di[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int main() {
    WT ("C.out");
    
    repcase {
        scanf ("%d%d%d", &n, &m, &b);
        rep (i, b) {
            scanf ("%d%d%d%d", &x1[i], &ya[i], &x2[i], &yb[i]);
        }
        g.clear();
        int S = 2 * n * m, T = 2 * n * m + 1;
        rep (i, n) rep (j, m) {
            if (!can_move(i, j)) continue;
            g.insert (get_id(i, j, 0), get_id(i, j, 1), 1);
            rep (k, 4) {
                int ni = i + di[k][0], nj = j + di[k][1];
                if (can_move(ni, nj)) {
                    g.insert (get_id(i, j, 1), get_id(ni, nj, 0), 1);
                }
            }
            if (j == 0) {
                g.insert (S, get_id(i, j, 0), 1);
            }
            if (j == m - 1) {
                g.insert (get_id(i, j, 1), T, 1);
            }
        }
        printf ("Case #%d: %d\n", Case++, g.maxflow(S, T));
    }
    return 0;
}

