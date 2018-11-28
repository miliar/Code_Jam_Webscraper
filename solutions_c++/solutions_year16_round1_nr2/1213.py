#include <cstdio>
#include <vector>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		scanf("%u",&N);
		std::vector<uint> c(2501,0);
		for(uint i=0; i<(2*N-1)*N; ++i)
		{
			uint a=0;
			scanf("%u",&a);
			++c[a];
		}
		
		printf("Case #%u:",t);
		for(uint i=1; i<=2500; ++i)
			if(c[i]%2)
				printf(" %u",i);
		printf("\n");
	}
}
