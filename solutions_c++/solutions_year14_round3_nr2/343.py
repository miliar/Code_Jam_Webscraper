#include <cassert>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
typedef unsigned int uint;
typedef unsigned long long int ull;
uint const M=1e9+7;


main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		scanf("%u",&N);
//		uint left[128];
//		uint right[128];
		char cars[128][128];
		for(uint i=0; i<N; ++i)
		{
			scanf("%s",cars[i]);
//			left[i]=cars[i][0]-'a';
//			uint l=strlen(cars[i]);
//			right[i]=cars[i][l-1]-'a';
		}
		uint perm[128];
		for(uint i=0; i<N; ++i)
			perm[i]=i;
		uint r=0;
		do
		{
			bool ok=1;
			uint d=1;
			uint last[32]={};
			for(uint i=0; ok && i<N; ++i)
			{
				uint k=perm[i];
				for(uint j=0; ok && cars[k][j]; ++j)
				{
					uint c=(cars[k][j]-'a')&0x1f;
					if(last[c]==0 || last[c]==d-1)
						last[c]=d;
					else ok=false;
					++d;
				}
			}
			r+=ok;
		}
		while(std::next_permutation(perm,perm+N));

		printf("Case #%u: %u\n",t,r);
	}
}
