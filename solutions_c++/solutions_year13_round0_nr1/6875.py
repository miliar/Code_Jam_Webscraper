#include<stdio.h>
#include<string.h>
char map[10][10];
int dp[10][10][4];

int dir(int x,int y,int d)
{
	if(d==0)
	{
		if(x-1>=0&&map[x-1][y]==map[x][y])
			return dp[x-1][y][d];
		if(map[x-1][y]=='T')
			if(x-2>=0&&map[x-2][y]==map[x][y])
				return dp[x-1][y][d];
			else
				return 1;
	}
	else if(d==1)
	{
		if(y-1>=0&&map[x][y-1]==map[x][y])
			return dp[x][y-1][d];
		if(map[x][y-1]=='T')
			if(y-2>=0&&map[x][y-2]==map[x][y])
				return dp[x][y-1][d];
			else
				return 1;
	}
	else if(d==2)
	{
		if(x-1>=0&&y-1>=0&&map[x-1][y-1]==map[x][y])
			return dp[x-1][y-1][d];
		if(map[x-1][y-1]=='T')
			if(x-2>=0&&y-2>=0&&map[x-2][y-2]==map[x][y])
				return dp[x-1][y-1][d];
			else
				return 1;
	}	
	else
	{
		if(x-1>=0&&y+1<4&&map[x-1][y+1]==map[x][y])
			return dp[x-1][y+1][d];
		if(map[x-1][y+1]=='T')
			if(x-2>=0&&y+2<4&&map[x-2][y+2]==map[x][y])
				return dp[x-1][y+1][d];
			else
				return 1;
	}
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin) ;
	freopen("A-large.out","w",stdout) ;

	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		for(int i=0;i<4;i++)
			scanf("%s",map[i]);
			
		memset(dp,0,sizeof(dp));
		int end=1;
		int over=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(map[i][j]=='.')
				{
					end=0;
					continue;
				}
				else if(map[i][j]=='T')
				{
					for(int q=0;q<4;q++)
						dp[i][j][q]=1;
					if(i-1>=0)
						dp[i][j][0]+=dp[i-1][j][0];
					if(j-1>=0)
						dp[i][j][1]+=dp[i][j-1][1];
					if(i-1>=0&&j-1>=0)
						dp[i][j][2]+=dp[i-1][j-1][2];
					if(i-1>=0&&j+1<4)
						dp[i][j][3]+=dp[i-1][j+1][3];
				}
				else
				{
					for(int p=0;p<4;p++)
					{
						dp[i][j][p]=1+dir(i,j,p);
					}
				}
				for(int p=0;p<4;p++)
				{
					if(dp[i][j][p]==4)
					{
						char c=map[i][j];
						if(map[i][j]=='T')
						{
							if(p==0)
								c=map[i-1][j];
							else if(p==1)
								c=map[i][j-1];
							else if(p==2)
								c=map[i-1][j-1];
							else 
								c=map[i-1][j+1];
						}
						printf("Case #%d: %c won\n",k,c);
						over=1;
						break;
					}
				}
				if(over)
					break;
			}
			if(over)
				break;
		}/*
		for(int i=0;i<4;i++)
		{
			printf("%d:\n",i);
			for(int j=0;j<4;j++)
			{
				for(int p=0;p<4;p++)
					printf("%d ",dp[j][p][i]);
				printf("\n");
			}
			
		}*/
		if(over)
			continue;
		if(end==0)
			printf("Case #%d: Game has not completed\n",k);
		else
			printf("Case #%d: Draw\n",k);
	}	
	return 0;
}
