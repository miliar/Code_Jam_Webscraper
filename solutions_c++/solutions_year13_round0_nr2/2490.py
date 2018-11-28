#include <cstdio>
#include <cstring>

const int maxn = 105;

int map[maxn][maxn], n, m;

bool col(int x, int y)
{
	int temp = map[x][y];
	for(int i = x; i > 0; i--)
		if(map[i][y] > temp)
			return false;
	for(int i = x; i <= n; i++)
		if(map[i][y] > temp)
			return false;
	return true;
}

bool row(int x, int y)
{
	int temp = map[x][y];
	for(int j = y; j > 0; j--)
		if(map[x][j] > temp)
			return false;
	for(int j = y; j <= m; j++)
		if(map[x][j] > temp)
			return false;
	return true;
}

int main()
{
	freopen("d://test/B-Large.in", "r", stdin);
	freopen("d://test/B-Large.out", "w", stdout);
	bool flag;
	int t, cnt = 0;
	
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d %d", &n, &m);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				scanf("%d", &map[i][j]);
		flag = true;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				if(!col(i, j) && !row(i, j))
				{
					flag = false;
					goto z;
				}
z:		if(flag)
			printf("Case #%d: YES\n", ++cnt);
		else
			printf("Case #%d: NO\n", ++cnt);
	}
	return 0;
}