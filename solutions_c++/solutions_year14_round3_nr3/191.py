#include <cstdio>
typedef unsigned int uint;

uint X=0,Y=0,K=0;
uint grid[32][32]={};

void wat(uint x, uint y)
{
	if(grid[y][x]!=0)
		return;
	grid[y][x]=3;
	if(0<x)
		wat(x-1,y);
	if(x+1<X)
		wat(x+1,y);
	if(0<y)
		wat(x,y-1);
	if(y+1<Y)
		wat(x,y+1);
}

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		X=0;Y=0;K=0;
		scanf("%u%u%u",&X,&Y,&K);

		// brútforsz béjbi
		uint r=X*Y;
		for(uint m=1<<(X*Y); m--;)
		{
			uint n=0;
			for(uint y=0,o=0; y<Y; ++y)
				for(uint x=0; x<X; ++x,++o)
				{
					uint stone=(m>>o)&1;
					grid[y][x]=stone;
					n+=stone;
				}
			for(uint x=0; x<X; ++x)
			{
				wat(x,0);
				wat(x,Y-1);
			}
			for(uint y=0; y<Y; ++y)
			{
				wat(0,y);
				wat(X-1,y);
			}
			uint k=0;
			for(uint y=0; y<Y; ++y)
				for(uint x=0; x<X; ++x)
					k+=grid[y][x]<3;
			if(K<=k && n<r)
				r=n;
		}
		printf("Case #%u: %u\n",t,r);
	}
}
