#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iostream>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		printf("Case #%u:\n",t);
		uint R,N,M,K;
		scanf("%u%u%u%u",&R,&N,&M,&K);
		for(uint r=0; r<R; ++r)
		{
			uint p[16];
			uint c[16];
			uint h[10]={};
			for(uint i=0; i<K; ++i)
				scanf("%u",&p[i]);

			for(uint i=0; i<K; ++i)
			{
				uint q=p[i];
				for(uint n=2; n<10; ++n)
				{
					uint e=0;
					while(q%n==0)
					{
						++e;
						q/=n;
					}
					h[n]=std::max(e,h[n]);
				}
			}
			uint k=0;
			for(uint i=0; i<h[3]; ++i)
				c[k++]=3;
			for(uint i=0; i<h[5]; ++i)
				c[k++]=5;
			if(k<3)
			{
				while(k<3 && (3-k)*1<h[2])
				{
					c[k++]=4;
					h[2]-=2;
				}
				while(k<3)
					c[k++]=2;
			}

			for(uint i=0; i<N; ++i)
				printf("%u",c[i]);
			printf("\n");
		}
	}
}
