#include <stdio.h>
#include <algorithm>
using namespace std;
long long int a[100000010];
int main()
{
	freopen( "B-small-attempt4.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,sum,rsv,lol,time,j,k,l;
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&a[i]);
		}
		sort(a,a+n);
		sum=0;j=n-1;
		rsv=a[j];
		time=rsv;
		if(a[n-1]==9&&(n==1||a[n-2]<4))
		{
			rsv=0;time=5;
		}
		else if(a[n-1]==9&&n>1&&a[n-2]==6&&(n==2||a[n-3]<4))
		{
			rsv=0;time=6;
		}
		while(rsv>3)
		{
			a[n++]=a[j]/2;
			a[j]=a[j]-a[n-1];
			sum++;
			rsv=a[0];j=0;
			for(i=1;i<n;i++)
			if(a[i]>rsv)
			{
				rsv=a[i];
				j=i;
			}
			if(sum+rsv<time)time=sum+rsv;
		}
		printf("Case #%lld: %lld\n",lol,time);
	}
}
