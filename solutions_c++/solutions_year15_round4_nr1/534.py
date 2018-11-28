#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 105
#define MYINF 1000000000

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static char data[MAXN][MAXN];
	char dirchar[4] = {'^', 'v', '<', '>'};
	int dirx[4] = {-1, 1, 0, 0};
	int diry[4] = {0, 0, -1, 1};
	for (iT = 0; iT < T; iT++)
	{
		int N, M;
		scanf("%d %d",&N,&M);
		int i, j, x, y;
		for (i = 0; i < N; i++)
		{
			scanf("\n%s",data[i]);
		}
		int res = 0;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				if (data[i][j] != '.')
				{
					char dirb[4];
					memset(dirb, 0, sizeof(dirb));
					for (int dir = 0; dir < 4; dir++)
					{
						x = i + dirx[dir];
						y = j + diry[dir];
						while ((x >= 0) && (x < N) && (y >= 0) && (y < M))
						{
							if (data[x][y] != '.')
							{
								dirb[dir] = 1;
								break;
							}
							x += dirx[dir];
							y += diry[dir];
						}
					}
					int dirorig = 0;
					while (dirchar[dirorig] != data[i][j]) dirorig++;
					if (dirb[dirorig] == 0)
					{
						int dirnew = 0;
						while ((dirnew < 4) && (dirb[dirnew] == 0)) dirnew++;
						if (dirnew == 4) res = MYINF;
						else res++;
					}
				}
			}
		}
		printf("Case #%d: ",iT+1);
		if (res >= MYINF) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
	return 0;
}
