# include <stdio.h>
# include <algorithm>

using namespace std;

int v[15];
int test, e, r, n, best;
int kase = 0;

void dfs(int now, int nowe, int nowg)
{
	if (nowe <= 0) return;
	if (now == n)
	{
		best = max(best, nowg);
		return;
	}

	for (int i = 0; i <= nowe; i ++)
	{
		dfs(now + 1, min(e, nowe - i + r), nowg + i * v[now]);
	}
}

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);

	scanf("%d", &test);

	while (test --)
	{
		scanf("%d%d%d", &e, &r, &n);

		for (int i = 0; i < n; i ++)
		{
			scanf("%d", &v[i]);
		}

		best = 0;

		dfs(0, e, 0);

		printf("Case #%d: %d\n", ++kase, best);
	}
}