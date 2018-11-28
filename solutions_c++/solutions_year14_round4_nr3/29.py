#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#if __cplusplus > 201103L
#include <initializer_list>
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#ifdef LOCAL
#define DEBUG
#endif

#define oo 0x3F3F3F3F
#define fst first
#define snd second
#define PB push_back
#define SZ(x) (int)((x).size())
#define ALL(x) (x).begin(), (x).end()
#define FOR(i, a, b) for (int _end_ = (b), i = (a); i <= _end_; ++i)
#define ROF(i, a, b) for (int _end_ = (b), i = (a); i >= _end_; --i)

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

int64 fpm(int64 b, int64 e, int64 m) { int64 t = 1; for (; e; e >>= 1, b = b * b % m) e & 1 ? t = t * b % m : 0; return t; }
template<class T> inline bool chkmin(T &a, T b) {return a > b ? a = b, true : false;}
template<class T> inline bool chkmax(T &a, T b) {return a < b ? a = b, true : false;}
template<class T> inline T sqr(T x) {return x * x;}
template <typename T> T gcd(T x, T y) {for (T t; x; ) t = x, x = y % x, y = t; return y; }

template<class edge> struct Graph {
    vector<vector<edge> > adj;
    Graph(int n) {adj.clear(); adj.resize(n + 5);}
    Graph() {adj.clear(); }
    void resize(int n) {adj.resize(n + 5); }
    void add(int s, edge e){adj[s].push_back(e);}
    void del(int s, edge e) {adj[s].erase(find(iter(adj[s]), e)); }
    vector<edge>& operator [](int t) {return adj[t];}
};

const int N = 1e3 + 10;

int o[N], lx[N], rx[N], ly[N], ry[N], dist[N];

bool intersect(int a, int b, int c, int d) {
    return (a <= c && c <= b) || (a <= d && d <= b) || (c <= a && a <= d) || (c <= b && b <= d);
}

int D(int a, int b) {
    int dy = min(abs(ly[a] - ry[b] - 1), abs(ly[b] - ry[a] - 1));
    int dx = min(abs(lx[a] - rx[b] - 1), abs(lx[b] - rx[a] - 1));
    if (intersect(lx[a], rx[a], lx[b], rx[b])) return dy;
    if (intersect(ly[a], ry[a], ly[b], ry[b])) return dx;
    return max(dx, dy);
}

int main(int argc, char **argv) {
#ifdef LOCAL
    freopen("C-large.in" , "r", stdin);
    freopen("c.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        int w, h, b;
        
        scanf("%d%d%d", &w, &h, &b);
        for (int i = 1; i <= b; ++i)
            scanf("%d%d%d%d", lx + i, ly + i, rx + i, ry + i);
        int p = 0, q = b + 1;
        lx[p] = -1, rx[p] = -1, ly[p] = 0, ry[p] = 1e9;
        lx[q] =  w, rx[q] =  w, ly[q] = 0, ry[q] = 1e9;

        memset(dist, 0x3F, sizeof(dist));
        memset(o, 0, sizeof(o));
        dist[0] = 0;
        for (int _ = 0; _ <= b; ++_) {
            int x = 0;
            for (int i = 0; i <= b; ++i)
                if (!o[i] && (o[x] || dist[i] < dist[x]))
                    x = i;

            o[x] = true;
            for (int i = 0; i <= b + 1; ++i)
                chkmin(dist[i], dist[x] + D(x, i));
        }
        printf("Case #%d: %d\n", tc, dist[b + 1]);
    }

    return 0; 
}
