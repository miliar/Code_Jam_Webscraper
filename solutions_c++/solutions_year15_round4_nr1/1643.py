#define _CRT_SECURE_NO_WARNINGS C4996
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#define UP '^'
#define DOWN 'v'
#define RIGHT '>'
#define LEFT '<'
#define NONE '.'
int r, c;
int mindata = 0;
int minget = 0x7ffffff;
int rcheck[110][110], rcount;
int check[110][110];
char data[110][110];
char st[110][110];
int count = 0;
bool check_route(int x, int y, char vec)
{
	rcount++;
	while ((x > 0 && x <= r) && (y > 0 && y <= c))
	{
		if (st[x][y] == UP)
		{
			vec = UP;
		}
		else if (st[x][y] == DOWN)
		{
			vec = DOWN;
		}
		else if (st[x][y] == RIGHT)
		{
			vec = RIGHT;
		}
		else if (st[x][y] == LEFT)
		{
			vec = LEFT;
		}
		if (rcheck[x][y] == rcount) return true;
		rcheck[x][y] = rcount;
		if (vec == UP){ x--; }
		else if (vec == DOWN){ x++; }
		else if (vec == RIGHT){ y++; }
		else if (vec == LEFT){ y--; }
	}
	return false;
}
void back_process(int x, int y, int cval)
{
	char val = st[x][y];
	if (x == r + 1)
	{
		int i, a;

		for (i = 1; i <= r; i++)
		{
			for (a = 1; a <= c; a++)
			{
				if (!check_route(i, a, st[i][a])) return;
			}
		}
		if (minget > cval) minget = cval;
	}
	else if (y == c + 1) back_process(x + 1, 1, cval);
	else if (st[x][y] != NONE)
	{
		st[x][y] = RIGHT;
		back_process(x, y + 1, cval + (val != st[x][y]));
		st[x][y] = LEFT;
		back_process(x, y + 1, cval + (val != st[x][y]));
		st[x][y] = DOWN;
		back_process(x, y + 1, cval + (val != st[x][y]));
		st[x][y] = UP;
		back_process(x, y + 1, cval + (val != st[x][y]));
		st[x][y] = val;
	}
	else if (st[x][y] == NONE) back_process(x, y + 1, cval);
}
bool process(char vec, int x, int y, bool sw)
{
	int stx = x, sty = y;
	int edx = x, edy = y;
	char changevec = vec;

	count++;
	while ((x > 0 && x <= r) && (y > 0 && y <= c))
	{
		if (data[x][y] == UP)
		{
			if (vec == UP){ changevec = DOWN; }
			else if (vec == DOWN){ changevec = UP; }
			else if (vec == RIGHT){ changevec = LEFT; }
			else if (vec == LEFT){ changevec = RIGHT; }
			edx = x; edy = y;
			vec = UP;
		}
		else if (data[x][y] == DOWN)
		{
			if (vec == UP){ changevec = DOWN; }
			else if (vec == DOWN){ changevec = UP; }
			else if (vec == RIGHT){ changevec = LEFT; }
			else if (vec == LEFT){ changevec = RIGHT; }
			edx = x; edy = y;
			vec = DOWN;
		}
		else if (data[x][y] == RIGHT)
		{
			if (vec == UP){ changevec = DOWN; }
			else if (vec == DOWN){ changevec = UP; }
			else if (vec == RIGHT){ changevec = LEFT; }
			else if (vec == LEFT){ changevec = RIGHT; }
			edx = x; edy = y;
			vec = RIGHT;
		}
		else if (data[x][y] == LEFT)
		{
			if (vec == UP){ changevec = DOWN; }
			else if (vec == DOWN){ changevec = UP; }
			else if (vec == RIGHT){ changevec = LEFT; }
			else if (vec == LEFT){ changevec = RIGHT; }
			edx = x; edy = y;
			vec = LEFT;
		}
		if (check[x][y] == count) return true;
		check[x][y] = count;
		if (vec == UP){ x--; }
		else if (vec == DOWN){ x++; }
		else if (vec == RIGHT){ y++; }
		else if (vec == LEFT){ y--; }
	}

	if (sw == true && (edx != stx || edy != sty))
	{
		data[edx][edy] = changevec;
		mindata++;
		return true;
	}
	return false;
}
bool last_check_process(char vec, int x, int y)
{
	int stx = x, sty = y;
	int edx = x, edy = y;
	char changevec = vec;
	bool sw = 0;

	count++;
	data[x][y] = UP;
	if (process(vec, x, y, true)){
		mindata++;
		return true;
	}
	data[x][y] = DOWN;
	if (process(vec, x, y, true)){
		mindata++;
		return true;
	}
	data[x][y] = RIGHT;
	if (process(vec, x, y, true)){
		mindata++;
		return true;
	}
	data[x][y] = LEFT;
	if (process(vec, x, y, true)){
		mindata++;
		return true;
	}
	return false;
}
int main()
{
	int i, a;
	int Test = 0;
	int ans = 0;
	bool sw = 0;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	srand(time(NULL));
	scanf("%d", &Test);

	for (int P = 1; P <= Test; P++)
	{
		scanf("%d%d", &r, &c);
		if (P == 99)
		{
			P = P;
		}
		for (i = 1; i <= r; i++)
		{
			scanf("%s\n", data[i] + 1);
			for (a = 1; a <= c; a++)
			{
				check[i][a] = rcheck[i][a] = 0;
				st[i][a] = data[i][a];
			}
		}
		count = rcount = 0;
		mindata = 0;
		minget = r*c;
		for (i = 1; i <= r; i++)
		{
			for (a = 1; a <= c; a++)
			{
				if (data[i][a] != NONE) process(data[i][a], i, a, true);
			}
		}
		sw = false;
		for (i = 1; i <= r; i++)
		{
			for (a = 1; a <= c; a++)
			{
				if (!process(data[i][a], i, a, false))
				{
					if (!last_check_process(data[i][a], i, a))
					{
						sw = 1;
						break;
					}
				}
			}
			if (sw) break;
		}
		/*if ((sw && minget == r*c) || minget == mindata)
		{
		printf("OK!\n");
		}
		else
		{
		for (i = 1; i <= r; i++)
		{
		for (a = 1; a <= c; a++)
		{
		printf("%c", st[i][a]);
		}
		printf("\n");
		}
		printf("%d %d\n", mindata, minget);
		break;
		}*/
		if (!sw)printf("Case #%d: %d\n", P, mindata);
		else printf("Case #%d: IMPOSSIBLE\n", P);
		//printf("%d\n", minget);
	}

	return 0;
}
