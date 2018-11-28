#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int MAXN = 600020; // число вершин
const int INF = 1000000000; // константа-бесконечность
 
struct edge {
	int a, b, cap, flow;
};
 
int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];

void init()
{
	e.clear();
	for (int i = 0; i < n; ++i)
		g[i].clear();
	memset(d, 0, sizeof(d));
	memset(ptr, 0, sizeof(ptr));
	memset(q, 0, sizeof(q));
}
 
void add_edge_2 (int a, int b, int cap) {
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].push_back ((int) e.size());
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}

void add_edge (int a, int b, int cap) {
	//~ printf("ED %d %d %d\n", a, b, cap);
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
			//~ printf("PU %d %d %d\n", e[id].a, e[id].b, pushed);
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
		//~ printf("aa 1\n");
		if (!bfs())  break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
		{
			//~ printf("pushed %d\n", pushed);
			flow += pushed;
		}
	}
	return flow;
}

int w, h, b;
bool bl[128][512];

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

int ein(int x, int y)
{
	return (x * h + y) * 4;
}

int emid1(int x, int y)
{
	return (x * h + y) * 4 + 1;
}

int emid2(int x, int y)
{
	return (x * h + y) * 4 + 2;
}

int eout(int x, int y)
{
	return (x * h + y) * 4 + 3;
}

int main()
{
	int te, T;
	scanf("%d", &T);
	for (te = 1; te <= T; ++te)
	{
		scanf("%d %d %d", &w, &h, &b);
		memset(bl, 0, sizeof(bl));
		n = w * h * 4 + 2;
		s = n - 2;
		t = n - 1;
		init();
		for (int i = 0; i < b; ++i)
		{
			int x0, x1, y0, y1;
			scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
			for (int j = x0; j <= x1; ++j)
				for (int k = y0; k <= y1; ++k)
				{
					//~ printf("BL %d %d __ %d\n", j, k, ein(j, k));
					bl[j][k] = 1;
				}
		}

		for (int i = 0; i < w; ++i)
		{
			if (!bl[i][0])
				add_edge(s, ein(i, 0), 1);
			if (!bl[i][h-1])
				add_edge(eout(i, h-1), t, 1);
		}
		
		for (int i = 0; i < w; ++i)
		{
			for (int j = 0; j < h; ++j)
			{
				//~ printf("%d %d :: %d %d %d %d\n", i, j, ein(i, j), emid1(i, j), emid2(i, j), eout(i, j));
				if (bl[i][j])
					continue;
				add_edge(ein(i, j), emid1(i, j), 1);
				add_edge(emid1(i, j), emid2(i, j), 1);
				add_edge(emid2(i, j), eout(i, j), 1);
				for (int k = 0; k < 4; ++k)
				{
					int ni = i + dx[k];
					int nj = j + dy[k];
					if (ni < 0 || nj < 0 || ni >= h || nj >= h)
						continue;
					if (bl[ni][nj])
						continue;
					add_edge(eout(i, j), ein(ni, nj), 1);
				}
			}
		}
		//~ printf("SD %d %d %d\n", s, t, n);
		printf("Case #%d: %d\n", te, dinic());
	}
	return 0;
}
