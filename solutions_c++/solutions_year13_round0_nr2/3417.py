#define maxn 100
#define maxm 100

#include <stdio.h>

int a[maxn][maxm], rows[maxn], cols[maxm];

inline int max(int a, int b)
{
	return a > b ? a : b;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int test = 0; test < t; test++)
	{
		int n, m;
		scanf("%d%d", &n, &m);

		for (int i = 0; i < n; i++)
			rows[i] = -1;
		for (int j = 0; j < m; j++)
			cols[j] = -1;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{				
				scanf("%d", &a[i][j]);
				rows[i] = max(rows[i], a[i][j]);
				cols[j] = max(cols[j], a[i][j]);
			}

		bool b = true;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j] < rows[i] && a[i][j] < cols[j])
					b = false;

		printf("Case #%d: %s\n", test + 1, b ? "YES" : "NO");
	}

	return 0;
}