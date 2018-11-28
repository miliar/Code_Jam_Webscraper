#include <stdio.h>

bool sameVLevel(int** map, int c, int N, int M)
{
	int start = map[0][c];
	for(int i = 0; i < N; i += 1)
	{
		if (start != map[i][c]) return false;
	}
	return true;
}

bool sameHLevel(int** map, int r, int N, int M)
{
	int start = map[r][0];
	for(int i = 0; i < M; i += 1)
	{
		if (start != map[r][i]) return false;
	}
	return true;
}

int findMaxH(int **map, int r, int N, int M)
{
	int value = 0;
	for(int i = 0; i < M; i += 1)
	{
		if (value < map[r][i]) value = map[r][i];
	}
	return value;
}

void main(void)
{
	int T, N, M;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases += 1)
	{
		scanf("%d %d", &N, &M);
		int ** map = new int*[N];
		for(int i = 0; i < N; i += 1) map[i] = new int[M];

		for(int i = 0; i < N; i += 1)
		{
			for(int j = 0; j < M; j += 1)
			{
				scanf("%d", &map[i][j]);
			}
		}

		bool gotAnswer = false;
		for(int c = 0; c < M; c += 1)
		{
			if (!sameVLevel(map, c, N, M))
			{
				for(int r = 0; r < N; r += 1)
				{
					if (map[r][c] < findMaxH(map, r, N, M))
					{
						gotAnswer = true;
						printf("Case #%d: NO\n", cases);
						c = M+1;
						break;
					}
				}
			}
		}
		if (!gotAnswer)
		printf("Case #%d: YES\n", cases);
	}
}