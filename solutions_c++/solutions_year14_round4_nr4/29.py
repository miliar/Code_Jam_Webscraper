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

const int NN = 1e5 + 10, N = 1e2 + 10, MOD = 1e9 + 7;

struct node {
    int x;
    int64 f, g; bool o;
    node *c[27];
} ;

node buf[NN], *bptr = buf, *root;
char S[N];
int n, m;
int64 cb[N][N], fac[N];

node *get_new() {
    return *++bptr = (node){0}, bptr;
}

void insert() {
    node *p = root; ++p->x;
    for (int i = 1; S[i]; ++i) {
        int c = S[i] - 'A';
        if (!p->c[c]) p->c[c] = get_new();
        p = p->c[c];
        ++p->x;
    }
    p->o = true;
}

void dfs(node *p) { 
    // if (p->x < n) {
    //     p->f = p->g = 1;
    //     return ;
    // }
    p->x = min(p->x, n), p->f = p->x, p->g = 1;

    int64 g[N + 1];
    for (int i = 1; i <= p->x; ++i) g[i] = 1;
    for (int c = 0; c < 26; ++c) {
        node *x = p->c[c];
        if (!x) continue;
        dfs(x);
        p->f += x->f;
        p->g = p->g * x->g % MOD;
        for (int i = 1; i <= p->x; ++i)
            g[i] = g[i] * cb[i][x->x] % MOD;
    }
    if (p->o)
        for (int i = 1; i <= p->x; ++i)
            g[i] = g[i] * i % MOD;
    for (int i = 1; i <= p->x; ++i)
        for (int j = 1; j < i; ++j)
            g[i] = (g[i] + MOD - g[j] * cb[i][j] % MOD) % MOD;
    p->g = p->g * g[p->x] % MOD;
}

int main(int argc, char **argv) {
#ifdef LOCAL
    // freopen("d.in" , "r", stdin);
    freopen("D-large.in" , "r", stdin);
    freopen("d-2.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    
    int T;
    scanf("%d", &T);
    for (int i = 0; i < N; ++i)
        for (int j = 0; j <= i; ++j)
            cb[i][j] = j ? (cb[i - 1][j - 1] + cb[i - 1][j]) % MOD : 1;
    fac[0] = 1;
    for (int i = 1; i < N; ++i)
        fac[i] = fac[i - 1] * i % MOD;
    
    for (int tc = 1; tc <= T; ++tc) {
        bptr = buf, root = get_new();
        scanf("%d%d", &m, &n);
        for (int i = 1; i <= m; ++i) {
            scanf("%s", S + 1);
            // S[strlen(S + 1) + 1] = 'A' + 26;
            // S[strlen(S + 1) + 2] = '\0';
            
            insert();
        }
        dfs(root);
        printf("Case #%d: %d %d\n", tc, (int)root->f, (int)root->g);
        fprintf(stderr, "%d\n", tc);
    }


    return 0; 
}

