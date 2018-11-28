#include <cstdio>
#include <algorithm>
typedef unsigned int uint;

char map[64][64];

bool rect(uint n, uint m)
{
	for(uint i=0; i<n; ++i)
		for(uint j=0; j<m; ++j)
			map[i][j]='.';
	return true;
}

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,M=0,X=0;
		scanf("%u%u%u",&N,&M,&X);
		bool rot=M<N;
		if(rot)
			std::swap(N,M);
		uint E=N*M-X;
		for(uint i=0; i<N; ++i)
			for(uint j=0; j<M; ++j)
				map[i][j]='*';
		bool ok=0;
		if(E==1)
			ok=1;
		else if(N==1)
			ok=rect(1,E);
		else
		{
			for(uint n=2; !ok && n<=N; ++n)
				for(uint m=2; !ok && m<=M; ++m)
				{
					uint r=n*m;
					if(r<E)
						continue;
					if(r==E)
						ok=rect(n,m);
					else if(2<n && 2<m)
					{
						uint br=n+m-1;
						uint u=br-2-2;
						uint s=r-E;
						if(u<s)
							continue;
						ok=rect(n,m);
						for(uint i=m-1; 0<s && 2<=i; --i,--s)
							map[n-1][i]='*';
						for(uint i=n-2; 0<s && 2<=i; --i,--s)
							map[i][m-1]='*';
					}
				}
		}
		map[0][0]='c';
		printf("Case #%u:\n",t);
		if(ok)
		{
			for(uint i=0; i<(rot?M:N); ++i)
			{
				for(uint j=0; j<(rot?N:M); ++j)
					printf("%c",(rot?map[j][i]:map[i][j]));
				printf("\n");
			}
		}
		else printf("Impossible\n");
	}
}
