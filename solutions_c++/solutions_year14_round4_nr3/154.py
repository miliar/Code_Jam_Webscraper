#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;


const int maxn = 1e3 + 100;
const int inf = 1005;

vector <pair<int, int> > g[maxn * maxn];
int dist[maxn];

priority_queue <pair<int, int> > qu;
int x[2][maxn], y[2][maxn];
	
void addEdge(int a, int b, int d)
{
	g[a].push_back(make_pair(b, d) );
	g[b].push_back(make_pair(a, d) );
}

int w, h, n;

int getSt()
{
	return n;
}
int getFin()
{
	return n + 1;
}

bool hasInt(int a, int b, int c, int d)
{
	return (min(b, d) >= max(a, c) );
}

int getDist(int a, int b)
{
	int ans = inf;
	for (int i1 = 0; i1 < 2; i1++)
	for (int i2 = 0; i2 < 2; i2++)
	for (int i3 = 0; i3 < 2; i3++)
	for (int i4 = 0; i4 < 2; i4++)
		ans = min(ans, max(abs(x[i1][a] - x[i2][b] ), abs(y[i3][a] - y[i4][b] ) ) );
	if (hasInt(x[0][a], x[1][a], x[0][b], x[1][b] ) )
		for (int i1 = 0; i1 < 2; i1++)
		for (int i2 = 0; i2 < 2; i2++)
			ans = min(ans, abs(y[i1][a] - y[i2][b] ) );
	if (hasInt(y[0][a], y[1][a], y[0][b], y[1][b] ) )
		for (int i1 = 0; i1 < 2; i1++)
		for (int i2 = 0; i2 < 2; i2++)
			ans = min(ans, abs(x[i1][a] - x[i2][b] ) );
	return ans;
}

void solve()
{

	scanf("%d%d%d", &w, &h, &n);
	

	int ysz = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d%d", &x[0][i], &y[0][i] );
		scanf("%d%d", &x[1][i], &y[1][i] );
		x[1][i]++;
		y[1][i]++;
	}
	int st = getSt();
	int fin = getFin();

	x[0][n] = x[1][n] = 0;
	y[0][n] = 0;
	y[1][n] = h - 1;
	
	x[0][n + 1] = x[1][n + 1] = w;
	y[0][n + 1] = 0;
	y[1][n + 1] = h - 1;


	for (int i = 0; i <= n + 1; i++)
		for (int j = i + 1; j <= n + 1; j++)
			addEdge(i, j, getDist(i, j) );
	

	memset(dist, -1, sizeof dist);
	dist[st] = 0;
	qu.push(make_pair(0, st) );
	
	fprintf(stderr, "bfs is here\n");

	while (qu.size() )
	{
		pair <int, int> p = qu.top();
		qu.pop();

		int v = p.second;
		int cd = -p.first;
		if (cd != dist[v] )
			continue;
		//fprintf(stderr, "l = %d, r = %d, v = %d, dist = %d\n", l, r, v, cd);
		for (int i = 0; i < g[v].size(); i++)
		{
			int nv = g[v][i].first;
			int nd = cd + g[v][i].second;
			if (dist[nv] == -1 || dist[nv] > nd)
			{
				dist[nv] = nd;
				qu.push(make_pair(-nd, nv) );
			}
		}
	}
	printf("%d", dist[fin] );

	for (int i = 0; i <= fin; i++)
		g[i].clear();
}


int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		fprintf(stderr, "Case #%d: ", i);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}