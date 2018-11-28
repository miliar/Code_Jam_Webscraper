#include<cstdio>
using namespace std;
int dot;
int check_row(char s[4][5])
{
	int ans=0,i,j,c=0;
	char cur=' ';
	for(i=0;i<4;i++)
	{
		cur=' ';
		c=0;
		for(j=0;j<4;j++)
		{
			if(s[i][j]=='T')
				c++;
			else if(s[i][j]=='.')
				dot++;
			else if(cur==' ')
			{
				cur=s[i][j];
				c++;
			}
			else if(s[i][j]==cur)
				c++;
		}
		if(c==4)
		{
			if(cur=='X')
				return 1;
			else
				return 2;
			break;
		}
	}
	return 0;
}
int check_col(char s[4][5])
{
	int ans=0,i,j,c=0;
	char cur=' ';
	for(i=0;i<4;i++)
	{
		c=0;
		cur=' ';
		for(j=0;j<4;j++)
		{
			if(s[j][i]=='T')
				c++;
			else if(s[j][i]=='.')
				dot++;
			else if(cur==' ')
			{
				cur=s[j][i];
				c++;
			}
			else if(s[j][i]==cur)
				c++;
		}
		if(c==4)
		{
			if(cur=='X')
				return 1;
			else
				return 2;
			break;
		}
	}
	return 0;
}
int check_dia(char s[4][5])
{
	char cur=' ';
	int c=0,j;
	for(j=0;j<4;j++)
	{
		if(s[j][j]=='T')
			c++;
		else if(s[j][j]=='.')
				dot++;
		else if(cur==' ')
		{
			cur=s[j][j];
			c++;
		}
		else if(s[j][j]==cur)
			c++;
	}
	if(c==4)
	{
		if(cur=='X')
			return 1;
		else
			return 2;
	}
	c=0;
	cur=' ';
	for(j=0;j<4;j++)
	{
		if(s[j][3-j]=='T')
			c++;
		else if(s[j][3-j]=='.')
			dot++;
		else if(cur==' ')
		{
			cur=s[j][3-j];
			c++;
		}
		else if(s[j][3-j]==cur)
			c++;
	}
	if(c==4)
	{
		if(cur=='X')
			return 1;
		else
			return 2;
	}
	return 0;
}
int main()
{
	int t,i,ans,j;
	char s[4][5];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		for(j=0;j<4;j++)
			scanf("%s",s[j]);
		dot=0;
		ans=check_row(s);
		if(!ans)
			ans=check_col(s);
		if(!ans)
			ans=check_dia(s);
		if(!ans&&dot)
			printf("Case #%d: Game has not completed\n",i);
		else if(!ans)
			printf("Case #%d: Draw\n",i);
		else if(ans==1)
			printf("Case #%d: X won\n",i);
		else
			printf("Case #%d: O won\n",i);
	}
	return 0;
}
