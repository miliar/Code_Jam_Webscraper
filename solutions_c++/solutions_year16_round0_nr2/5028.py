#include <stdio.h>
#include <string.h>
int T,t,S;
char temp[1100];

int fn[2][1000];
int f(int b, int x)
{
	if(fn[b][x] >= 0) return fn[b][x];

	if(temp[x] == '+')
	{
		if(b == 1)
			fn[b][x] = f(1,x-1) < f(0,x-1)+1 ? f(1,x-1) : f(0,x-1)+1;
		else
			fn[b][x] = f(1,x-1)+1 < f(0,x-1)+2 ? f(1,x-1)+1 : f(0,x-1)+2;
	}
	else
	{
		if(b == 0)
			fn[b][x] = f(0,x-1) < f(1,x-1)+1 ? f(0,x-1) : f(1,x-1)+1;
		else
			fn[b][x] = f(0,x-1)+1 < f(1,x-1)+2 ? f(0,x-1)+1 : f(1,x-1)+2;
	}
	return fn[b][x];
}

int solve(int x)
{
	int i,j,k;
	int d;
	int res = 0;
	
	for(i=0;i<2;i++)
		for(j=0;j<x;j++)
			fn[i][j] = -1;
		
	if(temp[0] == '+')
	{
		fn[0][0] = 1;
		fn[1][0] = 0;
	}
	else
	{
		fn[0][0] = 0;
		fn[1][0] = 1;
	}
	
	return f(1,x-1);
}


int main()
{
	int i,j,k,x;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%s",&temp);
		x = strlen(temp);
		printf("Case #%d: %d\n",t,solve(x));
		//printf("%d %s\n",S,temp);
		//printf("Case #%d: %d\n",i,solve());

	}

	//gets(temp);
	return 0;
}
