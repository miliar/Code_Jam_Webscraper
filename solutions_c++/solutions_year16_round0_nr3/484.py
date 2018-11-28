#include <cstdio>
#include <vector>
typedef unsigned int uint;

main()
{
	uint const P=4;
	uint const primes[P]={2,3,5,7};
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,K=0;
		scanf("%u%u",&N,&K);
		printf("Case #%u:\n",t);
		uint k=0;
		for(uint n2=(1u<<(N-1))+1; k<K; n2+=2)
		{
			uint d[32]={};
			for(uint q=n2,i=0; 0<q; ++i,q/=2)
				d[i]=q%2;

			uint fp[11];
			bool ok=1;
			for(uint b=2; ok && b<=10; ++b)
			{
				bool composite=0;
				for(uint i=0; !composite && i<P; ++i)
				{
					uint p=primes[i];
					uint m=0;
					for(uint j=N; j--;)
						m=(m*b+d[j])%p;
					if(m==0)
					{
						composite=1;
						fp[b]=p;
					}
				}
				ok=composite;
			}
			if(ok)
			{
				for(uint i=N; i--;)
					printf("%u",d[i]);
				for(uint b=2; b<=10; ++b)
					printf(" %u",fp[b]);
				printf("\n");
				++k;
			}
		}
	}
}
