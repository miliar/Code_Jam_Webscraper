#include<stdio.h>

int main()
{
	int T;
	scanf("%d",&T);
	int c=1;
	while(c<=T)
	{
		bool flag=0;
		int n,m;
		scanf("%d%d",&n,&m);
		int a[101][101];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		int mr[101],mc[101];
		for(int i=0;i<n;i++)
		{
			int max=-1;
			for(int j=0;j<m;j++)
			{
				if(a[i][j]>max) max=a[i][j];
			}
			mr[i]=max;
		}
		for(int j=0;j<m;j++)
		{
			int max=-1;
			for(int i=0;i<n;i++)
			{
				if(a[i][j]>max) max=a[i][j];
			}
			mc[j]=max;
		}

		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(a[i][j]<mr[i]&&a[i][j]<mc[j]) flag=1;
			}
		}
		printf("Case #%d: %s\n",c,flag?"NO":"YES");
		c++;
	}
	return 0;
}