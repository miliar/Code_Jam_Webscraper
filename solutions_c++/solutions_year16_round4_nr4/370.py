#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[5][5],b[5][5],v[10],used[10];
int n,ans;
char s1[10];

bool Dfs(int x)
{
	if (x > n)
	{
		return 1;
	}
	int flag = 1, ouc = 0;
	for (int i = 1; i <= n; i ++)
		if (!used[i] && b[v[x]][i])
		{
			ouc = 1;
			used[i] = 1;
			flag &= Dfs(x + 1);
			if (!flag) return 0;
			used[i] = 0;
		}
	return 1 && ouc;
}

bool Chk()
{
	for (int i = 1; i <= n; i ++) v[i] = i;
	while (1)
	{
		memset(used, 0, sizeof used);
		if (!Dfs(1)) return 0;
		if (!next_permutation(v + 1, v + n + 1)) break;
	}
	return 1;
}

int main()
{
//	freopen("data.in", "r", stdin);
//	freopen("data.out", "w", stdout);

	int CT; scanf("%d", &CT);

	for (int pt = 1; pt <= CT; pt ++)
	{
		printf("Case #%d: ", pt);
		scanf("%d", &n);

		for (int i = 1; i <= n; i ++)
		{
			scanf(" %s", s1 + 1);
			for (int j = 1; j <= n; j ++)
				a[i][j] = s1[j] - '0';
		}

		ans = -1;
		int m = n * n;
		for (int st = 0, lim = 1 << m; st < lim; st ++)
		{
			for (int i = 1; i <= n; i ++)
				for (int j = 1; j <= n; j ++) b[i][j] = (st & (1 << (i*n-n+j-1))) > 0;

			int cost = 0;
			int flag = 1;
			for (int i = 1; i <= n && flag; i ++)
				for (int j = 1; j <= n; j ++)
				{
					if (a[i][j] && !b[i][j]) { flag = 0; break; }
					if (!a[i][j] && b[i][j]) cost ++;
				}
			if (!flag) continue;
			if (ans != -1 && cost > ans) continue;
			if (Chk()) ans = cost;
		}
		printf("%d", ans);
		puts("");
	}
	return 0;
}



