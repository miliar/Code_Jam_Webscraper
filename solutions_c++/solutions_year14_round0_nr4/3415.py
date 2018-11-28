#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	long long int t;
	scanf("%lld",&t);
	long long int cases=1;
	while(t--)
	{
		long double a[10000]={},b[10000]={},c[10000]={},d[10000]={};
		long long int wina=0;
		long long int winb=0;
		long long int n;
		scanf("%lld",&n);
		for(long long int i=0;i<n;i++)
		{
			scanf("%llf",&a[i]);
		}
		for(long long int i=0;i<n;i++)
		{
			scanf("%llf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		for(long long int i=0;i<n;i++)
		{
			c[i]=a[i];
			d[i]=b[i];
		}
		for(long long int i=0;i<n;i++)
		{
			for(long long int j=0;j<n;j++)
			{
				if(b[j]>a[i])
				{
					winb++;
					a[i]=-1;
					b[j]=-1;
					break;
				}
			}
		}
		for(long long int i=0;i<n;i++)
		{
			for(long long int j=0;j<n;j++)
			{
				if(c[j]>d[i]&&c[j]!=-1)
				{
					wina++;
					c[j]=-1;
					break;
				}
			}
		}
		printf("Case #%lld: %lld %lld\n",cases,wina,(n-winb));
		cases++;
	}
}
