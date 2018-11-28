#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;
const int M = 500 + 3;

int good[N][M];
int n, m, k;

inline bool read()
{
	if (scanf("%d%d%d", &n, &m, &k) != 3)
		return false;

	memset(good, true, sizeof(good));

	forn(i, k)
	{
		int xa, ya, xb, yb;
		assert(scanf("%d%d%d%d", &xa, &ya, &xb, &yb) == 4);

		fore(x, xa, xb)
			fore(y, ya, yb)
				good[x][y] = false;
	}

    return true;
}

struct edge
{
	int to, c, f, rev;
};

const int V = 2 * N * M + 3;

int p[V], pe[V];
vector <edge> g[V];

inline void add (int u, int v, int c){

	edge forward = { v, c, 0, sz(g[v]) };
	edge back = { u, 0, 0, sz(g[u]) };
	g[u].pb(forward);
	g[v].pb(back);
}

inline bool enlarge (int s, int t){

	memset(p, -1, sizeof(p));
	queue <int> q;
	q.push (s);
	p[s] = s;

	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		
		forn (i, sz(g[v]))
		{
			int to = g[v][i].to;
			int c = g[v][i].c;
			int f = g[v][i].f;

			if (c - f > 0 && p[to] == -1)
			{
				p[to] = v;
				pe[to] = i;
				q.push (to);
			}
		}
	}
	
	if (p[t] == -1)
		return false;

	while (p[t] != t){

		g[ p[t] ][ pe[t] ].f++;
		g[ t ][ g[ p[t] ][ pe[t] ].rev ].f--;
		t = p[t];
	}
                          
	return true;
}

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, -1, 0, 1 };

inline int get(int x, int y, int t)
{
	int v = x * m + y;
	v = (2 * v + t);

	return v;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(v, 2 * n * m + 3)
		g[v].clear();

	int s = n * m * 2, t = s + 1;

	forn(x, n)
		forn(y, m)
		{
			if (!good[x][y])
				continue;

			add(get(x, y, 0), get(x, y, 1), 1);

			forn(i, 4)
			{
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (!correct(nx, ny, n, m))
					continue;

				if (!good[nx][ny])
					continue;

				add( get(x, y, 1), get(nx, ny, 0), 1);
			}

			if (y == 0)
				add(s, get(x, y, 0), 1);

			if (y == m - 1)
				add(get(x, y, 1), t, 1);
		}

	int ans = 0;
	
	while(enlarge(s, t))
		ans++;

	cout << ans << endl;
	cerr << test << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(scanf("%d", &testCnt) == 1);

	forn(test, testCnt)
	{
	    assert(read());
    	solve(test);
	}

    return 0;
}

