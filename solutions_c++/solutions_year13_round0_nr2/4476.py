#include<stdio.h>
int n,m,a[100][100];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,test,i,j,minh;
	scanf("%d",&test);
	for(T=1;T<=test;T++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
			}
		}

		while(n>0 && m>0)
		{
			minh=200;
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
				{
					if(a[i][j]<minh)
						minh=a[i][j];
				}
			}
			for(i=0;i<n;i++)
			{
				for(j=0;j<m;j++)
					if(a[i][j]!=minh)
						break;
				if(j==m)
					break;
			}
			if(i<n)
			{
				for(i=i+1;i<n;i++)
					for(j=0;j<m;j++)
						a[i-1][j]=a[i][j];
				n--;
				continue;
			}
			for(i=0;i<m;i++)
			{
				for(j=0;j<n;j++)
					if(a[j][i]!=minh)
						break;
				if(j==n)
					break;
			}
			if(i<m)
			{
				for(i=i+1;i<m;i++)
					for(j=0;j<n;j++)
						a[j][i-1]=a[j][i];
				m--;
				continue;
			}
			break;
		}
		printf("Case #%d: ",T);
		if(n==0 || m==0)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}