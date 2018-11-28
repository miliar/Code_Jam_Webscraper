#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
using namespace std;
int find(char ch[5][5])
{
	int xx=0,oo=0;
	for(int j=0;j<4;j++)
	{
		for(int i=0;i<4;i++)
		{
			if(ch[j][i]=='X')
			{xx++;}
			if(ch[j][i]=='O')
			{oo++;}
		}
		if(xx==4) return 1;
		if(oo==4) return 2;
		xx=0;oo=0;
	}
	xx=0;oo=0;
	for(int j=0;j<4;j++)
	{
		for(int i=0;i<4;i++)
		{
			if(ch[i][j]=='X')
			{xx++;}
			if(ch[i][j]=='O')
			{oo++;}
		}
		if(xx==4) return 1;
		if(oo==4) return 2;
		xx=0;oo=0;
	}
	
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(ch[i][i]=='X')
		{xx++;}
		if(ch[i][i]=='O')
		{oo++;}
		if(xx==4) return 1;
		if(oo==4) return 2;
	}
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(ch[i][3-i]=='X')
		{xx++;}
		if(ch[i][3-i]=='O')
		{oo++;}
		if(xx==4) return 1;
		if(oo==4) return 2;
	}
	return 0;
}
int main()
{
    int i,j,k;
    int n,m,t;
    char ch[5][5];
    freopen("A-large.in","r",stdin);freopen("output.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
		for(i=0;i<4;i++)
		{scanf("%s",ch[i]);}
		int x=-1,y=-1,flag=0;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(ch[i][j]=='T')
			{x=i;y=j;}
			if(ch[i][j]=='.')
			{flag=1;}
		}
		int ans=0;
		if(x==-1)
		{
			ans=find(ch);
		}
		else
		{
			ch[x][y]='X';
			int ans1=find(ch);
			ch[x][y]='O';
			int ans2=find(ch);
			ans=max(ans1,ans2);
		}
		if(ans==0&&flag==1)
		{printf("Case #%d: Game has not completed\n",tcase);}
		else if(ans==0)
		{printf("Case #%d: Draw\n",tcase);}
		else if(ans==1)
		{printf("Case #%d: X won\n",tcase);}
		else
		{printf("Case #%d: O won\n",tcase);}
	}
}
