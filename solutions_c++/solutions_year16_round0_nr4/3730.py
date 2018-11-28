// ProblemD.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	int T;
	int K;
	int C;
	int S;
	int minTiles;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d%d", &K, &C, &S);
		minTiles = K - C + 1;
		if (minTiles <= 0)
			minTiles = 1;

		printf("Case #%d: ", i + 1);
		if (minTiles <= S)
		{
			long long int startTile = 1;
			long long int endTile = K;
			int nTiles = K;
			for (int j = 1; j < C; j++)
			{
				if (--nTiles <= 0)
					nTiles = 1;
				endTile = startTile * K;
				startTile = endTile - nTiles + 1;
			}
			for (long long int k = startTile; k <= endTile; k++)
				printf("%lld ", k);
			printf("\n");
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}

    return 0;
}

