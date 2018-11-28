#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std; 

const int Dx[] = {-1, 1, 0, 0};
const int Dy[] = {0, 0, -1, 1};

int N, M;
char Map[120][120];
int isDanger[120][120][4];

int Work()
{
	int Ans = 0;
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i ++)
		scanf("%s", &Map[i]);
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < M; j ++)
			if (Map[i][j] != '.')
			{
				int OK[4];
				for (int k = 0; k < 4; k ++)
				{
					OK[k] = 0;
					int x = i, y = j;
					for (int l = 1; ; l ++)
					{
						x += Dx[k];
						y += Dy[k];
						if (x < 0 || y < 0 || x >= N || y >= M)
							break;
						if (Map[x][y] != '.')
							OK[k] = 1;
					}
				}
				if (OK[0] + OK[1] + OK[2] + OK[3] == 0)
					return -1;
				if (Map[i][j] == '^' && OK[0] == 0) Ans ++;
				if (Map[i][j] == 'v' && OK[1] == 0) Ans ++;
				if (Map[i][j] == '<' && OK[2] == 0) Ans ++;
				if (Map[i][j] == '>' && OK[3] == 0) Ans ++;
			}
	return Ans;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		int A = Work();
		if (A == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", A);
	}
	return 0;
}
