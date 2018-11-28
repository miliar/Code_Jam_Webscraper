#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <ext/rope>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <ratio>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<double, int> pdi;

const int INF = 0x3f3f3f3f;
const int MAXN = 100002;
const int MAXM = 1000000;
const int MOD = 1000000007;
const ll INFLL = 0x3f3f3f3f3f3f3f3fLL;
const double EPS = 1e-8;
const double PI = acos(-1.0);

#define DEBUG(args...) fprintf(stderr, args)
#define all(c) (c).begin(), (c).end()
#define pb push_back

template<typename U, typename V> void add(U& ret, const V& val) { ret = (ll)(ret + val) % MOD; }
template<typename U, typename V> void chkmax(U& ret, const V& val) { if (ret < val) { ret = val; } }
template<typename U, typename V> void chkmin(U& ret, const V& val) { if (val < ret) { ret = val; } }
template<typename T> T gcd(T a, T b) { return a == 0 ? b : gcd(b % a, a); }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

struct Sap {
#define RE(i) ((((i) - P) ^ 1) + P)
    struct Edge {
        int v, c;
        Edge* next;
        Edge(int v = 0, int c = 0, Edge* next = NULL) : v(v), c(c), next(next) {}
    };

    int n, S, T, psize, len;
    int maxflow;
    int c[MAXN];
    int d[MAXN];
    int path[MAXN];
    Edge* curr[MAXN];
    Edge P[MAXM * 2];
    Edge* e[MAXN];

    void bfs() {
        queue<int> q;
        fill(d, d + n, n);
        fill(c, c + n, 0);
        q.push(T);
        d[T] = 0;
        while (!q.empty()) {
            int top = q.front();
            q.pop();
            ++c[d[top]];
            for (Edge* i = e[top]; i != NULL; i = i->next) {
                if (d[i->v] == n) {
                    d[i->v] = d[top] + 1;
                    q.push(i->v);
                }
            }
        }
    }

    int flow(int _S, int _T) {
        n = max(n, max(S = _S, T = _T)) + 1;
        bfs();
        for (int i = 0; i < n; ++i) {
            curr[i] = e[i];
        }
        path[maxflow = len = 0] = S;
        while (d[S] != n) {
            int u = path[len];
            if (u == T) {
                int minf = INF;
                int last = -1;
                for (int i = 0; i < len; ++i) {
                    if (curr[path[i]]->c < minf) {
                        minf = curr[path[i]]->c;
                        last = i;
                    }
                }
                for (int i = 0; i < len; ++i) {
                    curr[path[i]]->c -= minf;
                    RE(curr[path[i]])->c += minf;
                }
                len = last;
                maxflow += minf;
            } else {
                for (; curr[u] != NULL && (d[curr[u]->v] != d[u] - 1 || curr[u]->c == 0); curr[u] = curr[u]->next);
                if (curr[u] == NULL) {
                    if (--c[d[u]] == 0) {
                        break;
                    } else {
                        d[u] = n;
                        for (Edge* i = e[u]; i != NULL; i = i->next) {
                            if (d[i->v] + 1 < d[u] && i->c != 0) {
                                d[u] = d[i->v] + 1;
                                curr[u] = i;
                            }
                        }
                        ++c[d[u]];
                        (u != S) && (len--);
                    }
                } else {
                    path[++len] = curr[u]->v;
                }
            }
        }
        return maxflow;
    }

    void init() {
        n = psize = 0;
        memset(e, 0, sizeof(e));
    }

    void addEdge(int u, int v, int c) {
        P[psize] = Edge(v, c, e[u]);
        e[u] = &P[psize++];
        P[psize] = Edge(u, 0, e[v]);
        e[v] = &P[psize++];
        n = max(n, max(u, v));
    }

    void addUEdge(int u, int v, int c) {
        P[psize] = Edge(v, c, e[u]);
        e[u] = &P[psize++];
        P[psize] = Edge(u, c, e[v]);
        e[v] = &P[psize++];
        n = max(n, max(u, v));
    }
} sap;

const int DR[] = {-1, 0, 1, 0};
const int DC[] = {0, -1, 0, 1};

int W, H, B;
int s[500][100];
int res;

void init() {
}

void input() {
    memset(s, 0, sizeof(s));
    scanf("%d%d%d", &W, &H, &B);
    for (int i = 0; i < B; ++i) {
        int x0, y0, x1, y1;
        scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
        for (int j = x0; j <= x1; ++j) {
            for (int k = y0; k <= y1; ++k) {
                s[k][j] = 1;
            }
        }
    }
}

int id(int r, int c) {
    return r * W + c;
}

void solve() {
    sap.init();
    int N = H * W;
    int S = N * 2, T = S + 1;
    for (int i = 0; i < W; ++i) {
        sap.addEdge(S, id(0, i), 1);
    }
    for (int i = 0; i < W; ++i) {
        sap.addEdge(id(H - 1, i) + N, T, 1);
    }
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (s[i][j] == 1) {
                continue;
            }
            sap.addEdge(id(i, j), id(i, j) + N, 1);
            for (int k = 0; k < 4; ++k) {
                int r = i + DR[k];
                int c = j + DC[k];
                if (r >= 0 && r < H && c >= 0 && c < W && s[r][c] == 0) {
                    sap.addEdge(id(i, j) + N, id(r, c), 1);
                }
            }
        }
    }
    res = sap.flow(S, T);
}


int main(int argc, char** argv) {
    int totalCaseNumber = 1;

    init();

    scanf("%d", &totalCaseNumber);
    for (int caseNum = 1; caseNum <= totalCaseNumber; ++caseNum) {
        input();
        solve();
        printf("Case #%d: %d\n", caseNum, res);
    }

    return 0;
}
