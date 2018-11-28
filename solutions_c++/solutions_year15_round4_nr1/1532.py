#include<stdio.h>
#include<algorithm>

#pragma warning(disable:4996)

int T;
int R, C;
char map[111][111];

#define NONE ('.')
#define UP ('^')
#define DOWN ('v')
#define LEFT ('<')
#define RIGHT ('>')

int main()
{

	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	
	int t;
	int i, j, k;

	int cnt; 
	bool chk;
	
	char last;

	fscanf(in, "%d", &T);

	for (t = 1; t <= T; t++)
	{
		fscanf(in, "%d %d ", &R, &C);
		for (i = 0; i < R; i++)
			fscanf(in,"%s", map[i]);

		cnt = 0;
		chk = true;

		for (i = 0; i < R && chk; i++)
		{
			last = NONE;
			for (j = 0; j < C; j++)
			{
				if (map[i][j] != NONE)
				{
					if (last == NONE)
					{
						if (map[i][j] == LEFT)
							cnt++;
						chk = false;
						for (k = 0; k < R && !chk; k++)
						{
							if (map[k][j] != NONE && k != i)
							{
								chk = true;
							}
						}
					}
					else
					{
						chk = true;
					}
					last = map[i][j];
				}
			}
			if (last == RIGHT)
				cnt++;
		}

		for (i = 0; i < C && chk; i++)
		{
			last = NONE;
			for (j = 0; j < R; j++)
			{
				if (map[j][i] != NONE)
				{
					if (last == NONE)
					{
						if (map[j][i] == UP)
							cnt++;
						chk = false;
						for (k = 0; k < C && !chk; k++)
						{
							if (map[j][k] != NONE && k != i)
							{
								chk = true;
							}
						}
					}
					else
					{
						chk = true;
					}
					last = map[j][i];
				}
			}
			if (last == DOWN)
				cnt++;
		}

		fprintf(out,"Case #%d: ", t);

		if (chk) fprintf(out,"%d\n", cnt);
		else fprintf(out,"IMPOSSIBLE\n");
	}

	return 0;
}