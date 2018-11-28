#include<stdio.h>
#include<iostream>
using namespace std;
long long ans1,ans2;
long long f(int xx)
{
	return (long long)(1<<(xx/2))*(1<<(xx-xx/2));
}
main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,n;
	long long p,x,z,y;
	cin >> t;
	for(int ll=0;ll<t;ll++)
	{
		scanf("%d %lld",&n,&p);
		x=f(n);
		z=x;
		//cout << x << endl;
		for(int i=0;i<=n;i++)
		{
			y=f(n-i);
			if(p>=z-y+1)
			{
				ans1=f(i+1)-2;
			}
		}
		ans1=min(ans1,z-1);
		for(int i=n;i>=0;i--)
		{
			y=f(n-i);
			if(p>=y)
			{
				ans2=z-f(i);
			}
		}
		printf("Case #%d: ",ll+1);
		printf("%lld %lld\n",ans1,ans2);
	}
	
}
