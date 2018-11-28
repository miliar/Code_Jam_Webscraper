#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>

using namespace std;

const string owins = "O won";
const string xwins = "X won";
const string draw = "Draw";
const string notCompleted = "Game has not completed";

char a[4][5];
bool hasempty;

void init()
{
	hasempty = false;
	for (int i = 0; i < 4; i++)
	{
		gets(a[i]);
	}
	scanf("\n");
}

int check(int x, int y, int dx, int dy)
{
	int xn = 0, on = 0, tn = 0;
	for (int i = 0; i < 4; i++)
	{
		if (a[x][y] == 'X')
		{
			xn++;
		}
		if (a[x][y] == 'O')
		{
			on++;
		}
		if (a[x][y] == 'T')
		{
			tn++;
		}
		if (a[x][y] == '.')
		{
			hasempty = true;
		}
		x += dx;
		y += dy;
	}
	if (xn + tn == 4) return 1;
	if (on + tn == 4) return 0;
	return 2;
}

string solve()
{
	int res[4 + 4 + 2];
	int cnt = 0;
	for (int i = 0; i < 4; i++)
	{
		res[cnt++] = check(i,0,0,1);
		res[cnt++] = check(0,i,1,0);
	}
	res[cnt++] = check(0,0,1,1);
	res[cnt++] = check(3,0,-1,1);
	for (int i = 0 ; i < 10; i++)
	{
		if (res[i] == 0)
			{
				return owins;
			} else
				if (res[i] == 1)
				{
					return xwins;
				}
	}
	if (hasempty)
	{
		return notCompleted;
	} else
	{
		return draw;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int i = 1; i <= t; i++)
	{
		init();
		printf("Case #%d: %s\n", i, solve().c_str());
	}
	return 0;
}