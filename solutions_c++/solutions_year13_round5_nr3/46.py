#include <iostream>
#include <queue>
#include <vector>
using namespace std;


struct Edge
{
	int from, to, a, b, ID;
	Edge(int from, int to, int a, int b, int ID) : from(from), to(to), a(a), b(b), ID(ID) {}
	Edge() : to(), a(), b(), ID(), from() {}
};

vector <Edge> q[2005];
vector <Edge> qf[2005];
vector <Edge> all;

int way[2005];

priority_queue <pair<long long, int> > qu;

long long dpbad[2005];
long long dpgood[2005];
long long dpfrom[2005];
const long long inf = 1e17;
bool used[2005];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int n, m, p;
		scanf("%d%d%d", &n, &m, &p);
		
		all.clear();
		all.push_back(Edge() );
		for (int i = 0; i <= n; i++)
		{
			q[i].clear();
			qf[i].clear();
		}
		for (int i = 0; i < m; i++)
		{
			int u, v, a, b;
			scanf("%d%d%d%d", &u, &v, &a, &b);
			Edge cur = Edge(u, v, a, b, i + 1);
			qf[u].push_back(cur);
			all.push_back(cur);
			swap(cur.from, cur.to);
			q[v].push_back(cur);
		}
		for (int i = 0; i < p; i++)
		{
			scanf("%d", &way[i] );
		}

		for (int i = 1; i <= n; i++)
		{
			used[i] = false;
			dpbad[i] = inf;
		}
		dpbad[2] = 0;
		qu.push(make_pair(0, 2) );
		while (qu.size() )
		{
			int curv = qu.top().second;
			long long curd = -qu.top().first;
			qu.pop();
			if (used[curv] )
				continue;
			used[curv] = true;
			for (int i = 0; i < q[curv].size(); i++)
			{
				long long nd = curd + q[curv][i].b;
				int nv = q[curv][i].to;
				if (nd < dpbad[nv] )
				{
					dpbad[nv] = nd;
					qu.push(make_pair(-nd, nv) );
				}
			}
		}



		for (int i = 1; i <= n; i++)
		{
			used[i] = false;
			dpfrom[i] = inf;
		}
		dpfrom[1] = 0;
		qu.push(make_pair(0, 1) );
		while (qu.size() )
		{
			int curv = qu.top().second;
			long long curd = -qu.top().first;
			qu.pop();
			if (used[curv] )
				continue;
			used[curv] = true;
			for (int i = 0; i < qf[curv].size(); i++)
			{
				long long nd = curd + qf[curv][i].b;
				int nv = qf[curv][i].to;
				if (nd < dpfrom[nv] )
				{
					dpfrom[nv] = nd;
					qu.push(make_pair(-nd, nv) );
				}
			}
		}




		for (int i = 1; i <= n; i++)
		{
			used[i] = false;
			dpgood[i] = inf;
		}
		dpgood[2] = 0;
		qu.push(make_pair(0, 2) );
		while (qu.size() )
		{
			int curv = qu.top().second;
			long long curd = -qu.top().first;
			qu.pop();
			if (used[curv] )
				continue;
			used[curv] = true;
			for (int i = 0; i < q[curv].size(); i++)
			{
				long long nd = curd + q[curv][i].a;
				int nv = q[curv][i].to;
				if (nd < dpgood[nv] )
				{
					dpgood[nv] = nd;
					qu.push(make_pair(-nd, nv) );
				}
			}
		}


		long long curD = 0;
		int ans = 0;
		for (int i = 0; i < p && ans == 0; i++)
		{
			Edge cur = all[way[i] ];
			int curv = cur.from;
			int nv = cur.to;
			long long nextCD = cur.a + dpgood[nv];
			curD += cur.a;
			if (curD > dpfrom[nv] )
			{
				ans = cur.ID;
				break;
			}
			if (dpbad[curv] < nextCD)
			{
				ans = cur.ID;
				break;
			}
			if (curD + nextCD - cur.a > dpbad[1] )
			{
				ans = cur.ID;
				break;
			}
			
		}
		printf("Case #%d: ", t);
		if (ans == 0)
			printf("Looks Good To Me\n");
		else
			printf("%d\n", ans);
	}




	return 0;
}