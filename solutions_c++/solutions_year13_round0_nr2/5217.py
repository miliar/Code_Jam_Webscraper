#include <stdio.h>
int line[250],a[111][111];
int main()
{
	int t,i,j,flag,test=0,m,n;
//	freopen("B-large.in","r",stdin);
//	freopen("2l.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n+m;i++)
			line[i]=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				if(line[i]<=a[i][j])	line[i]=a[i][j];
				if(line[j+n]<=a[i][j])	line[j+n]=a[i][j];
			}
		flag=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(a[i][j]==line[i] || a[i][j]==line[j+n])
					continue;
				flag=1;
			}
		}
		printf("Case #%d: ",++test);
		if(flag)
			puts("NO");
		else
			puts("YES");
	}

	return 0;
}