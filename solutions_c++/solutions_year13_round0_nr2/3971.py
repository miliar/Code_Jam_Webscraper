# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;

int a[105][105];
int test, n, m;
int kase = 0;

# define oo 1000

bool checkRow(int r, int c)
{
	int x = a[r][c];

	for (int i = 0; i < m; i ++)
	{
		if (a[r][i] != x && a[r][i] != oo) return false;
	}

	return true;
}

bool checkCol(int r, int c)
{
	int x = a[r][c];

	for (int i = 0; i < n; i ++)
	{
		if (a[i][c] != x && a[i][c] != oo) return false;
	}

	return true;
}

int check(int r, int c)
{
	if (checkRow(r, c)) return 1;
	if (checkCol(r, c)) return 2;

	return 0;
}

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);
	scanf("%d", &test);

	while (test --)
	{
		int err = 0;

		scanf("%d%d", &n, &m);

		printf("Case #%d: ", ++ kase);

		for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
				scanf("%d", &a[i][j]);

		bool finish = false;

		while (true)
		{
			int x = oo;
			int si, sj;

			for (int i = 0; i < n; i ++)
			{
				for (int j = 0; j < m; j ++)
				{
					if (a[i][j] < x)
					{
						x = a[i][j];
						si = i;
						sj = j;
					}
					// printf("%4d ", a[i][j]);
				}

				// printf("\n");
			}

			if (x == oo) break;

			int t = check(si, sj);

			if (!t)
			{
				err = 1;
				break;
			} else
			{
				if (t == 1)
				{
					for (int i = 0; i < m; i ++)
					{
						a[si][i] = oo;
					}
				}

				if (t == 2)
				{
					for (int i = 0; i < n; i ++)
					{
						a[i][sj] = oo;
					}
				}
			}
		}

		if (err) printf("NO\n"); else printf("YES\n");
	}
}