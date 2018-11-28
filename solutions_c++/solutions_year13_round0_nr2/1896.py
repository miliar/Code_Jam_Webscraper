#include <cstdio>

#define MAX(a, b) (a > b ? a : b)

int main()
{
	int t, test, N, M, i, j, v;
	int tab[100][100], tab2[100][100], l1[100], l2[100];
	bool b;

	scanf("%d", &t);
	for (test = 1; test <= t; test++)
	{
		scanf("%d", &N);
		scanf("%d", &M);

		for (i = 0; i < 100; i++)
		{
			l1[i] = l2[i] = 0;
		}

		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				scanf("%d", &tab[i][j]);
				
				if (l1[i] < tab[i][j])
				{
					l1[i] = tab[i][j];
				}
				if (l2[j] < tab[i][j])
				{
					l2[j] = tab[i][j];
				}

				//printf("%d ", tab[i][j]);
			}
			//printf("\n");
		}

		for (i = 0; i < N; i++)
		{
			//if (tab[i][0] == l1[i])
			{
				v = MAX(l1[i], tab[i][0]);
				for (j = 0; j < M; j++)
				{
					tab2[i][j] = l1[i];
				}
			}
		}
		for (i = 0; i < M; i++)
		{
			//if (tab[0][i] == l2[i])
			{
				v = MAX(tab[0][i], l2[i]);
				for (j = 0; j < N; j++)
				{
					if (tab2[j][i] > v)
					{
						tab2[j][i] = v;
					}
				}
			}
		}

		for (i = 0, b = true; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				if (tab[i][j] != tab2[i][j])
				{
					b = false;
				}
			}
		}

		printf("Case #%d: %s\n", test, b ? "YES" : "NO");
	}

	return 0;
}
