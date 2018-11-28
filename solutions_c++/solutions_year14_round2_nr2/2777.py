#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;
int main()
{
	int t,c=1,i,j;
	ll ans=0,A,B,K;
	scanf("%d",&t);
	while(c<=t)
	{
		scanf("%lld",&A);
		scanf("%lld",&B);
		scanf("%lld",&K);
		ans=0;
		for (i = 0; i < A; ++i)
		{
			for (j = 0; j < B; ++j)
			{
				if((i&j)<K)
					ans++;
			}
		}
		printf("Case #%d: %lld\n",c,ans);
		c++;
	}
	return 0;
}
