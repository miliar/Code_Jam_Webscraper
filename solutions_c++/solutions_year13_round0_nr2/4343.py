#include <stdio.h>

int a[110][110];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				scanf("%d", a[i] + j);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				int k;
				for (k = 0; k < m; ++k)
					if (a[i][j] < a[i][k])
						break;
				if (k == m)
					continue;
				for (k = 0; k < n; ++k)
					if (a[i][j] < a[k][j])
					{
						printf("NO\n");
						goto end;
					}
			}
		printf("YES\n");
end:;
	}
	return 0;
}
