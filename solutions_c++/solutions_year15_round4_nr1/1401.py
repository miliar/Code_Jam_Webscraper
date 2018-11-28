#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

int to[200][200][5];
char grid[200][200];

inline int convert(char c)
{
	switch (c)
	{
		case '>': return RIGHT;
		case '<': return LEFT;
		case '^': return UP;
		case 'v': return DOWN;
	}
	return -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int R,C;
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; i++)
		{
			scanf("%s", grid[i]);
		}
		memset(to, -1, sizeof(to));
		for (int i = 0; i < R; i++)
		{
			int last = -1;
			for (int j = 0; j < C; j++)
			{
				if (grid[i][j] == '.') continue;
				to[i][j][LEFT] = last;
				if (last != -1) to[i][last][RIGHT] = j;
				last = j;
			}
		}
		for (int j = 0; j < C; j++)
		{
			int last = -1;
			for (int i = 0; i < R; i++)
			{
				if (grid[i][j] == '.') continue;
				to[i][j][UP] = last;
				if (last != -1) to[last][j][DOWN] = i;
				last = i;
			}
		}
		int num = 0;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (grid[i][j] == '.') continue;
				if (to[i][j][convert(grid[i][j])] == -1)
				{
					int one = 0;
					for (int k = 0; k < 4; k++)
						one |= (to[i][j][k] != -1);
					if (!one)
					{
						printf("Case #%d: IMPOSSIBLE\n", t);
						num = -2; i = R; j = C;
					}
					num++;
				}
			}
		}
		if (num != -1) printf("Case #%d: %d\n", t, num);
	}
}
