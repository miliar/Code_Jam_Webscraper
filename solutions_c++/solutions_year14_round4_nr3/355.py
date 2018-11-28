#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

#define MAXW 110
#define MAXH 510
#define MAXB 20

int w, h, b;

int mat[MAXW][MAXH], pos[MAXB][4];

int global = 0;

int move[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

bool walk(int i, int j, int dir)
{
	// printf("Now i = %d, j = %d\n", i, j);
	mat[i][j] = -1;
	if (j == h - 1)
	{
		global++;
		return true;
	}
	bool flag = false;
	for (int d = 0; d < 3; d++)
	{
		int sel = (dir - 1 + d + 4) % 4;
		int ni = i + move[sel][0];
		int nj = j + move[sel][1];
		if (ni >= 0 && ni < w && nj >= 0 && nj < h && mat[ni][nj] == 1)
		{
			flag = walk(ni, nj, sel);
			if (flag) return true;
		}
	}
	return false;
}

int main()
{
	int t, cas;
	int i, j, k;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		scanf("%d%d%d", &w, &h, &b);
		for (i = 0; i < w; i++)
			for (j = 0; j < h; j++)
				mat[i][j] = 1;
		for (i = 0; i < b; i++)
		{
			for (j = 0; j < 4; j++)
				scanf("%d", &pos[i][j]);
			pos[i][3]++;
		}
		for (i = 0; i < b; i++)
		{
			int x0 = pos[i][0], x1 = pos[i][2];
			int y0 = pos[i][1], y1 = pos[i][3];
			for (j = x0; j <= x1; j++)
				for (k = y0; k < y1; k++)
					mat[j][k] = 0;
		}
		// for (j = h - 1; j >= 0; j--)
		// {
			// for (i = 0; i < w; i++) printf("%d", mat[i][j]);
			// printf("\n");
		// }
		// printf("\n");
		
		global = 0;
		for (i = 0; i < w; i++)
			if (mat[i][0] == 1)
				walk(i, 0, 1);
		printf("Case #%d: %d\n", cas, global);
	}
	return 0;
}
