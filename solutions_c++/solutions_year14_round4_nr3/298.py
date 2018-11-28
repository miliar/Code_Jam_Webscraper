//sap算法求最大流，src为源点，dst为汇点，点编号从0开始

#include <iostream>
#include <cstdio>
#include <cstring>
#define mem(a,b) memset(a,b,sizeof(a))
#define MAXV 120010
#define MAXE 3000000
#define INF 1000000000

using namespace std;

struct Edge
{
	int ed, flow, next;
} edge[MAXE];

int head[MAXV], nEdge;
int d[MAXV], pre[MAXV], path[MAXV], his[MAXV], cur[MAXV], vh[MAXV];

void init()
{
	memset(head, -1, sizeof(head));
	nEdge = 0;
}

void addEdge(const int a, const int b, const int flow)
{
//	cout<<a<<"  "<<b<<"  "<<flow<<endl;
	edge[nEdge].ed = b;
	edge[nEdge].flow = flow;
	edge[nEdge].next = head[a];
	head[a] = nEdge++;
	edge[nEdge].ed = a;
	edge[nEdge].flow = 0;
	edge[nEdge].next = head[b];
	head[b] = nEdge++;
}

int sap(const int v, const int src, const int dst)
{
	int x, y, i, m, nowFlow = INF, totalFlow = 0;
	bool flag;

	memset(d, 0, sizeof(d));
	memset(vh, 0, sizeof(vh));
	memcpy(cur, head, sizeof(cur));

	for (vh[0] = v, x = src; d[src] < v;)
	{
		his[x] = nowFlow;

		for (flag = false, i = cur[x]; ~i; i = edge[i].next)
		{
			if (edge[i].flow && d[x] == d[y = edge[i].ed] + 1)
			{
				flag = true;
				nowFlow = min(nowFlow, edge[i].flow);
				pre[y] = x;
				path[y] = cur[x] = i;

				if ((x = y) == dst)
				{
					for (totalFlow += nowFlow; x != src; x = pre[x])
					{
						edge[path[x]].flow -= nowFlow;
						edge[path[x] ^ 1].flow += nowFlow;
					}

					nowFlow = INF;
				}

				break;
			}
		}

		if (!flag)
		{
			for (m = v, i = cur[x] = head[x]; ~i; i = edge[i].next)
			{
				if (edge[i].flow && d[y = edge[i].ed] < m)
				{
					m = d[y];
					cur[x] = i;
				}
			}

			if (!(--vh[d[x]]))
			{
				break;
			}

			++vh[d[x] = m + 1];

			if (x != src)
			{
				nowFlow = his[x = pre[x]];
			}
		}
	}

	return totalFlow;
}

int a[600][600];
int id[600][600][3];

int main()
{
	int T;
	int i, j, cas = 0, n, m, b, x, y, xx, yy, k;
//
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> T;

	while (T--)
	{
		mem(a, 0);
		mem(id,0);
		scanf("%d%d%d", &m, &n, &b);

		for (k = 0; k < b; k++)
		{
			scanf("%d%d%d%d", &y, &x, &yy, &xx);

			for (i = x ; i <= xx; i++)
				for (j = y; j <= yy; j++)
				{
					a[i][j] = 1;
				}
		}
//
//		for (i = n - 1; i >= 0; i--)
//		{
//			for (j = 0; j < m; j++)
//			{
//				cout << a[i][j] << "  ";
//			}
//
//			cout << endl;
//		}

		init();
		int tot = 0;
		int s = 0, t = 2 * n * m + 1;

		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
			if (a[i][j] != 1)
			{
				id[i][j][0] = ++tot;
				id[i][j][1] = ++tot;
				addEdge(id[i][j][0], id[i][j][1], 1);
			}
//		cout<<tot<<endl;
		for (i = 0 ; i < m; i++)
			if (a[0][i] == 0)
			{
				addEdge(s, id[0][i][0], 1);
			}

		for (i = 0 ; i < m; i++)
			if (a[n - 1][i] == 0)
			{
				addEdge(id[n - 1][i][1], t, 1);
			}

		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
			{
				if (a[i][j])
				{
					continue;
				}

				if (i > 0 && a[i - 1][j] == 0)
				{
					addEdge(id[i][j][1], id[i - 1][j][0], 1);
				}

				if (i < n && a[i + 1][j] == 0)
				{
					addEdge(id[i][j][1], id[i + 1][j][0], 1);
				}

				if (j > 0 && a[i][j - 1] == 0)
				{
					addEdge(id[i][j][1], id[i][j - 1][0], 1);
				}

				if (j < m && a[i][j + 1] == 0)
				{
					addEdge(id[i][j][1], id[i][j + 1][0], 1);
				}
			}

		int ans = sap(t + 1, s , t);
		printf("Case #%d: %d\n", ++cas, ans);
	}

	return 0;
}
