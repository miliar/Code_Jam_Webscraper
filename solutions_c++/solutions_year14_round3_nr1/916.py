#include <cstdio>

typedef unsigned usd;
typedef unsigned long long ull;

ull p,q,s,g;
usd T,n;

ull gcd(ull a,ull b)
{
	for (ull c;b;c=a%b,a=b,b=c);
	return a;
}
int main()
{
	freopen("output","w",stdout);
	scanf("%u",&T);
	for (usd t=1;t<=T;++t)
	{
		scanf("%llu/%llu",&p,&q);
		g=gcd(p,q);
		p/=g;
		q/=g;
		for (s=q;!(s&1);s>>=1);
		printf("Case #%u: ",t);
		if (s==1)
		{
			n=0;
			while (p<q) p<<=1,++n;
			printf("%u\n",n);
		}
		else puts("impossible");
	}
	return 0;
}