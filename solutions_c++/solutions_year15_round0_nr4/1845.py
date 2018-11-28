#include<stdio.h>
int main()
{
	freopen("cook.txt","r",stdin);
	freopen("bro.txt","w",stdout);
	long long int t,x,i,r,c,ans[5][5][5],j,k;
	scanf("%lld",&t);
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		ans[1][i][j]=1;
	}
	ans[2][1][1]=0;
	ans[2][1][2]=1;
	ans[2][1][3]=0;
	ans[2][1][4]=1;
	ans[2][2][1]=1;
	ans[2][2][2]=1;
	ans[2][2][3]=1;
	ans[2][2][4]=1;
	ans[2][3][1]=0;
	ans[2][3][2]=1;
	ans[2][3][3]=0;
	ans[2][3][4]=1;
	ans[2][4][1]=1;
	ans[2][4][2]=1;
	ans[2][4][3]=1;
	ans[2][4][4]=1;
	
	ans[3][1][1]=0;
	ans[3][1][2]=0;
	ans[3][1][3]=0;
	ans[3][1][4]=0;
	ans[3][2][1]=0;
	ans[3][2][2]=0;
	ans[3][2][3]=1;
	ans[3][2][4]=0;
	ans[3][3][1]=0;
	ans[3][3][2]=1;
	ans[3][3][3]=1;
	ans[3][3][4]=1;
	ans[3][4][1]=0;
	ans[3][4][2]=0;
	ans[3][4][3]=1;
	ans[3][4][4]=0;
	
	ans[4][1][1]=0;
	ans[4][1][2]=0;
	ans[4][1][3]=0;
	ans[4][1][4]=0;
	ans[4][2][1]=0;
	ans[4][2][2]=0;
	ans[4][2][3]=0;
	ans[4][2][4]=0;
	ans[4][3][1]=0;
	ans[4][3][2]=0;
	ans[4][3][3]=0;
	ans[4][3][4]=1;
	ans[4][4][1]=0;
	ans[4][4][2]=0;
	ans[4][4][3]=1;
	ans[4][4][4]=1;
	for(i=1;i<=t;i++)
	{
		scanf("%lld%lld%lld",&x,&r,&c);
		if(ans[x][r][c]==1)
		{
			printf("Case #%lld: GABRIEL\n",i);
		}
		else
		{
		   printf("Case #%lld: RICHARD\n",i);
	    }
	}
	return 0;
}
