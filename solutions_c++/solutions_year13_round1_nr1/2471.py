#include <iostream>
#include <stdio.h>
using namespace std;
long long r,t;
int T;
int main()
{
	int co=0;
	scanf("%d",&T);
	while(T--)
	{
		co++;
		printf("Case #%d: ",co);
		scanf("%lld%lld",&r,&t);
		long long ans=0;
		while(t>=2*r+1ll)
		{
			t-=2*r+1ll;
			r+=2l;
			ans++;
		}
		printf("%lld\n",ans);
	}
	return 0;
}
