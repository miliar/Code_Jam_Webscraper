#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdlib>

using namespace std;

const int SZ = 105;

int N, M;
int lawn[SZ][SZ];
int rmin[SZ], rmax[SZ];
int cmin[SZ], cmax[SZ];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, t;
	int i, j;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d%d", &N, &M);
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				scanf("%d", &lawn[i][j]);
			}
		}
		for (i = 0; i < N; i++)
		{
			rmin[i] = lawn[i][0];
			rmax[i] = lawn[i][0];
			for (j = 1; j < M; j++)
			{
				if (rmin[i] > lawn[i][j])
					rmin[i] = lawn[i][j];
				if (rmax[i] < lawn[i][j])
					rmax[i] = lawn[i][j];
			}
		}
		for (j = 0; j < M; j++)
		{
			cmin[j] = lawn[0][j];
			cmax[j] = lawn[0][j];
			for (i = 1; i < N; i++)
			{
				if (cmin[j] > lawn[i][j])
					cmin[j] = lawn[i][j];
				if (cmax[j] < lawn[i][j])
					cmax[j] = lawn[i][j];
			}
		}
		char impos = 0;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				if (lawn[i][j] < rmax[i] && lawn[i][j] < cmax[j])
				{
					impos = 1;
					break;
				}
			}
		}
		if (impos)
			printf("NO\n");
		else
			printf("YES\n");
	}
	
	return 0;
}