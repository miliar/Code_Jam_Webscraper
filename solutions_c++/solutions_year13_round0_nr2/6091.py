#include <cstdio>
using namespace std;

int main()
{
	int T, t;
	int n, m;
	int l[101][101];
	int rl[101][101];
	int c;
	bool p;
	int i, j;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d %d", &n, &m);
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j <= m; j++)
			{
				scanf("%d", &l[i][j]);
			}
		}
		for (i = 1; i <= n; i++)
		{
			c = l[i][1];
			for (j = 2; j <= m; j++)
			{
				if (l[i][j] > c)
				{
					c = l[i][j];
				}
			}
			for (j = 1; j <= m; j++)
			{
				rl[i][j] = c;
			}
		}
		for (j = 1; j <= m; j++)
		{
			c = l[1][j];
			for (i = 2; i <= n; i++)
			{
				if (l[i][j] > c)
				{
					c = l[i][j];
				}
			}
			for (i = 1; i <= n; i++)
			{
				if (rl[i][j] > c)
				{
					rl[i][j] = c;
				}
			}
		}
		p = true;
		for (i = 0; p && i <= n; i++)
		{
			for (j = 0; p && j <= m; j++)
			{
				p = (l[i][j] == rl[i][j]);
			}
		}
		printf("Case #%d", t);
		if (p)
		{
			puts(": YES");
		}
		else
		{
			puts(": NO");
		}
	}
}