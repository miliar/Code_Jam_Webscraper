#include<stdio.h>
int i,a,b,c,t;
int block[4][4][4]=
{
	{
		{1,1,1,1},
		{1,1,1,1},
		{1,1,1,1},
		{1,1,1,1},
	},
	{
		{0,1,0,1},
		{1,1,1,1},
		{0,1,0,1},
		{1,1,1,1},
	},
	{
		{0,0,0,0},
		{0,0,1,0},
		{0,1,1,1},
		{0,0,1,0},
	},
	{
		{0,0,0,0},
		{0,0,0,0},
		{0,0,0,1},
		{0,0,1,1}
	}
};
int main()
{
	freopen("asdf.txt","r",stdin);
	freopen("outputasdf.txt","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{ 
		scanf("%d%d%d",&a,&b,&c);
		printf("Case #%d: %s\n",i,block[a-1][b-1][c-1]?"GABRIEL":"RICHARD");
	}
}
