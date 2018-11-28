#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif
#undef NDEBUG

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
#define forit(i, a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
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

const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const int INF = int(1e9) + 7;

const int G = 100500;

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

const int NMAX = 550;
const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};

int bad[NMAX][NMAX], n, m, k;

int input(int i, int j){
    int id = i * m + j;
    return id;
}

int output(int i, int j){
    int id = i * m + j;
    return id + n * m;
}

void solve_test(){
    memset(bad, 0, sizeof bad);
    cin >> n >> m >> k;
    forn(badi, k){
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        fori(x, x0, x1){
            fori(y, y0, y1){
                bad[x][y] = 1;
            }
        }
    }

    forn(i, G)
        g[i].clear();

    int S = n * m * 2, T = S + 1;
    assert(T < G);
    forn(i, n){
        forn(j, m){
            if(bad[i][j])
                continue;
            addEdge(input(i, j), output(i, j), 1);
            forn(dr, 4){
                int ni = i + dx[dr];
                int nj = j + dy[dr];

                if(0 <= ni && ni < n && 0 <= nj && nj < m && !bad[ni][nj]){
                    addEdge(output(i, j), input(ni, nj), 1);
                }
            }
        }
    }

    forn(i, n){
        if(!bad[i][0]){
            addEdge(S, input(i, 0), 1);
        }
        if(!bad[i][m - 1]){
            addEdge(output(i, m - 1), T, 1);
        }
    }
    
    printf("%d\n", maxFlow(S, T));
}

int main() {
    #ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
//    freopen("output.txt", "wt", stdout);
    #endif

    int tcases;
    cin >> tcases;
    fori(i, 1, tcases){
        printf("Case #%d: ", i);
        solve_test();
        fprintf(stderr, "-- Time for case %d = %.3lf\n\n", i, (((double)clock())/CLOCKS_PER_SEC));
    }

    return 0;
}


