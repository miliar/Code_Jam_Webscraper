#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <cstring>
#include <string.h>
#include <sstream>
#include <cmath>
#include <math.h>
#include <queue>
#include <deque>
#include <cassert>
#include <time.h>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}

/*const int NMAX = 155000;
int target, source;

class edge
{
public:
	int from, to, cap, flow;
	edge() {}
	edge (int a, int b, int c, int d) { from = a; to = b; cap = c; flow = d;  }
};

vector <edge> e;
vector <int> g[NMAX];
int ptr[NMAX];

void add(int i, int j, int c)
{
	g[i].pb ( e.size());
	e.pb  ( edge(i, j, c, 0) );

	g[j].pb ( e.size() );
	e.pb ( edge(j, i, 0, 0) );
}

int r[NMAX];
int q[NMAX*4], qh = 0, qt = 0;

bool bfs()
{
	q[qt ++] = source;
	
	_(r, -1);
	r[source] = 0;
	while (qh < qt)
	{
		int v = q[qh++];
		forn(i, g[v].size())
		{
			int id = g[v][i];
			int u = e[id].to;
			if (r[u] == -1 && e[id].flow < e[id].cap)
			{
				r[u] = r[v] + 1;
				q[qt++] = u;
			}
		}
	}

	return r[target] != -1;
}

int dfs(int v, int flow)
{
	if (v == target || !flow)
		return flow;
	for (int &i = ptr[v]; i < (int)g[v].size(); i++)
	{
		int id = g[v][i];
		if (r[e[id].to] == r[v] + 1)
		{
			int f = dfs(e[id].to, min(flow, e[id].cap - e[id].flow));
			if (f)
			{
				e[id].flow += f;
				e[id ^ 1].flow -= f;
				return f;
			}
		}
	}
	return 0;
}

int dinic()
{
	int res = 0;
	while (bfs ())
	{
		_(ptr, 0);
		while (int p = dfs(source, 2*INF))
			res += p;
	}
	return res;
}*/

const int MAXN = 155555; // число вершин
 
struct edge {
	int a, b, cap, flow;
};
 
int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];
 
void add (int a, int b, int cap) {
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].push_back ((int) e.size());
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}
 
bool bfs() {
	int qh=0, qt=0;
	q[qt++] = s;
	memset (d, -1, n * sizeof d[0]);
	d[s] = 0;
	while (qh < qt && d[t] == -1) {
		int v = q[qh++];
		for (size_t i=0; i<g[v].size(); ++i) {
			int id = g[v][i],
				to = e[id].b;
			if (d[to] == -1 && e[id].flow < e[id].cap) {
				q[qt++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[t] != -1;
}
 
int dfs (int v, int flow) {
	if (!flow)  return 0;
	if (v == t)  return flow;
	for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
		int id = g[v][ptr[v]],
			to = e[id].b;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) {
			e[id].flow += pushed;
			e[id^1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}
 
int dinic() {
	int flow = 0;
	for (;;) {
		if (!bfs())  break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
			flow += pushed;
	}
	return flow;
}

const int WMAX = 555, HMAX = 555;
int w, h, b;
int a[WMAX][HMAX];

void clear()
{
	e.clear();
	forn(i, MAXN) g[i].clear();
}

void read()
{
	clear();
	scanf("%d %d %d", &w, &h, &b);
	forn(i, WMAX) forn(j, HMAX) a[i][j] = 1;
	forn(it, b)
	{
		int x0_, y0_, x1_, y1_;
		scanf("%d %d %d %d", &x0_, &y0_, &x1_, &y1_);
		for(int i = x0_; i <= x1_; i++)
		{
			for(int j = y0_; j <= y1_; j++)
			{
				a[i][j] = 0;
			}
		}
	}
}

void solve()
{
	s = MAXN - 1;
	t = MAXN - 2;
	n = MAXN;
	int dx[] = {1, 0, -1, 0};
	int dy[] = {0, 1, 0, -1};
	
	for(int i = 0; i < w; i++)
	{
		for(int j = 0; j < h; j++)
		{
			if (a[i][j] == 1)
			{
				add((i*h + j)*2, (i*h + j)*2 + 1, 1);
				for(int k = 0; k < 4; k++)
				{
					int x, y;
					x = i + dx[k];
					y = j + dy[k];
					if (0 <= x && x < w && 0 <= y && y < h && a[i][j] == 1 && a[x][y] == 1)
					{
						add((i*h + j)*2 + 1, (x*h + y)*2, 1);
					}
				}
			}
		}
	}
	
	for(int i = 0; i < w; i++)
	{
		if (a[i][0] == 1)
			add(s, i*h*2, 1);
		if (a[i][h - 1] == 1)
			add((i*h + h - 1)*2 + 1, t, 1);
	}
	
	int flow = dinic();
	printf("%d\n", flow);
}

int main ()
{
	prepare ("");

	int t;
	scanf("%d", &t);
	forn(i, t)
	{
		dbgx( i );
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}

	return 0;
}
