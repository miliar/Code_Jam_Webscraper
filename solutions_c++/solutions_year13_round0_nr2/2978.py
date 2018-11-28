#include <stdio.h>

#define MAX 128

int lawn[MAX][MAX];
int N, M;

bool check_row(int r, int c)
{
	int col = 0;
	for(col = 0; col < M; col++)
	{
		if(lawn[r][col] > lawn[r][c])
			return false;
	}
	return true;
}

bool check_col(int r, int c)
{
	int row = 0;
	for(row = 0; row < N; row++)
	{
		if(lawn[row][c] > lawn[r][c])
			return false;
	}
	return true;
}

bool judge()
{
	int r, c;
	for(r = 0; r < N; r++)
	{
		for(c = 0; c < M; c++)
		{
			if(!check_row(r, c) && !check_col(r, c))
				return false;
		}
	}
	return true;
}

int main()
{
	int T, t;
	int r, c;
	scanf("%d", &T);
	for(t = 0; t < T; t++)
	{
		scanf("%d %d", &N, &M);
		for(r = 0; r < N; r++)
			for(c = 0; c < M; c++)
				scanf("%d", &lawn[r][c]);
		printf("Case #%d: %s\n", t + 1, judge()?"YES":"NO");
	}

	return 0;
}