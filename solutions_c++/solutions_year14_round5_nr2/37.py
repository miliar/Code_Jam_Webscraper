#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 105
#define MAXSHOTS 1005

using namespace std;

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int P, Q, N;
		scanf("%d %d %d",&P,&Q,&N);
		static int H[MAXN];
		static int G[MAXN];
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("%d %d",&(H[i]),&(G[i]));
		}
		static int a[MAXN][MAXSHOTS][2];
		int j, f;
		for (i = 0; i <= N; i++)
		{
			for (j = 0; j < MAXSHOTS; j++)
			{
				for (f = 0; f < 2; f++)
				{
					a[i][j][f] = -1;
				}
			}
		}
		a[0][0][0] = 0;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < MAXSHOTS; j++)
			{
				for (f = 0; f < 2; f++)
				{
					if (a[i][j][f] != -1)
					{
						//printf("a[%d][%d][%d] = %d\n",i,j,f,a[i][j][f]);
						//Can shoot it down immediately without tower taking a chance
						int need = (H[i] + P - 1) / P;
						if (need <= j)
						{
							if ((a[i][j][f] + G[i]) > a[i+1][j-need][f]) a[i+1][j-need][f] = a[i][j][f] + G[i];
						}
						//Otherwise we will take turns
						int h = H[i];
						if (f) h -= Q;
						if (h <= 0)
						{
							if (a[i][j][f] > a[i+1][j][0]) a[i+1][j][0] = a[i][j][f];
						}
						else
						{
							//Give up
							int nj = j + (h + Q - 1) / Q;
							if (a[i][j][f] > a[i+1][nj][0]) a[i+1][nj][0] = a[i][j][f];
							//Shoot it down
							int immediate;
							for (immediate = 0; immediate <= j; immediate++)
							{
								int rem = h - immediate * P;
								if (rem <= 0) break;
								int saved = (rem + Q - 1) / Q;
								while (saved >= 0)
								{
									int rem2 = rem - saved * Q;
									if (rem2 > 0)
									{
										int remmod = rem2 % (P + Q);
										if ((remmod >= 1) && (remmod <= P))
										{
											nj = j - immediate + saved;
											if ((a[i][j][f] + G[i]) > a[i+1][nj][1]) a[i+1][nj][1] = a[i][j][f] + G[i];
											break;
										}
									}
									saved--;
								}
							}
						}
					}
				}
			}
		}
		i = N;
		int res = -1;
		for (j = 0; j < MAXSHOTS; j++)
		{
			for (f = 0; f < 2; f++)
			{
				if (a[i][j][f] > res) res = a[i][j][f];
			}
		}
		printf("Case #%d: %d\n",iT+1,res);
	}
	return 0;
}
