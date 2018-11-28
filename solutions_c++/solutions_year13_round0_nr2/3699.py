#include<stdio.h>
int map[110][110];
int n, m;
int judge(int x, int y)
{
	int a, b;
	int max;

	max = 0;
	for(a = x+1; a < n; a ++)
	{
		if( map[a][y] > max)
			max = map[a][y];
	}
	if( max > map[x][y] )
	{
		max = 0;
		for(b = y+1; b < m; b ++)
		{
			if( map[x][b] > max)
				max = map[x][b];
		}
		if( max > map[x][y] )
			return 1;
		else
		{
			max = 0;
			for(b = y-1; b >= 0; b --)
			{
				if( map[x][b] > max)
					max = map[x][b];
			}
			if( max > map[x][y])
				return 1;
			else
				return 0;
		}
	}
	else
	{
		max = 0;
		for(a = x-1; a >= 0; a --)
		{
			if(map[a][y] > max)
				max = map[a][y];
		}
		if( max > map[x][y])
		{
			max = 0;
			for(b = y+1; b < m; b ++)
			{
				if( map[x][b] > max)
					max = map[x][b];
			}
			if( max > map[x][y] )
				return 1;
			else
			{
				max = 0;
				for(b = y-1; b >= 0; b --)
				{
					if( map[x][b] > max)
						max = map[x][b];
				}
				if(max > map[x][y])
					return 1;
				else
					return 0;
			}
		}
		else
			return 0;
	}

}
int main()
{
	int t, i, j, k;
	int flag ;
	scanf("%d", &t);
	for(i = 1; i <= t; i ++)
	{
		flag = 0;
		scanf("%d %d", &n, &m);
		for(j = 0; j < n; j ++)
		{
			for(k = 0; k < m; k ++)
			{
				scanf("%d", &map[j][k]);
			}
		}
		for(j = 0; j < n; j ++)
		{
			for(k = 0; k < m; k ++)
			{
				if( judge(j, k ) == 1)
					flag = 1;
			}
		}
		if( flag == 1)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: YES\n", i);
	}
	return 0;
}