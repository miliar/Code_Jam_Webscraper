#include "stdio.h"
#include "string.h"
#include "math.h"

#define debug(...) 
//#define debug(...) printf("[debug]");printf(__VA_ARGS__);

int main()
{
	int a[128][128];
	int max_row[128], max_col[128];
	int T, N, M;
	int c, i, j;
	scanf("%d\n", &T);
	
	for (c = 1; c <= T; ++c)
	{
		scanf("%d %d\n", &N, &M);

		for (i = 0; i < N; ++i)
		{
			for (j = 0 ; j < M; ++j)
			{
				scanf("%d\n", &(a[i][j]));
			}
		}

		for (i = 0; i < N; ++i)
		{
			max_row[i] = 0;
			for (j = 0 ; j < M; ++j)
				if (a[i][j] > max_row[i])
					max_row[i] = a[i][j];
		}

		for (j = 0; j < M; ++j)
		{
			max_col[j] = 0;
			for (i = 0 ; i < N; ++i)
				if (a[i][j] > max_col[j])
					max_col[j] = a[i][j];
		}

		bool possible = true;
		for (i = 0; i < N && possible; ++i)
		{
			for (j = 0 ; j < M && possible; ++j)
			{
				if (!(a[i][j] >= max_row[i] || a[i][j] >= max_col[j]))
					possible = false;
			}
		}
		if (possible)
			printf("Case #%d: YES\n", c);
		else
			printf("Case #%d: NO\n", c);
	}
	return 0;
}
