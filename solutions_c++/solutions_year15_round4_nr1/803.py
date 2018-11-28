#include <bits/stdc++.h>
using namespace std;

char x[128][128];
int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};
int pos[256];
int r, c;
int T;

bool checkpoint(int a, int b, int p)
{
	a += dr[p], b += dc[p];
	while (a >= 0 && a < r && b >= 0 && b < c)
	{
		if (x[a][b] != '.')
			return true;
		a += dr[p], b += dc[p];
	}
	return false;
}

int main()
{
	pos['^'] = 0, pos['>'] = 1, pos['v'] = 2, pos['<'] = 3;
	scanf("%d", &T);
	for (int _ = 1;_ <= T;_++)
	{
		scanf("%d%d", &r, &c);
		for (int i = 0;i < r;i++)
			scanf("%s", x[i]);
		printf("Case #%d: ", _);
		int ans = 0;
		for (int i = 0;i < r;i++)
		{
			for (int j = 0;j < c;j++) if (x[i][j] != '.')
			{
				if (checkpoint(i, j, pos[x[i][j]]))
					continue;
				bool ok = false;
				for (int k = 0;k < 4;k++)
				{
					if (checkpoint(i, j, k))
					{
						ok = true;
						break;
					}
				}
				if (ok)
					ans++;
				else
				{
					ans = -1;
					printf("IMPOSSIBLE\n");
					break;
				}
			}
			if (ans == -1)
				break;
		}
		if (ans != -1)
			printf("%d\n", ans);
	}
	return 0;
}
