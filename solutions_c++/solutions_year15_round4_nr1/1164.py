#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

char g[112][112];
int n, m;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int dc[4] = {'v', '^', '<', '>'};

pair<int,int> go(pair<int,int> a, int i)
{
	a.first += dx[i], a.second += dy[i];

	while(g[a.first][a.second] == '.' && g[a.first][a.second] != 0)
		a.first += dx[i], a.second += dy[i];
	if(g[a.first][a.second] == 0)
		return pair<int,int> (-1, -1);
	else
		return a;
}

int
main(void)
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		bool possible = true;
		int ans = 0;
		memset(g, 0, sizeof(g));
		scanf("%d %d", &n, &m);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				scanf(" %c", &g[i][j]);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
			{
				if(g[i][j] != '.')
				{
					bool ok = false;
					for(int k = 0; k < 4; k++)
					{
						pair<int,int> b = go(pair<int,int> (i, j), k);
						if(b != pair<int,int> (-1,-1))
							ok = true;
						if(g[i][j] == dc[k] && b == pair<int,int> (-1,-1))
							ans++;
					}
					possible = (possible && ok);
				}
			}
		printf("Case #%d: ", t);
		if(possible)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
}
