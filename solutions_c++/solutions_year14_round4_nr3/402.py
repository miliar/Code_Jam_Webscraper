#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 2005;
//const int nmax = 205;
const int vmax = nmax * nmax * 4 + 5;
const int S = vmax - 2, T = vmax - 1;

struct Edge
{
	int from, to, flow, cap, id;
	Edge(int _from, int _to, int _cap, int _id)
	{
		from = _from;
		to = _to;
		flow = 0;
		cap = _cap;
		id = _id;
	}
};
vector < Edge > e;
vector < int > g[vmax];
int d[vmax], ptr[vmax];
queue < int > q;

void adde(int x, int y, int c)
{
	int id = sz(e);
	e.pb(Edge(x, y, c, id));
	g[x].pb(id);

	id = sz(e);
	e.pb(Edge(y, x, 0, id));
	g[y].pb(id);
}

bool bfs()
{
	_(d, -1);
	d[S] = 0;
	q.push(S);
	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		for (int i = 0; i < sz(g[v]); i ++)
		{
			Edge &t = e[g[v][i]];
			if (t.flow < t.cap && d[t.to] == -1)
			{
				d[t.to] = d[v] + 1;
				q.push(t.to);
			}
		}
	}
	return d[T] >= 0;
}

int dfs(int v, int flow = INF)
{
	if (!flow || v == T) return flow;
	for (; ptr[v] < sz(g[v]); ptr[v] ++)
	{
		Edge &t = e[g[v][ptr[v]]];
		if (d[v] + 1 == d[t.to])
		{
			int cur = dfs(t.to, min(flow, t.cap - t.flow));
			if (cur)
			{
				t.flow += cur;
				e[t.id ^ 1].flow -= cur;
				return cur;
			}
		}
	}
	return 0;
}

int dinic()
{
	int ret = 0, add;
	while (bfs())
	{
		_(ptr, 0);
		while (1)
		{
			add = dfs(S);
			if (!add) break;
			ret += add;
		}
	}
	return ret;
}

vector < int > Y;
int W, H, n, lx[nmax], rx[nmax], ly[nmax], ry[nmax];
int isFree[nmax][nmax];

void read()
{
	scanf("%d%d%d",&W,&H,&n);
	for (int i = 0; i < n; i ++)
	{
		scanf("%d%d%d%d",&lx[i],&ly[i],&rx[i],&ry[i]);
	}
}

void addy(int y)
{
	if (y - 1 >= 0) Y.pb(y - 1);
	Y.pb(y);
	if (y + 1 < H) Y.pb(y + 1);
}

void prep()
{
	Y.clear();
	Y.pb(0);
	Y.pb(H - 1);
	for (int i = 0; i < n; i ++)
	{
		addy(ly[i]);
		addy(ry[i]);
	}
	for (int i = 0; i < H; i ++)
		addy(i);
	sort(all(Y));
	Y.erase(unique(all(Y)), Y.end());
	
	for (int i = 0; i < n; i ++)
	{
		ly[i] = lower_bound(all(Y), ly[i]) - Y.begin();
		ry[i] = lower_bound(all(Y), ry[i]) - Y.begin();
	}
	H = sz(Y);

	for (int i = 0; i < H; i ++)
	{
		for (int j = 0; j < W; j ++)
		{
			isFree[i][j] = 1;
		}
	}

	for (int i = 0; i < n; i ++)
	{
		for (int y = ly[i]; y <= ry[i]; y ++)
		{
			for (int x = lx[i]; x <= rx[i]; x ++)
			{
				isFree[y][x] = 0;
			}
		}
	}
}

int getOpen(int x, int y)
{
	return (y * W + x) * 2;
}

int getClose(int x, int y)
{
	return (y * W + x) * 2 + 1;
}

const int dx[] = { -1, 1, 0, 0 };
const int dy[] = { 0, 0, -1, 1 };

bool in(int x, int y)
{
	return 0 <= x && x < W &&
		0 <= y && y < H;
}

void build()
{
	for (int i = 0; i < vmax; i ++)
		g[i].clear();
	e.clear();

	for (int x = 0; x < W; x ++)
	{
		if (isFree[0][x])
		{
			adde(S, getOpen(x, 0), 1);
		}
		if (isFree[H - 1][x])
		{
			adde(getClose(x, H - 1), T, 1);
		}

		for (int y = 0; y < H; y ++)
		{
			if (isFree[y][x])
			{
				adde(getOpen(x, y), getClose(x, y), 1);
				for (int i = 0; i < 4; i ++)
				{
					int nx = x + dx[i], ny = y + dy[i];
					if (in(nx,ny) && isFree[ny][nx])
					{
						adde( getClose(x, y), getOpen(nx, ny), 1 );
					}
				}
			}
		}
	}
}

bool solve()
{
	read();
	prep();
	build();
	int ans = dinic();
	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
