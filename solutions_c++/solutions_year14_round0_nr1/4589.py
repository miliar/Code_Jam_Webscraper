#include <cstdio>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint a=0;
		scanf("%u",&a);
		--a;
		uint A[4][4];
		for(uint i=0; i<4; ++i)
			for(uint j=0; j<4; ++j)
				scanf("%u",&A[i][j]);
		uint b=0;
		scanf("%u",&b);
		--b;
		uint B[4][4];
		for(uint i=0; i<4; ++i)
			for(uint j=0; j<4; ++j)
				scanf("%u",&B[i][j]);
		uint c[32]={};
		for(uint i=0; i<4; ++i)
			++c[A[a][i]];
		uint n2=0,r=0;
		for(uint i=0; i<4; ++i)
			if(++c[B[b][i]]==2)
			{
				++n2;
				r=B[b][i];
			}

		printf("Case #%u: ",t);
		if(n2==0)
			printf("Volunteer cheated!\n");
		else if(n2==1)
			printf("%u\n",r);
		else printf("Bad magician!\n");
	}
}
