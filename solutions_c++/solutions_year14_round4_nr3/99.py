#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1010;

int x0[N], y0[N], x1[N], y1[N];

int len[N][N];
long long dist[N]; bool sch[N];

long long dijkstra (int S, int T)
{
	memset(dist, -1, sizeof dist);
	memset(sch, 0, sizeof sch);
	dist[S] = 0;
	for (int i = 1; i <= T; i++)
	{
		int tmin = -1;
		for (int j = 0; j <= T; j++) if (!sch[j] && dist[j] != -1)
		{
			if (tmin == -1 || dist[j] < dist[tmin]) tmin = j;
		}
		sch[tmin] = true;
		for (int j = 0; j <= T; j++) if (!sch[j])
		{
			if (dist[j] == -1 || dist[j] > dist[tmin] + len[tmin][j])
			{
				dist[j] = dist[tmin] + len[tmin][j];
			}
		}
	}
	return dist[T];
}

int calDist (int a, int b)
{
	int res = 0;
	res = max(res, x0[b] - x1[a] - 1); 
	res = max(res, x0[a] - x1[b] - 1);
	res = max(res, y0[b] - y1[a] - 1);
	res = max(res, y0[a] - y1[b] - 1);
	return res;
}

int main ()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout); 
	int T; scanf("%d", &T);
	for (int kase = 1; kase <= T; kase++)
	{
		int w, h, b; scanf("%d %d %d", &w, &h, &b);
		for (int i = 1; i <= b; i++)
		{
			scanf("%d %d %d %d", &x0[i], &y0[i], &x1[i], &y1[i]);
			if (x0[i] > x1[i]) swap(x0[i], x1[i]);
			if (y0[i] > y1[i]) swap(y0[i], y1[i]);
		}
		int S = 0, T = b + 1;
		x0[S] = -1, x1[S] = -1, y0[S] = -1, y1[S] = h;
		x0[T] = w, x1[T] = w, y0[T] = -1, y1[T] = h;
		for (int i = S; i <= T; i++)
			for (int j = S; j <= T; j++)
			{
				if (i == j) len[i][j] = 0;
				else len[i][j] = calDist(i, j);
			}
		printf("Case #%d: %lld\n", kase, dijkstra(S, T));
	}
	return 0;
}
