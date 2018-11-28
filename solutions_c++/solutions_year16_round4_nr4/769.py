#include<stdio.h>

int n,map[50][50],ans[50][50],ans2,re[50],check[50],check2[50];

void test(void)
{
	int i,j,k,x=0,y,z;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			ans[i][j]=re[++x];
	}
	x=0;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(map[i][j]==1 && ans[i][j]!=1)
				return;
			else if(map[i][j]==0 && ans[i][j]==1)
				x++;
		}
	}

	for(i=1;i<=n;i++)
		check[i]=check2[i]=0;

	for(i=1;i<=n;i++)
	{
		if(check[i]==1)
			continue;
		y=0;
		z=0;
		for(j=1;j<=n;j++)
		{
			y+=ans[i][j];
			if(ans[i][j]==1 && check2[j]==1)
				return;
		}
		for(k=1;k<=n;k++)
		{
			for(j=1;j<=n;j++)
			{
				if(ans[i][j]!=ans[k][j])
					break;
			}
			if(j==n+1)
				z++;
		}
		if(y==0 || y!=z)
			return;

		for(j=1;j<=n;j++)
		{
			if(ans[i][j]==1)
				check2[j]=1;
		}
		for(k=1;k<=n;k++)
		{
			for(j=1;j<=n;j++)
			{
				if(ans[i][j]!=ans[k][j])
					break;
			}
			if(j==n+1)
				check[k]=1;
		}
	}

	if(ans2>x)
		ans2=x;
}

void recall(int lev)
{
	if(lev>n*n)
	{
		test();
		return;
	}
	re[lev]=0;
	recall(lev+1);
	re[lev]=1;
	recall(lev+1);
}

int main(void)
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int t,i,j,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		ans2=0x7fffffff;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				scanf("%1d",&map[i][j]);
		}
		recall(1);
		printf("Case #%d: %d\n",k,ans2);
	}
}