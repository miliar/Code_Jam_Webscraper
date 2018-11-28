#include <stdio.h>
#include <algorithm>

int arr[5][5];
bool vst[5][5];
int r, c;

int dfs(int x, int y)
{
	int i, j, nx, ny, sum = 1;

	vst[x][y] = 1;

	for (i = -1; i <= 1; i++)
		for (j = -1; j <= 1; j++)
		{
			nx = x + i;
			ny = y + j;
			if (nx >= 0 && nx < r && ny >= 0 && ny < c && !arr[nx][ny])
				return sum;
		}

	for (i = -1; i <= 1; i++)
		for (j = -1; j <= 1; j++)
		{	
			nx = x + i;
			ny = y + j;
			if (nx >= 0 && nx < r && ny >= 0 && ny < c && !vst[nx][ny])
				sum += dfs(nx, ny);
		}

	return sum;
}


int main()
{
	int t, cnt, x, ansx, ansy;
	int m, i, j, k, l;
	int tmp[25];
	bool flag;
	
	scanf("%d", &t);
	for (cnt = 1; cnt <= t; cnt++)
	{
		scanf("%d %d %d", &r, &c, &m);

		for (i = 0; i < m; i++) tmp[i] = 0;
		for (; i < r * c; i++) tmp[i] = 1;

		flag = true;
		
		do {
			x = 0;
			for (i = 0; i < r; i++)
				for (j = 0; j < c; j++)
					arr[i][j] = tmp[x++];
			for (k = 0; k < r && flag; k++)
				for (l = 0; l < c && flag; l++)
				{	
					if (!arr[k][l]) continue;
					for (i = 0; i < r; i++)
						for (j = 0; j < c; j++)
							vst[i][j] = 0;
					if (dfs(k, l) == r * c - m)
					{
						ansx = k;
						ansy = l;
						flag = false;
					}
				}
			if (!flag) break;
					
		} while (std::next_permutation(tmp, tmp+r*c));
		printf("Case #%d:\n", cnt);
		if (flag) puts("Impossible");
		else
		{
			for (i = 0; i < r; i++)
			{
				for (j = 0; j < c; j++)
				{
					if (i == ansx && j == ansy) putchar('c');
					else putchar(arr[i][j] ? '.' : '*');
				}
				puts("");
			}
		}
	}
	return 0;
}
