#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

#define TEST "small"
namespace MAXFLOW {
const int maxn = 300500;
const int inf = 1e9;
struct Edge {
    int to, cap, fl;
    Edge(int to, int cap, int fl): to(to), cap(cap), fl(fl) {}
};

vector<Edge> edges;
vi g[maxn];
int d[maxn], p[maxn], q[maxn];

void addEdge(int from, int to, int cap = 1) {
    g[from].pb(edges.size());
    edges.pb(Edge(to, cap, 0));
    g[to].pb(edges.size());
    edges.pb(Edge(from, 0, 0));
}

bool dfs(int v, int fin, int lim) {
    if (v == fin)
        return true;
    while (p[v] < (int)g[v].size()) {
        int num = g[v][p[v]];
        Edge ed = edges[num];
        if (d[ed.to] == d[v] + 1 && ed.cap - ed.fl >= lim) {
            if (dfs(ed.to, fin, lim)) {
                edges[num].fl+=lim;
                edges[num^1].fl-=lim;
                return true;
            }
        }
        p[v]++;
    }
    return false;
}

void bfs(int st, int lim, int n) {
    fill (d, d + n + 1, inf);
    q[0] = st;
    d[st] = 0;
    int head = 0, tail = 1;
    while (head < tail) {
        int v = q[head++];
        forn(i, g[v].size()) {
            Edge ed = edges[g[v][i]];
            if (ed.cap - ed.fl >= lim && d[ed.to] > d[v] + 1) {
                d[ed.to] = d[v] + 1;
                q[tail++] = ed.to;
            }
        }
    }
}

int calcFlow(int n, int st, int fin) {
    int lim = 1, ans = 0; // set lim(lim is maximal possible weight of edge)
    while (lim) {
        while (true) {
            bfs(st, lim, n);
            if (d[fin] == inf)
                break;
            fill(p, p + n + 1, 0);
            while (dfs(st, fin, lim))
                ans+=lim;
        }
        lim /= 2;
    }
    return ans;
}

void init()
{
	forn (i, maxn)
		g[i].clear();
}
}

const int N = 1010;
bool a[N][N * 3];
int W;

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

void f(int& x, const vi& a)
{
    x = lower_bound(all(a), x) - a.begin();
}

void add(vi& a, int h, int x)
{
    for (int k = -1; k <= 1; k++)
        if (x + k >= 0 && x + k < h)
            a.pb(x + k);
}

int g(int x, int y, int t)
{
    return (x + y * W) * 2 + t;
}

int solve()
{
    forn (i, N) forn (j, N) a[i][j] = false;
    int w, h, b;
    cin >> w >> h >> b;
    W = w;
    int n = b;
    vi x0(n), x1(n), y0(n), y1(n);
    //vi ay; ay.pb(0); ay.pb(h - 1);
    forn (i, n) {
        cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
        x0[i] = max(x0[i], 0);
        x1[i] = min(x1[i], w - 1);
        y0[i] = max(y0[i], 0);
        y1[i] = min(y1[i], h - 1);
        //add(ay, h, y0[i]);
        //add(ay, h, y1[i]);
    }
    //sort(all(ay)); ay.resize(unique(all(ay)) - ay.begin());
    //for1 (i, w) for1 (j, ay.size()) a[i][j] = true;
    for1 (i, w) for1 (j, h) a[i][j] = 1;
    forn (i, n)
    {
        //f(y0[i], ay);
        //f(y1[i], ay);
        for (int x = x0[i]; x <= x1[i]; x++)
            for (int y = y0[i]; y <= y1[i]; y++)
                a[x + 1][y + 1] = false;
    }
/*
    cerr << ay.size() << endl;
    
    
    forn (j, ay.size() + 2) {
    forn (i, w + 2) 
            cerr << a[i][j];
        cerr << endl;
    }
*/    
    MAXFLOW::init();
    int st = 0, fin = 1;
    for1 (i, w) {
        if(a[i][1]){
            MAXFLOW::addEdge(st, g(i, 1, 0));
        }
        if (a[i][h])
            MAXFLOW::addEdge(g(i, h, 1), fin);
    }
    for1 (i, w)
        for1 (j, h)
            if (a[i][j])
            {
                MAXFLOW::addEdge(g(i, j, 0), g(i, j, 1));
                forn (t, 4)
                {
                    int ni = dx[t] + i, nj = dy[t] + j;
                    if (a[ni][nj])
                        MAXFLOW::addEdge(g(i, j, 1), g(ni, nj, 0));
                }
            }
    return MAXFLOW::calcFlow((1+h) * (w+1) * 2 + 5, st, fin);
}

int main() {
#ifndef TEST
	freopen("input.txt", "r", stdin);
#else 
    freopen(TEST".in", "r", stdin);
    freopen(TEST".out", "w", stdout);
#endif
    int T;
    cin >> T;
    for1 (t, T)
	{
		cout << "Case #" << t << ": ";
	    cout << solve() << "\n";
    }
	return 0;
}
