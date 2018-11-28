#include <cstdio>
typedef unsigned int uint;
typedef unsigned long long int ull;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint A=0,B=0,K=0;
		scanf("%u%u%u",&A,&B,&K);
		ull r=0;
		for(uint a=0; a<A; ++a)
			for(uint b=0; b<B; ++b)
				r+=(a&b)<K;
		printf("Case #%u: %llu\n",t,r);
	}
}
