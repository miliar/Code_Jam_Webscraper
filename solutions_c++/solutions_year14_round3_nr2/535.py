#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
const int MAXN = 10, MAX_LENGTH = 100;
int n, used[MAXN], result, p[MAXN];
char s[MAXN][MAX_LENGTH + 1];
bool valid()
{
	int j, k, l;
	bool usedc[256] = { false };
	char current = s[p[0]][0];
	for (j = 0; j < n; j++)
	{
		l = strlen(s[p[j]]);
		for (k = 0; k < l; k++)
		{
			if (usedc[s[p[j]][k]] && s[p[j]][k] != current)
				return false;
			current = s[p[j]][k];
			usedc[current] = true;
		}
	}
	return true;
}
void solve(int pos)
{
	int i;
	if (pos == n)
	{
		if (valid())
			result++;
		/*for (i = 0; i < n; i++)
			printf("%d ", p[i]);
		printf("\n");*/
	}
	else
	{
		for (i = 0; i < n; i++)
		if (!used[i])
		{
			used[i] = true;
			p[pos] = i;
			solve(pos + 1);
			used[i] = false;
		}
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, j;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		result = 0;
		scanf("%d", &n);
		for (j = 0; j < n; j++)
			scanf("%s", s[j]);
		for (j = 0; j < n; j++)
			used[j] = false;
		solve(0);
		printf("Case #%d: %d\n", i, result);
	}
	return 0;
}