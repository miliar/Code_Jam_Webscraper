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

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		ull N=0;
		scanf("%llu",&N);
		std::vector<uint> A(N+1);
		for(uint n=0; n<=N; ++n)
			A[n]=n;
		for(uint n=0; n<=N; ++n)
		{
			ull v=0;
			for(ull q=n; 0<q; q/=10)
				v=v*10+q%10;
			ull s=A[n]+1;
			if(n+1<=N && s<A[n+1])
				A[n+1]=s;
			if(v<=N && s<A[v])
				A[v]=s;
		}

		ull r=A[N];
		printf("Case #%u: %llu\n",t,r);
	}
}
