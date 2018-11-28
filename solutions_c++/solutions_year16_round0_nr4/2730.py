#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	long long t,k,c,s,i,T;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld %lld",&k,&c,&s);		
		printf("Case #%lld:",t);
		for(i=1;i<=k;i++)
			printf(" %lld",i);
		printf("\n");
	}
	return 0;
}