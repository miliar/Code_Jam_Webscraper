#undef NDEBUG
#ifdef SU2_PROJ
//#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int W = 100 + 3, H = 500 + 3;

int w, h, n;
int a[W][H];

inline bool read()
{
	if (scanf("%d%d%d", &w, &h, &n) != 3) return false;
	
	forn(i, w) forn(j, h) a[i][j] = 0;
	
	forn(i, n)
	{
		int x1, y1, x2, y2;
		assert(scanf("%d%d%d%d", &x1, &y1, &x2, &y2) == 4);
		
		fore(x, x1, x2)
			fore(y, y1, y2)
				a[x][y] = 1;
	}
	
	return true;
}

struct edge
{
	int to, c, f, rev;
};

int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };

const int N = 2 * W * H + 13;
vector<edge> g[N];

inline void add(int from, int to, int c)
{
	edge f = { to, c, 0, sz(g[to]) };
	edge b = { from, 0, 0, sz(g[from]) };
	
	g[from].pb(f);
	g[to].pb(b);
}

int lev[N];
int head, tail, q[N];

inline bool bfs(int s, int t)
{
	memset(lev, 63, sizeof(lev));
	head = tail = 0;

	lev[s] = 0;
	q[head++] = s;

	while (head != tail)
	{
		int v = q[tail++];

		forn(i, sz(g[v]))
			if (g[v][i].f < g[v][i].c && lev[g[v][i].to] > lev[v] + 1)
			{
				lev[g[v][i].to] = lev[v] + 1;
				q[head++] = g[v][i].to;
			}
	}

	return lev[t] < INF / 2;
}

int ptr[N];

int dfs(int v, int t, int f)
{
	if (v == t) return f;

	for ( ; ptr[v] < sz(g[v]); ptr[v]++)
	{
		edge& e = g[v][ptr[v]];
		if (e.f == e.c || lev[e.to] != lev[v] + 1) continue;

		int df = dfs(e.to, t, min(f, e.c - e.f));

		if (df > 0)
		{
			e.f += df;
			g[e.to][e.rev].f -= df;
			return df;
		}
	}

	return 0;
}

inline int dinic(int s, int t)
{
	int ans = 0;

	while (bfs(s, t))
	{
		memset(ptr, 0, sizeof(ptr));

		for (int f; (f = dfs(s, t, INF)) != 0; ans += f);
	}

	return ans;
}


inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	int s = 2 * w * h, t = s + 1;
	
	forn(i, t + 1) g[i].clear();
	
	forn(i, w)
		forn(j, h)
		{
			if (a[i][j] == 1) continue;
			
			forn(k, 4)
			{
				int x = i + dx[k], y = j + dy[k];
				if (!correct(x, y, w, h) || a[x][y] == 1) continue;
				
				add(2 * (i * h + j) + 1, 2 * (x * h + y), 1);
			}
			
			add(2 * (i * h + j), 2 * (i * h + j) + 1, 1);
			
			if (j == 0) add(s, 2 * (i * h + j), 1);
			if (j == h - 1) add(2 * (i * h + j) + 1, t, 1);
		}
		
	printf("%d\n", dinic(s, t));
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
    	cerr << test << endl;
	    assert(read());
    	solve(test);
    }
    
#ifdef SU2_PROJ
    cerr << "== TIME: " << clock() << " ==" << endl;
#endif

    return 0;
}
