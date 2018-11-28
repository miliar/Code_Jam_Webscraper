#include <cassert>
#include <cstdio>
#include <vector>
typedef unsigned int uint;
typedef std::vector<uint> vu;

int main()
{
	uint T=0;
	scanf("%u\n", &T);
	for(uint t=1; t<=T; ++t)
	{
		uint Y=0,X=0;
		scanf("%u%u",&Y,&X);
		assert(1<=Y && Y<=100 && 1<=X && X<=100);
		vu my(Y,0);
		vu mx(X,0);
		uint A[128][128];
		for(uint y=0; y<Y; ++y)
			for(uint x=0; x<X; ++x)
			{
				uint a=0;
				scanf("%u",&a);
				assert(1<=a && a<=100);
				A[y][x]=a;
				my[y]=std::max(my[y],a);
				mx[x]=std::max(mx[x],a);
			}
		bool ok=1;
		for(uint y=0; ok && y<Y; ++y)
			for(uint x=0; ok && x<X; ++x)
				ok=my[y]<=A[y][x] || mx[x]<=A[y][x];
		printf("Case #%u: %s\n",t,(ok?"YES":"NO"));
	}
	return 0;
}

