#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char map[10][10];
int checkd(int y,int flag)
{
	if(flag==1)
	{
		for(int i=1;i<4;i++)
			if(map[i][y]=='O'||map[i][y]=='.')
				return 0;
		return 1;
	}
	else if(flag==0)
	{
		for(int i=1;i<4;i++)
			if(map[i][y]=='X'||map[i][y]=='.')
				return 0;
		return 1;
	}
}
int checkr(int x,int flag)
{
	if(flag==1)
	{
		for(int i=1;i<4;i++)
			if(map[x][i]=='O'||map[x][i]=='.')
				return 0;
		return 1;
	}
	else if(flag==0)
	{
		for(int i=1;i<4;i++)
			if(map[x][i]=='X'||map[x][i]=='.')
				return 0;
		return 1;
	}
}
int checkrd(int flag)
{
	if(flag)
	{
		for(int i=1;i<4;i++)
			if(map[i][i]=='O'||map[i][i]=='.')
				return 0;
		return 1;
	}
	else
	{
		for(int i=1;i<4;i++)
			if(map[i][i]=='X'||map[i][i]=='.')
				return 0;
		return 1;
	}
}
int checkld(int flag)
{
	if(flag)
	{
		for(int i=1;i<4;i++)
		{
			if(map[i][3-i]=='O'||map[i][3-i]=='.')
				return 0;
		}
		return 1;
	}
	else
	{
		for(int i=1;i<4;i++)
		{
			if(map[i][3-i]=='X'||map[i][3-i]=='.')
				return 0;
		}
		return 1;
	}
}
int main()
{
	int T,ncase=1;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("ouput.txt","w",stdout);
	cin>>T;
	while(T--)
	{
		memset(map,'\0',sizeof map);
		for(int i=0;i<4;i++)
			scanf("%s",map[i]);
		bool flag1=0,flag2=0;
		if(map[0][0]=='T')
		{
			if(map[1][1]=='X') flag1=checkrd(1);
			else if(map[1][1]=='O') flag2=checkrd(0);
		}
		else if(map[0][0]=='X') flag1=checkrd(1);
		else if(map[0][0]=='O') flag2=checkrd(0);
		if(map[0][3]=='T')
		{
			if(map[1][2]=='X'&&!flag1)
				flag1=checkld(1);
			else if(map[1][2]=='O'&&!flag2)
				flag2=checkld(0);
		}
		else if(map[0][3]=='X'&&!flag1)
			flag1=checkld(1);
		else if(map[0][3]=='O'&&!flag2)
			flag2=checkld(0);
		for(int i=0;i<4;i++)
		{
			if(map[i][0]=='X')
			{
				if(!flag1)
					flag1=checkr(i,1);
				//cout<<flag1<<endl;
			}
			else if(map[i][0]=='O')
			{
				if(!flag2)
					flag2=checkr(i,0);
			}
			else if(map[i][0]=='T')
			{
				if(map[i][1]=='X')
				{
					if(!flag1)
						flag1=checkr(i,1);
				}
				else if(map[i][1]=='O')
				{
					if(!flag2)
						flag2=checkr(i,0);
				}
			}
			if(map[0][i]=='X')
			{
				if(!flag1)
					flag1=checkd(i,1);
			}
			else if(map[0][i]=='O')
			{
				if(!flag2)
					flag2=checkd(i,0);
			}
			else if(map[0][i]=='T')
			{
				if(map[1][i]=='X')
				{
					if(!flag1)
						flag1=checkd(i,1);
				}
				else if(map[1][i]=='O')
				{
					if(!flag2)
						flag2=checkd(i,0);
				}
			}
		}
		bool Find=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(map[i][j]=='.')
					Find=1;
		printf("Case #%d: ",ncase++);
		if((flag1==1&&flag2==1)||(!flag1&&!flag2&&Find==0))
			puts("Draw");
		else if(flag1==1)
			puts("X won");
		else if(flag2==1)
			puts("O won");
		else
			puts("Game has not completed");
	}
	return 0;
}
