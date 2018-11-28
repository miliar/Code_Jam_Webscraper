#include "../../lib/include.h"

// #define MAXV 2*(100*100)+100
// int d[MAXV], p[MAXV], pot[MAXV];
// struct cmp {
//     bool operator ()(int i, int j) {
//         return d[i] == d[j] ? i < j : d[i] < d[j];
//     }
// };
// struct flow_network {
//     struct edge {
//         int v, cap, cost, nxt;
//         edge(int _v, int _cap, int _cost, int _nxt)
//             : v(_v), cap(_cap), cost(_cost), nxt(_nxt) {  }
//     };
//     int n, ecnt, *head;
//     vector<edge> e, e_store;
//     flow_network(int _n, int m = -1) : n(_n), ecnt(0) {
//         e.reserve(2 * (m == -1 ? n : m));
//         memset(head = new int[n], -1, n << 2);
//     }
//     void destroy() { delete[] head; }
//     void reset() { e = e_store; }
//     void add_edge(int u, int v, int cost, int uv, int vu=0) {
//         e.push_back(edge(v, uv, cost, head[u])); head[u] = ecnt++;
//         e.push_back(edge(u, vu, -cost, head[v])); head[v] = ecnt++;
//     }
//     ii min_cost_max_flow(int s, int t, bool res = true) {
//         if (s == t) return ii(0, 0);
//         e_store = e;
//         memset(pot, 0, n << 2);
//         int f = 0, c = 0, v;
//         while (true) {
//             memset(d, -1, n << 2);
//             memset(p, -1, n << 2);
//             set<int, cmp> q;
//             q.insert(s); d[s] = 0;
//             while (!q.empty()) {
//                 int u = *q.begin();
//                 q.erase(q.begin());
//                 for (int i = head[u]; i != -1; i = e[i].nxt) {
//                     if (e[i].cap == 0) continue;
//                     int cd = d[u] + e[i].cost + pot[u] - pot[v = e[i].v];
//                     if (d[v] == -1 || cd < d[v]) {
//                         if (q.find(v) != q.end()) q.erase(q.find(v));
//                         d[v] = cd; p[v] = i;
//                         q.insert(v);
//                     }
//                 }
//             }
//             if (p[t] == -1) break;
//             int x = INF, at = p[t];
//             while (at != -1) x = min(x, e[at].cap), at = p[e[at^1].v];
//             at = p[t], f += x;
//             while (at != -1)
//                 e[at].cap -= x, e[at^1].cap += x, at = p[e[at^1].v];
//             c += x * (d[t] + pot[t] - pot[s]);
//             for (int i = 0; i < n; i++) if (p[i] != -1) pot[i] += d[i];
//         }
//         if (res) reset();
//         return ii(f, c);
//     }
// };


struct solver {

    solver() {
    }

    void solve(bool process, istream &cin, ostream &cout) {

        int dx[4] = {-1,0,1,0};
        int dy[4] = {0,1,0,-1};

        char arr[110][110];
        int n, m;
        cin >> n >> m;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> arr[i][j];
            }
        }

        LOGIC;

        int cnt = 0;
        bool ok = true;
        for (int i = 0; ok && i < n; i++) {
            for (int j = 0; ok && j < m; j++) {

                if (arr[i][j] == '.')
                    continue;

                int curd = -1;
                switch (arr[i][j]) {
                    case '^': curd = 0; break;
                    case '>': curd = 1; break;
                    case 'v': curd = 2; break;
                    case '<': curd = 3; break;
                    default:
                              assert(false);
                }


                int mn = INF;
                for (int d = 0; d < 4; d++) {
                    int x = i,
                        y = j;
                    bool curok = false;
                    while (true) {
                        x += dx[d];
                        y += dy[d];
                        if (x < 0 || x >= n || y < 0 || y >= m)
                            break;
                        if (arr[x][y] != '.') {
                            curok = true;
                            break;
                        }
                    }

                    if (curok) {
                        if (d == curd)
                            mn = min(mn, 0);
                        else
                            mn = min(mn, 1);
                    }
                }

                if (mn == INF) {
                    ok = false;
                    break;
                }

                cnt += mn;
            }
        }

        OUTPUT;

        if (!ok) cout << "IMPOSSIBLE" << endl;
        else cout << cnt << endl;

    }
};

// see https://github.com/SuprDewd/GoogleCodeJamRunner
#include "../../lib/gcj.h"
