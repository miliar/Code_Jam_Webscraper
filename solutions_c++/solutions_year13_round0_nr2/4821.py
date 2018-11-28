#include <stdio.h>
#include <algorithm>

using namespace std;
#define minmax joltcola

int minmax[2][2][100];
int map[100][100];

int main()
{
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++)
	{
		for (int a = 0; a < 2; a++)
		{			
			for (int k = 0; k < 100; k++)
			{
				minmax[a][0][k] = 100;
				minmax[a][1][k] = 0;				
			}
		}

		int N, M;
		scanf("%d %d", &N, &M);
		int newmap[100][100];
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < M; x++)
			{
				scanf("%d", &map[y][x]);
				int values[2] = {y, x};
				for (int t = 0; t < 2; t++)
				{
					minmax[t][0][values[t]] = min(minmax[t][0][values[t]], map[y][x]);
					minmax[t][1][values[t]] = max(minmax[t][1][values[t]], map[y][x]);
				}

				newmap[y][x] = 100;
			}
		}
		
		int outerloopsteps[2] = {N, M};
		int innerloopsteps[2] = {M, N};
		int iy[2] = {1,0};
		int dy[2] = {0,1};

		int ix[2] = {0,1};				
		int dx[2] = {1,0};

		for (int a = 0; a < 2; a++)
		{
			for (int index = 0; index < outerloopsteps[a]; index++)
			{
				int setval = max(minmax[a][0][index], minmax[a][1][index]);
				int y = index * iy[a];
				int x = index * ix[a];

				for (int subindex = 0; subindex < innerloopsteps[a]; subindex++, x += dx[a], y += dy[a])
				{
					newmap[y][x] = min(newmap[y][x], setval);
				}
			}
		}

		bool ok = true;
		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < M; x++)
			{
				ok &= (map[y][x] == newmap[y][x]);
			}
		}

		printf("Case #%d: %s\n", test + 1, ok ? "YES" : "NO");
	}


}