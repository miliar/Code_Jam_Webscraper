#include <iostream>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T, M, N;
int a[200][200];

int main()
{
	fscanf(f, "%d", &T);
	for (int t = 0; t < T; ++t)
	{
		fscanf(f, "%d %d", &N, &M);
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				fscanf(f, "%d", &a[i][j]);
			}
		}

		bool isSolution = true;
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				bool horizontal = false, vertical = false;
				for (int i1 = 0; i1 < N; ++i1)
				{
					if (a[i][j] < a[i1][j])
					{
						horizontal = true;
					}
				}
				for (int j1 = 0; j1 < M; ++j1)
				{
					if (a[i][j] < a[i][j1])
					{
						vertical = true;
					}
				}
				if (horizontal && vertical)
				{
					isSolution = false;
				}
			}
		}

		if (isSolution)
		{
			fprintf(g, "Case #%d: YES\n", t + 1);
		}
		else
		{
			fprintf(g, "Case #%d: NO\n", t + 1);
		}
	}


	return 0;
}