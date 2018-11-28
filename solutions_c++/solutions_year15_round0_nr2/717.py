#include <cstdio>
#include <algorithm>
#include <vector>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		scanf("%u",&N);
		std::vector<uint> p(N);
		for(uint i=0; i<N; ++i)
			scanf("%u",&p[i]);
		uint mp=*std::max_element(p.begin(),p.end());
		uint r=mp;
		for(uint m=1; m<mp; ++m)
		{
			uint tm=m;
			for(uint i=0; i<N; ++i)
				tm+=(p[i]+m-1)/m-1;
			r=std::min(r,tm);
		}
		printf("Case #%u: %u\n",t,r);
	}
}
