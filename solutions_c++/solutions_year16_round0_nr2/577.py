#include <cstdio>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		char S[128];
		scanf("%s",S);
		uint k=1;
		uint N=1;
		for(; S[N]; ++N)
			k+=S[N]!=S[N-1];
		bool lp=S[N-1]=='+';
		uint r=k-1+!lp;
		printf("Case #%u: %u\n",t,r);
	}
}
