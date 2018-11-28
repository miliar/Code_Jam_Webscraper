#include<iostream>
#include<cstdio>
#include<cstdlib>
int t,n,m,a[10][10];
int check(int r,int c)
{
	int flag=0,fl=0;
	for(int i=0;i<n;i++)
	{
		if(a[i][c]!=1)
		{
			flag=1;break;
		}
	}
	if(flag==1)
	{
		for(int j=0;j<m;j++)
		{
			if(a[r][j]!=1)
			{
				fl=1;break;
			}
		}
	}
	if(fl==0)	flag=0;
	return flag;
}
int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d%d",&n,&m);
		int r[10]={0},c[10]={0};
		int fl=0;
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<m;k++)
			{
				scanf("%d",&a[j][k]);
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]==1)
				{
					fl=check(i,j);
					if(fl==1)
						break;
				}
			}
			if(fl==1)	break;
		}
		if(fl==1)
			printf("Case #%d: NO\n",tc);
		else
			printf("Case #%d: YES\n",tc);
	}
	return 0;
}