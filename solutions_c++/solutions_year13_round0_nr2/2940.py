#include <cstdio>
int T;
int d[101][101];
int r[101][101];
int c[101][101];
int main()
{
	int t, i, j, N, M, temp;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{	
		scanf("%d %d", &N, &M);
		for (i = 0; i < N; i++)
		{
			temp = -1;
			for (j = 0; j < M; j++)
			{
				scanf("%d", &d[i][j]);
				if (temp < d[i][j]) temp = d[i][j];
			}
			for (j = 0; j < M; j++) 
			{
				if (temp == d[i][j]) r[i][j] = 1;
				else r[i][j] = 0;
			}
		}
		for (i = 0; i < M; i++)
		{
			temp = -1;
			for (j = 0; j < N; j++)
			{
				if (temp < d[j][i]) temp = d[j][i];
			}
			for (j = 0; j < N; j++)
			{
				if (temp == d[j][i]) c[j][i] = 1;
				else c[j][i] = 0;
			}
		}
		bool re = false;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				if (c[i][j] + r[i][j] == 0) 
				{
					re = true;
					break;
				}
			}
			if (re) break;
		}
		printf("Case #%d: ", t);
		if (re) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
