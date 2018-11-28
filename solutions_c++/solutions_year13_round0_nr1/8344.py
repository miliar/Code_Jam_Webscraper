#include <stdio.h>


char map[5][5];
int main()
{
//	freopen("d:\\gcj\\tic.in","r",stdin);
//  freopen("d:\\gcj\\tic.out","w",stdout);
	int i,j,case_t,t;
	int cnt=0;
	scanf("%d",&case_t);
	for(t=1;t<=case_t;t++)
	{
		for(i=0;i<4;i++)
			scanf("%s",map[i]);
		int flag=0;
		printf("Case #%d: ",t);
		if(map[0][0]=='X')
		{
			cnt=1;
			if(map[1][1]=='X' || map[1][1]=='T') 
				cnt++;
			if(map[2][2]=='X' || map[2][2]=='T')
				cnt++;
			if(map[3][3]=='X' || map[3][3]=='T')
				cnt++;
			if(cnt==4)
			{
				puts("X won");
				flag=1;
				continue;
			}
		}
		if(map[0][0]=='O')
		{
			cnt=1;
			if(map[1][1]=='O' || map[1][1]=='T') 
				cnt++;
			if(map[2][2]=='O' || map[2][2]=='T')
				cnt++;
			if(map[3][3]=='O' || map[3][3]=='T')
				cnt++;
			if(cnt==4)
			{
				puts("O won");
				flag=1;
				continue;
			}
		}
		if(map[0][3]=='X')
		{
			cnt=1;
			if(map[1][2]=='X' || map[1][2]=='T') 
				cnt++;
			if(map[2][1]=='X' || map[2][1]=='T')
				cnt++;
			if(map[3][0]=='X' || map[3][0]=='T')
				cnt++;
			if(cnt==4)
			{
				puts("X won");
				flag=1;
				continue;
			}
		}
		if(map[0][3]=='O')
		{
			cnt=1;
			if(map[1][2]=='O' || map[1][2]=='T') 
				cnt++;
			if(map[2][1]=='O' || map[2][1]=='T')
				cnt++;
			if(map[3][0]=='O' || map[3][0]=='T')
				cnt++;
			if(cnt==4)
			{
				puts("O won");
				flag=1;
				continue;
			}
		}
		for(i=0;i<4;i++)
		{
			if(map[i][0]=='X')
			{
				cnt=1;
				if(map[i][1]=='X' || map[i][1]=='T') 
					cnt++;
				if(map[i][2]=='X' || map[i][2]=='T')
					cnt++;
				if(map[i][3]=='X' || map[i][3]=='T')
					cnt++;
				if(cnt==4)
				{
					puts("X won");
					flag=1;
					break;
				}
			}
			else if(map[i][0]=='O')
			{
				cnt=1;
				if(map[i][1]=='O' || map[i][1]=='T') 
					cnt++;
				if(map[i][2]=='O' || map[i][2]=='T')
					cnt++;
				if(map[i][3]=='O' || map[i][3]=='T')
					cnt++;
				if(cnt==4)
				{
					puts("O won");
					flag=1;
					break;
				}
			}
			
		}
		if(flag)
			continue;
		for(i=0;i<4;i++)
		{
			if(map[0][i]=='X')
			{
				cnt=1;
				if(map[1][i]=='X' || map[1][i]=='T') 
					cnt++;
				if(map[2][i]=='X' || map[2][i]=='T')
					cnt++;
				if(map[3][i]=='X' || map[3][i]=='T')
					cnt++;
				if(cnt==4)
				{
					puts("X won");
					flag=1;
					break;
				}
			}
			else if(map[0][i]=='O')
			{
				cnt=1;
				if(map[1][i]=='O' || map[1][i]=='T') 
					cnt++;
				if(map[2][i]=='O' || map[2][i]=='T')
					cnt++;
				if(map[3][i]=='O' || map[3][i]=='T')
					cnt++;
				if(cnt==4)
				{
					puts("O won");
					flag=1;
					break;
				}
			}			
		}
		if(flag)
			continue;
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
				if(map[i][j]=='.')
				{
					puts("Game has not completed");
					flag=1;
					break;
				}
			if(flag)
				break;
		}
		if(flag)
			continue;
		puts("Draw");
	}
	return 0;
}