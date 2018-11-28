#include<stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d\n",&T);
	for(int Case = 1 ; Case<=T ; Case++)
	{
		char data[20][20]={0};
		bool checkEnd = true;
		for(int i = 4 ; i <= 4+4 ; i++)
		{
			gets(data[i]+4);
		}

		int winner = 0;
		int oCount, xCount, tCount;
		for(int i = 4 ; i <= 4+4 ; i++)
		{
			for(int j = 4 ; j <= 4+4; j++)
			{
				if(data[i][j]=='.') checkEnd=false;
				oCount=0;
				xCount=0;
				tCount=0;
				for(int k = 0 ; k < 4 ; k++)
				{
					if(data[i][j+k]=='O') oCount++;
					if(data[i][j+k]=='X') xCount++;
					if(data[i][j+k]=='T') tCount++;
				}
				if(oCount+tCount == 4)
				{
					winner = 1;
					break;
				}
				if(xCount+tCount == 4)
				{
					winner = 2;
					break;
				}

				oCount=0;
				xCount=0;
				tCount=0;
				for(int k = 0 ; k < 4 ; k++)
				{
					if(data[i+k][j]=='O') oCount++;
					if(data[i+k][j]=='X') xCount++;
					if(data[i+k][j]=='T') tCount++;
				}
				if(oCount+tCount == 4)
				{
					winner = 1;
					break;
				}
				if(xCount+tCount == 4)
				{
					winner = 2;
					break;
				}
				
				oCount=0;
				xCount=0;
				tCount=0;
				for(int k = 0 ; k < 4 ; k++)
				{
					if(data[i+k][j+k]=='O') oCount++;
					if(data[i+k][j+k]=='X') xCount++;
					if(data[i+k][j+k]=='T') tCount++;
				}
				if(oCount+tCount == 4)
				{
					winner = 1;
					break;
				}
				if(xCount+tCount == 4)
				{
					winner = 2;
					break;
				}
				
				oCount=0;
				xCount=0;
				tCount=0;
				for(int k = 0 ; k < 4 ; k++)
				{
					if(data[i+k][j-k]=='O') oCount++;
					if(data[i+k][j-k]=='X') xCount++;
					if(data[i+k][j-k]=='T') tCount++;
				}
				if(oCount+tCount == 4)
				{
					winner = 1;
					break;
				}
				if(xCount+tCount == 4)
				{
					winner = 2;
					break;
				}
			}
			if(winner!=0) break;
		}
		if(winner==1) printf("Case #%d: O won\n",Case);
		else if(winner==2) printf("Case #%d: X won\n",Case);
		else if(checkEnd) printf("Case #%d: Draw\n",Case);
		else printf("Case #%d: Game has not completed\n",Case);
	}
	return 0;
}