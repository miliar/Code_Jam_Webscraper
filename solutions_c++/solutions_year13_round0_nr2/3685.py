#include <cstdio>

#define MAX 100

bool isPossible(int lawn[MAX][MAX], int N, int M)
{
		for (int i = 0; i < N; i++)
				for (int j = 0; j < M; j++)
				{
						int k;
						int target = lawn[i][j];
						for (k = 0; k < M; k++)
								if (lawn[i][k] > target)
										break;
						if (k == M)
								continue;

						for (k = 0; k < N; k++)
								if (lawn[k][j] > target)
										return false;
				}
		return true;
}


int main(int argc, char* argv[])
{
		int T;
		int lawn[MAX][MAX];
		int N, M;

		scanf("%d\n", &T);
		for (int t = 0; t < T; t++)
		{
				scanf("%d%d\n", &N, &M);
				for (int i = 0; i < N; i++)
						for (int j = 0; j < M; j++)
								scanf("%d", &lawn[i][j]);
				if(isPossible(lawn, N, M))
						printf("Case #%d: YES\n", t+1);
				else
						printf("Case #%d: NO\n", t+1);
		}

		return 0;
}


