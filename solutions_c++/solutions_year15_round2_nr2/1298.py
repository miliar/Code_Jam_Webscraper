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

uint Y=0,X=0,N=0;
uint best=0;

void rec(uint y=0, uint lm=0, uint u=0, uint n=0)
{
	if(y<Y)
	{
		for(uint m=0; m<(1<<X); ++m)
		{
			uint dn=0;
			uint du=0;
			for(uint q=m,lq=lm; 0<q || 0<lq; q/=2,lq/=2)
			{
				du+=(q%4==3);
				du+=(q&lq&1);
				dn+=(q&1);
			}
			rec(y+1,m,u+du,n+dn);
		}
	}
	else
	{
		if(n==N && u<best)
			best=u;
	}
}

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		scanf("%u%u%u",&Y,&X,&N);
		best=2*X*Y;
		rec();
		printf("Case #%u: %u\n",t,best);
	}
}
