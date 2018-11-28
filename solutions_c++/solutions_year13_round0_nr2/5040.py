# include <iostream>
using namespace std;
int map[105][105];
int n, m;
bool ok(int x, int y)
{
	int i, flag1=1, flag2=1;
	for (i = 1; i<=m; i++)
	{
		if (map[x][i]>map[x][y])
		{
			flag1=0;
			break;
		}
	}
	for (i = 1; i<=n; i++)
	{
		if (map[i][y]>map[x][y])
		{
			flag2=0;
			break;
		}
	}
	if (flag1||flag2)
		return true;
	else
		return false;
}
int main()
{
	int i, j, count, flag, N;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin>>N;
	count=1;
	while (N--)
	{
		flag=0;
		cin>>n>>m;
		for (i = 1; i<=n; i++)
		{
			for (j = 1; j<=m; j++)
				cin>>map[i][j];
		}
		for (i = 1; i<=n; i++)
		{
			for (j = 1; j<=m; j++)
			{
				if (ok(i, j))
					continue;
				else
				{
					flag=1;
					break;
				}
			}
			if (flag)break;
		}
		if (flag)
			printf("Case #%d: NO\n", count++);
		else
			printf("Case #%d: YES\n", count++);
	}
	return 0;
}