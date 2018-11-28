#include <stdio.h>
long long int a[100010],b[100010];
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int t,rsv,lol,x,r,c,n,i,sum;
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		scanf("%lld",&a[i]);
		sum=0;rsv=a[0];
		for(i=1;i<n;i++)
		{
			if(a[i]<rsv)
			sum+=rsv-a[i];
			rsv=a[i];
		}
		for(i=0;i<n-1;i++)
		{
			b[i]=a[i]-a[i+1];
		}
		rsv=b[0];
		for(i=1;i<n-1;i++)
		{
			if(b[i]>rsv)
			rsv=b[i];
		}
		x=0;
		for(i=0;i<n-1;i++)
		{
			if(a[i]>rsv)
			x+=rsv;
			else
			x+=a[i];
		}
		printf("Case #%lld: %lld %lld\n",lol,sum,x);
	}
	
}
