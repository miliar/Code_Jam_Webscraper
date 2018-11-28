#include<stdio.h>

int t;
int c;
int f, s;
int fcards[4][4], scards[4][4];

void init(int x)
{
	c = x+1;
	scanf("%d", &f);
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			scanf("%d", &fcards[i][j]);
		}
	}
	scanf("%d", &s);
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			scanf("%d", &scards[i][j]);
		}
	}
}

void magic()
{
	int ret = -1;
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			if(fcards[f-1][i] == scards[s-1][j])
			{
				if(ret == -1)
				{
					ret = fcards[f-1][i];
				}
				else
				{
					printf("Case #%d: Bad magician!\n", c);
					return;
				}
			}
		}
	}
	if(ret != -1)
	{
		printf("Case #%d: %d\n", c, ret);
	}
	else
	{
		printf("Case #%d: Volunteer cheated!\n", c);
	}
}

int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("magic-havin.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		init(i);
		magic();
	}

	return 0;
}