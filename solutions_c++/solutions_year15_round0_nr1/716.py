#include <cstdio>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		char S[1024];
		scanf("%u%s",&N,S);
		uint r=0;
		for(uint i=0,s=0; i<=N; ++i)
		{
			if(s<i)
			{
				r+=i-s;
				s=i;
			}
			s+=S[i]-'0';
		}
		printf("Case #%u: %u\n",t,r);
	}
}
