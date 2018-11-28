#pragma warning(disable:4996)
#include<stdio.h>
char map[110][110];
int Cr[110];
int Cc[110];
void solve()
{
	int r, c;
	int i, j;
	int ans = 0;
	scanf("%d%d", &r, &c);
	for (i = 0; i < r; i++)scanf("%s", map[i]);
	for (i = 0; i < r; i++) Cr[i] = 0;
	for (j = 0; j < c; j++) Cc[j] = 0;
	for (i = 0; i < r; i++)for (j = 0; j < c; j++) if (map[i][j] != '.')
	{
		Cr[i] ++; Cc[j]++;
	}
	for (i = 0; i < r; i++)
	{
		for (j = 0; j < c; j++) if (map[i][j] != '.') break;
		if (j != c && map[i][j] == '<')
		{
			ans++;
			if (Cr[i] == 1 && Cc[j] == 1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
		for (j = c-1; j >= 0; j--) if (map[i][j] != '.') break;
		if (j != -1 && map[i][j] == '>')
		{
			ans++;
			if (Cr[i] == 1 && Cc[j] == 1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	for (j = 0; j < c; j++)
	{
		for (i = 0; i < r; i++) if (map[i][j] != '.') break;
		if (i != r && map[i][j] == '^')
		{
			ans++;
			if (Cr[i] == 1 && Cc[j] == 1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
		for (i = r-1; i >= 0; i--) if (map[i][j] != '.') break;
		if (i != -1 && map[i][j] == 'v')
		{
			ans++;
			if (Cr[i] == 1 && Cc[j] == 1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	printf("%d\n", ans);
	return ;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		solve();
	}
	return 0;
}