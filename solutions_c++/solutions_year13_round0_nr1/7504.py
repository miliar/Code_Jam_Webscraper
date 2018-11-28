#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

char p[6][6];
int map[5][5];

int main()
{
	
	int t;
	scanf("%d",&t);
	int tt=t;
	
	while(t--)
	{
		for(int i=0;i<4;i++)
			scanf("%s",p[i]);
		
		int dx=-1,dy=-1;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(p[i][j]=='O')
					map[i][j]=1;
				else if(p[i][j]=='X')
					map[i][j]=2;
				else if(p[i][j]=='.')
					map[i][j]=0;
				else
				{
					dx=i;
					dy=j;
					map[i][j]=-1;	
				}
			}	
		}
		
		/*for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				printf("%d ",map[i][j]);
			printf("\n");	
		}*/
		
		int ans=0;
		
		if(dx==-1 && dy==-1)
		{
			for(int i=0;i<4;i++)
			{
				if(map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][0]==1
				|| map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[0][i]==1)
				{
					ans=1;
					break;
				}
			}
			if(map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[0][3]==map[3][0] && map[0][3]==1 
			|| map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[0][0]==1)
				ans=1;
			
			for(int i=0;i<4;i++)
			{
				if(map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][0]==2
				|| map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[0][i]==2)
				{
					ans=2;
					break;
				}
			}
			if(map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[0][3]==map[3][0] && map[0][3]==2 
			|| map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[0][0]==2)
				ans=2;
		}
		else
		{
			map[dx][dy]=1;
			for(int i=0;i<4;i++)
			{
				if(map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][0]==1
				|| map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[0][i]==1)
				{
					ans=1;
					break;
				}
			}
			if(map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[0][3]==map[3][0] && map[0][3]==1 
			|| map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[0][0]==1)
				ans=1;
				
			map[dx][dy]=2;
			for(int i=0;i<4;i++)
			{
				if(map[i][0]==map[i][1] && map[i][0]==map[i][2] && map[i][0]==map[i][3] && map[i][0]==2
				|| map[0][i]==map[1][i] && map[0][i]==map[2][i] && map[0][i]==map[3][i] && map[0][i]==2)
				{
					ans=2;
					break;
				}
			}
			if(map[0][3]==map[1][2] && map[0][3]==map[2][1] && map[0][3]==map[3][0] && map[0][3]==2 
			|| map[0][0]==map[1][1] && map[0][0]==map[2][2] && map[0][0]==map[3][3] && map[0][0]==2)
				ans=2;
			map[dx][dy]=-1;
		}
		
		printf("Case #%d: ",tt-t);
		
		if(ans==1)
			printf("O won\n");
		else if(ans==2)
			printf("X won\n");
		else
		{
			int check=0;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
				{
					if(map[i][j]==0)
						check=1;
				}
			if(check)
				printf("Game has not completed\n");
			else
				printf("Draw\n");
		}
	}
	scanf(" ");
	return 0;	
}
