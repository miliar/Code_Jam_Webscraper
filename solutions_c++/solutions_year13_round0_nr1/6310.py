#include <stdio.h>

char gp[6][6];
char ch;

bool X(int x,int y) { return gp[x][y]==ch||gp[x][y]=='T'; }

int main()
{
	int T;
	freopen("c:\\temp\\a.in","r",stdin);
	freopen("c:\\temp\\a.out","w",stdout);
	scanf("%d",&T);
	for (int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);

		for (int i = 1; i <= 4; i++)
		{
			scanf("%s",gp[i]+1);
		}
		ch='X';

		if(X(1,1)&&X(1,2)&&X(1,3)&&X(1,4) ||
			X(2,1)&&X(2,2)&&X(2,3)&&X(2,4) ||
			X(3,1)&&X(3,2)&&X(3,3)&&X(3,4) ||
			X(4,1)&&X(4,2)&&X(4,3)&&X(4,4) ||

			X(1,1)&&X(2,1)&&X(3,1)&&X(4,1) ||
			X(1,2)&&X(2,2)&&X(3,2)&&X(4,2) ||
			X(1,3)&&X(2,3)&&X(3,3)&&X(4,3) ||
			X(1,4)&&X(2,4)&&X(3,4)&&X(4,4) ||

			X(1,1)&&X(2,2)&&X(3,3)&&X(4,4) ||
			X(4,1)&&X(3,2)&&X(2,3)&&X(1,4))
		{
			printf("X won\n");
			continue;
		}
		ch='O';
		if(X(1,1)&&X(1,2)&&X(1,3)&&X(1,4) ||
			X(2,1)&&X(2,2)&&X(2,3)&&X(2,4) ||
			X(3,1)&&X(3,2)&&X(3,3)&&X(3,4) ||
			X(4,1)&&X(4,2)&&X(4,3)&&X(4,4) ||

			X(1,1)&&X(2,1)&&X(3,1)&&X(4,1) ||
			X(1,2)&&X(2,2)&&X(3,2)&&X(4,2) ||
			X(1,3)&&X(2,3)&&X(3,3)&&X(4,3) ||
			X(1,4)&&X(2,4)&&X(3,4)&&X(4,4) ||

			X(1,1)&&X(2,2)&&X(3,3)&&X(4,4) ||
			X(4,1)&&X(3,2)&&X(2,3)&&X(1,4))
		{
			printf("O won\n");
			continue;
		}

		for(int i=1; i<=4; i++)
		{
			for (int j =1; j <= 4; j++)
			{
				if(gp[i][j]=='.')
				{
					printf("Game has not completed\n");
					goto outloop;
				}
			}
		}

		printf("Draw\n");

outloop:
		;
	}
	return 0;
}