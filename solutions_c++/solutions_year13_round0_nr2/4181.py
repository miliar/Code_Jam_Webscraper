#include <cstdio>

int n, m, fix[200][200], v[200][200];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int test = 0; test < t; test++)
	{
		printf("Case #%d: ", test + 1);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &v[i][j]);
				fix[i][j] = 0;
			}

		int prev = 0, cnt = 0, min;
		bool yes = true, check;

		while (cnt < n * m)
		{
			min = 101;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
					if (!fix[i][j] && v[i][j] < min)
						min = v[i][j];

			for (int i = 0; i < n; i++)
			{
				check = true;
				for (int j = 0; j < m; j++)
					if (!fix[i][j] && v[i][j] != min)
					{
						check = false;
						//break;
					}
				if (check)
					for (int j = 0; j < m; j++)
					{
						cnt += 1 - fix[i][j];
						fix[i][j] = 1;
					}
			}

			//if (!check)
			//{
				for (int i = 0; i < m; i++)
				{
					check = true;
					for (int j = 0; j < n; j++)
						if (!fix[j][i] && v[j][i] != min)
						{
							check = false;
						//	break;
						}
					if (check)
						for  (int j = 0; j < n; j++)
						{
							cnt += 1 - fix[j][i];
							fix[j][i] = 1;
						}
						
				}
			//}


			if (prev == cnt)
			{
				yes = false;
				break;
			}
			prev = cnt;			
		}

		if (yes)
			puts("YES");
		else
			puts("NO");
	}
}