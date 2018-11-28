#include <cstdio>
typedef unsigned int uint;
typedef unsigned long long int ull;

struct q
{
	q(): a(), b(), c(), d() {}
	q(int _a): a(_a), b(0), c(0), d(0) {}
	q(int _a, int _b, int _c, int _d): a(_a), b(_b), c(_c), d(_d) {}
	friend q operator* (q const &l, q const &r)
	{
		return q(
			l.a*r.a - l.b*r.b - l.c*r.c - l.d*r.d,
			l.a*r.b + l.b*r.a + l.c*r.d - l.d*r.c,
			l.a*r.c - l.b*r.d + l.c*r.a + l.d*r.b,
			l.a*r.d + l.b*r.c - l.c*r.b + l.d*r.a);
	}
	friend bool operator== (q const &l, q const &r)
	{
		return l.a==r.a && l.b==r.b && l.c==r.c && l.d==r.d;
	}
	int a,b,c,d;
	static q const i,j,k;
};
q const q::i(0,1,0,0);
q const q::j(0,0,1,0);
q const q::k(0,0,0,1);

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint L=0;
		ull X=0;
		char S[10042];
		scanf("%u%llu%s",&L,&X,S);
		uint first_i=0,first_ik=0;
		q m=1;
		q s[4]={q::i,q::j,q::k};
		q pow[8];
		for(uint x=0; x<8; ++x)
		{
			pow[x]=m;
			for(uint i=0; i<L; ++i)
			{
				m=m*s[(S[i]-'i')%4];
				if(!first_i && m==q::i)
					first_i=x+1;
				if(first_i && !first_ik && m==q::k)
					first_ik=x+1;
			}
		}
		bool r=0<first_ik && first_ik<=X && pow[X%4]==-1;
		printf("Case #%u: %s\n",t,(r?"YES":"NO"));
	}
}
