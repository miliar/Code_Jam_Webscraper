#include<cstdio>
int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("Output2A.out","w",stdout);
	int t,i,j,n;
	long long ans,max;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d",&n);
		int a[n];
		for (j=0;j<n;j++)
			scanf("%d",&a[j]);
		max=ans=0;
		for (j=0;j<n-1;j++)
		{
			if (a[j]>a[j+1])
				ans+=a[j]-a[j+1];
			if (max<a[j]-a[j+1])
				max=a[j]-a[j+1];
		}
		printf("Case #%d: %lld ",i,ans);
		ans=0;
		for (j=0;j<n-1;j++)
		{
			if (a[j]<=max)
				ans+=a[j];
			else
				ans+=max;
		}
		printf("%lld\n",ans);
	}
	return 0;
}
