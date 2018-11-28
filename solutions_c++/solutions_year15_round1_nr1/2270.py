#include<stdio.h>
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int t,T;
	scanf("%lld",&T);
	t=1;
	while(t<=T)
	{
		long long int n,i,a[10001],result1=0,result2=0,max=0;
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&a[i]);
		}
		for(i=1;i<n;i++)
		{
			if(a[i]<a[i-1])
			{
				result1=result1+(a[i-1]-a[i]);
				if((a[i-1]-a[i])>max)
				{
					max=a[i-1]-a[i];
				}
			}
		}
		for(i=0;i<n-1;i++)
		{
			if(a[i]>max)
			{
				result2+=max;
			}
			else
			{
				result2+=a[i];
			}
		}
		printf("Case #%lld: %lld %lld\n",t,result1,result2);
		t++;
	}
}
