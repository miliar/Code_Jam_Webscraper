#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 100 + 5
#define MAXV 10000 + 5
#define INF 1e9
#define eps 1e-9
int n, m;
int maze[MAXN][MAXN];
int isRowMax(int x, int y)
{
	int maxV = maze[x][y];
	for(int i = 1; i <= m; i++)
	{
		if(maze[x][i] > maxV)
			return 0;
	}
	return 1;
}
int isColMax(int x, int y)
{
	int maxV = maze[x][y];
	for(int i = 1; i <= m; i++)
	{
		if(maze[i][y] > maxV)
			return 0;
	}
	return 1;
}
int solve()
{
	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= m; j++)
		{
			if(!isRowMax(i, j) && !isColMax(i, j))
				return 0;
		}
	}
	return 1;
}
int main()
{
#ifdef LOCAL
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for(int ncas = 1; ncas <= T; ncas++)
	{
		memset(maze, 0, sizeof(maze));
		scanf("%d%d", &n, &m);
		printf("Case #%d: ", ncas);
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= m; j++)
			{
				scanf("%d", &maze[i][j]);
			}
		}
		if(solve())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}