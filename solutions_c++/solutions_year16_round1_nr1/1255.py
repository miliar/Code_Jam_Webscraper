#include <cstdio>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		char S[1024];
		scanf("%s",S);
		char R[2048];
		char *b=R+1024,*e=b;
		*b=0;
		for(char const *s=S; *s; ++s)
		{
			char c=*s;
			if(c<*b)
				*e++=c;
			else *--b=c;
		}
		*e=0;
		printf("Case #%u: %s\n",t,b);
	}
}
