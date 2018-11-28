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

#define inf 0x3F3F3F3F
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

int a[N], b[N], f[N][N], bit[N];

int main(int argc, char **argv) {
    freopen("B-large.in", "r", stdin);
    int T;
    
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        int n;
        
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d", &a[i]), b[i] = a[i];
        sort(b + 1, b + n + 1);
        
        memset(f, 0x3F, sizeof(f)), f[1][1] = 0;
        for (int i = 1; i <= n; ++i) {
            int x = 1;
            for (; a[x] != b[i]; ++x)
                ;
            int p = 0, q = 0;
            for (int j = 1; j <= n; ++j)
                if (a[j] > b[i]) {
                    if (j < x) ++p;
                    if (j > x) ++q;
                }
            
            for (int j = 1; j <= n; ++j) {
                chkmin(f[i + 1][j    ], f[i][j] + q);
                chkmin(f[i + 1][j + 1], f[i][j] + p);
            }
        }

        int ans = inf;
        for (int i = 1; i <= n + 1; ++i)
            chkmin(ans, f[n + 1][i]);
        
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}
