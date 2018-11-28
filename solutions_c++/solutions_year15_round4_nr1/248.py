#include <cstdio>
const int maxn = 105, fx[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int n, m, ans;
char map[maxn][maxn];
bool walk(int x, int y, int dx, int dy)
{
	for (; x >= 1 && x <= n && y >= 1 && y <= m; x += dx, y += dy)
		if (map[x][y] != '.')
			return 1;
	return 0;
}
bool check()
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (map[i][j] != '.')
			{
				int dx, dy;
				if (map[i][j] == '<')
				{
					dx = 0, dy = -1;
				}
				else if (map[i][j] == '>')
				{
					dx = 0, dy = 1;
				}
				else if (map[i][j] == '^')
				{
					dx = -1, dy = 0;
				}
				else
				{
					dx = 1, dy = 0;
				}
				if (walk(i + dx, j + dy, dx, dy))
					continue;
				else
				{
					bool ok = 0;
					for (int q = 0; q < 4; q++)
					{
						if (walk(i + fx[q][0], j + fx[q][1], fx[q][0], fx[q][1]))
						{
							ok = 1;
							break;
						}
					}
					if (!ok)
						return 0;
					ans++;
				}
			}
	return 1;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			scanf("%s", map[i] + 1);
		printf("Case #%d: ", tt);
		ans = 0;
		if (!check())
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}
