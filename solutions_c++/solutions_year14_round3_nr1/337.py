#include <cstdio>
#include <algorithm>
typedef unsigned int uint;
typedef unsigned long long int ull;

ull gcd(ull a, ull b)
{
	while(b)
	{
		ull r=a%b;
		a=b;
		b=r;
	}
	return a;
}

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		ull P=0,Q=0;
		scanf("%llu/%llu",&P,&Q);
		ull g=gcd(P,Q);
		ull p=P/g,q=Q/g;

		printf("Case #%u: ",t);
		ull n=q;
		while(0<n && n%2==0)
			n/=2;
		if(n==1)
		{
			uint r=0;
			while(p<q)
			{
				p*=2;
				++r;
			}
			printf("%u",r);
		}
		else printf("impossible");
		printf("\n");
	}
}
