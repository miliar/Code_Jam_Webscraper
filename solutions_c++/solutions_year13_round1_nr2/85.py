#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef std::vector<uint> vu;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint E,R,N;
		scanf("%u%u%u",&E,&R,&N);
		R=std::min(E,R);
		vu v(N);
		for(uint i=0; i<N; ++i)
			scanf("%u",&v[i]);
		ull r=0;
		ull e=E;
		for(uint n=0; n<N; ++n)
		{
			// find first better
			uint b=n+1;
			while(b<N && v[b]<=v[n])
				++b;
			// there is a better one
			if(b<N)
			{
				ull eb=e+ull(b-n)*R;
				// no energy lost if we wait
				if(eb<=E)
					;
				// spend some energy here and
				// have full energy at (b)
				else
				{
					// if E+e<eb, it is unreachable, we better spend it all here
					ull s=std::min(e,eb-E);
					r+=s*v[n];
					e-=s;
				}
			}
			// no better
			else
			{
				r+=ull(e)*v[n];
				e=0;
			}
			// regen
			assert(e+R<=E);
			e+=R;
		}
		printf("Case #%u: %llu\n",t,r);
	}
}
