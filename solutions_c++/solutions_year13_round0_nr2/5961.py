#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#define Mset(x, y) memset(x, y, sizeof(x))
#define MAX 110
using namespace std;

struct data
{
	int x, y, v;
};

int g[MAX][MAX], f[MAX][MAX];
int n, m, sz;
vector <data> edge;

inline bool cmp(const data &A, const data &B)
{
	if (A.v < B.v) return true;
	return false;
}

int main()
{
	int TestCase;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &TestCase);
	for (int T = 1; T <= TestCase; ++T)
	{
		bool ans = 1;
		Mset(f, 0); Mset(g, 0);
		edge.clear();
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
			{
				scanf("%d", &g[i][j]);
				data get;
				get.x = i; 
				get.y = j;
				get.v = g[i][j];
				edge.push_back(get);
			}
		sort(edge.begin(), edge.end(), cmp);
		sz = edge.size();
		for (int i = 0; i < sz; ++i)
		{
			bool Ltmp = 1, Rtmp =1;
			int X = edge[i].x;
			int Y = edge[i].y;
			for (int i = 1; i <= n; ++i)
				if (g[X][Y] < g[X][i]) Ltmp = 0;
			for (int i = 1; i <= m; ++i)
				if (g[X][Y] < g[i][Y]) Rtmp = 0;
			if (!(Ltmp || Rtmp))
			{
				ans = 0;
				break;
			}
		}
		//printf("%d %d\n",n,m);
		if (ans) printf("Case #%d: YES\n",T);
		else printf("Case #%d: NO\n",T);
	}
	return 0;
}

