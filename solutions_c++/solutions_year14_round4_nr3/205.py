#undef NDEBUG
#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int N = 2010;
const int G = 100500;
const int INF = int(1e9) + 1;

const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};

struct edge {
    int to, f, c, rev;
};

vector<edge> g[G];

void addEdge(int fr, int to, int c) {
    edge fw = {to, 0, c, sz(g[to])};
    edge bw = {fr, 0, 0, sz(g[fr])};
    
    g[fr].pb(fw);
    g[to].pb(bw);
}

int lvl[G];

bool bfs(int s, int t) {
    memset(lvl, -1, sizeof(int) * (t + 1));
    lvl[s] = 0;
    
    queue<int> q;
    q.push(s);
    
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        
        forn(i, sz(g[v])) {
            const edge& e = g[v][i];
            
            if (e.f < e.c && lvl[e.to] == -1) {
                lvl[e.to] = lvl[v] + 1;
                q.push(e.to);
            }
        }
    }
    
    return lvl[t] != -1;
}

int ptr[G];

int dfs(int v, int f, int t) {
    if (v == t || f == 0)
        return f;
        
    for(;ptr[v] < sz(g[v]); ptr[v]++) {
        edge& e = g[v][ptr[v]];
        
        if (e.f == e.c || lvl[e.to] != lvl[v] + 1)
            continue;
            
        int cf = dfs(e.to, min(f, e.c - e.f), t);
        if (cf > 0) {
            e.f += cf;
            g[e.to][e.rev].f -= cf;
            return cf;
        }
    }
    
    return 0;
}

int maxFlow(int s, int t) {
    int ans = 0;
    
    while (bfs(s, t)) {
        memset(ptr, 0, sizeof(int) * (t + 1));
        while (int f = dfs(s, INF, t))
            ans += f;
    }
    
    return ans;
}

int n, m, c;

int cused;
int used[N][N];

inline bool good(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m && used[x][y] < cused;
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    #endif

    int tests;
    cin >> tests;
    
    forn(test, tests) {
        cin >> n >> m >> c;
        
        int s = 2 * n * m;
        int t = s + 1;
        
        forn(i, t + 1)
            g[i].clear();
            
        cused++;
        forn(i, c){
            int xlf, xrg, ylf, yrg;
            assert(scanf("%d %d %d %d", &xlf, &ylf, &xrg, &yrg) == 4);
            if (xlf > xrg)
                swap(xlf, xrg);
            if (ylf > yrg)
                swap(ylf, yrg);
                
            for (int x = xlf; x <= xrg; ++x)
                for (int y = ylf; y <= yrg; ++y)
                    used[x][y] = cused;                
        }
                        
        forn(x, n)
            forn(y, m) {
                if (used[x][y] == cused)
                    continue;
                    
                if (y == 0)
                    addEdge(s, x*m + y, 1);
                addEdge(x*m + y, x*m + y + n*m, 1);
                if (y == m - 1)
                    addEdge(x*m + y + n*m, t, 1);
                    
                forn(dir, 4) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (good(nx, ny))
                        addEdge(x*m + y + n*m, nx*m + ny, 1);
                }
            }
            
        cerr << test << endl;
        printf("Case #%d: %d\n", test + 1, maxFlow(s, t));                
    }
 
    return 0;
}

