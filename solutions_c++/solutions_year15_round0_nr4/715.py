#include <cstdio>
#include <algorithm>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint X=0,R=0,C=0;
		scanf("%u%u%u",&X,&R,&C);
		if(C<R)
			std::swap(R,C);
		bool r=false;
		if(R*C%X!=0)
			r=true; // grid area not divisible by X
		else if(X==1)
			r=false;
		else if(X==2)
			r=false;
		else if(X==3)
		{
			if(R==1)
				r=true; // 2x2 L
			else r=false;
		}
		else if(X==4)
		{
			if(R==1)
				r=true; // L
			else if(R==2)
				r=true; // Z
			else r=false;
		}
		else if(X==5)
		{
			if(R<=2)
				r=true; // 3x3 L
			else if(R==3)
				r=true; // staircase
			else r=false;
		}
		else if(X==6)
		{
			if(R<=2)
				r=true; // 3x4 L
			else if(R==3)
				r=true; // cross
			else r=false;
		}
		else if(7<=X)
			r=true; // hole
		printf("Case #%u: %s\n",t,(r?"RICHARD":"GABRIEL"));
	}
}
