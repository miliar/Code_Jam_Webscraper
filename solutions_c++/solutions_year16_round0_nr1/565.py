#include <cassert>
#include <cstdio>
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

uint digit_mask(uint x)
{
	if(x==0)
		return 1u<<0;
	uint r=0;
	for(; 0<x; x/=10)
		r|=1u<<x%10;
	return r;
}

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		scanf("%u",&N);
		printf("Case #%u: ",t);

		if(N==0)
			printf("INSOMNIA\n");
		else
		{
			uint dm=0;
			uint const dma=(1u<<10)-1;
			uint n=0;
			while(dm!=dma)
			{
				n+=N;
				dm|=digit_mask(n);
			}
			printf("%u\n",n);
		}
	}
}
