#include<iostream>
using namespace std;
char mt[10][10]={{0}};
int d[][2] ={{0,1}, {0,-1},{1,0},{-1,0},{1,1},{-1,-1}, {1,-1},{-1,1}};
int main()
{
	int t;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &t);
	for(int ii = 1; ii<=t; ii++)
	{
		printf("Case #%d: ",ii);
		bool ec = 0, fl = 1;
		for(int i = 1; i<=4; i++)
		{
			for(int j = 1; j<=4; j++)
			{
				scanf("%c", &mt[i][j]);
				if(mt[i][j] == '.')
					ec = 1;
			}
			scanf("\n");
		}
		for(int i = 1; i <= 4 && fl; i++)
		{
			int cx = 0, co = 0, ct = 0;
			for(int j = 1; j<=4; j++)
			{
				if(mt[i][j] == 'T')
					ct++;
				if(mt[i][j] == 'X')
					cx++;
				if(mt[i][j] == 'O')
					co++;
			}
			if(co + ct == 4)
			{
				printf("O won\n");
				fl = 0;
			}
			if(cx + ct == 4)
			{
				printf("X won\n");
				fl = 0;
			}
		}
		for(int i = 1; i <= 4 && fl; i++)
		{
			int cx = 0, co = 0, ct = 0;
			for(int j = 1; j<=4; j++)
			{
				if(mt[j][i] == 'T')
					ct++;
				if(mt[j][i] == 'X')
					cx++;
				if(mt[j][i] == 'O')
					co++;
			}
			if(co + ct == 4)
			{
				printf("O won\n");
				fl = 0;
			}
			if(cx + ct == 4)
			{
				printf("X won\n");
				fl = 0;
			}
		}
		if(fl)
		{
			int cx = 0, co = 0, ct = 0;
			for(int j = 1; j<=4; j++)
			{
				if(mt[j][j] == 'T')
					ct++;
				if(mt[j][j] == 'X')
					cx++;
				if(mt[j][j] == 'O')
					co++;
			}
			if(co + ct == 4)
			{
				printf("O won\n");
				fl = 0;
			}
			if(cx + ct == 4)
			{
				printf("X won\n");
				fl = 0;
			}
		}
		if(fl)
		{
			int cx = 0, co = 0, ct = 0;
			for(int j = 1; j<=4; j++)
			{
				if(mt[j][5-j] == 'T')
					ct++;
				if(mt[j][5-j] == 'X')
					cx++;
				if(mt[j][5-j] == 'O')
					co++;
			}
			if(co + ct == 4)
			{
				printf("O won\n");
				fl = 0;
			}
			if(cx + ct == 4)
			{
				printf("X won\n");
				fl = 0;
			}
		}
		if(fl)
		{
			if(!ec)
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
		scanf("\n");
	}
	return 0;
}