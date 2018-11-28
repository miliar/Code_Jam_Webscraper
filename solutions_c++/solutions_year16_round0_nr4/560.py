#include <cstdio>
#include <algorithm>
typedef unsigned int uint;
typedef unsigned long long int ull;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint K=0,C=0,S=0;
		scanf("%u%u%u",&K,&C,&S);
		uint r=0;
		printf("Case #%u:",t);
		if(S*C<K)
			printf(" IMPOSSIBLE");
		else
		{
			for(uint s=0; s*C<K; ++s)
			{
				ull n=0;
				for(uint i=0; i<C; ++i)
					n=n*K+std::min(K-1,s*C+i);
				printf(" %llu",n+1);
			}
		}
		printf("\n");
	}
}
