// http://web.archive.org/web/20020614225321/http://www.geocities.com/williamrexmarshall/math/palsq.html
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <gmpxx.h>
typedef mpz_class mpz;
typedef unsigned int uint;
typedef std::vector<mpz> vz;
template <typename T> void sort(std::vector<T> &x) { std::sort(x.begin(),x.end()); }

vz S;

uint const N=100; // <=100
mpz root;
mpz e10[64];

void check()
{
	mpz q=root*root;
	uint l=0;
	uint d[128];
	for(mpz u=q; 0<u; u/=10)
	{
		mpz a=u%10;
		d[l++]=a.get_si();
	}
	bool ok=1;
	for(uint i=0; ok && 2*i<l; ++i)
		ok=d[i]==d[l-1-i];
	if(ok)
		S.push_back(q);
}

void gen_br(uint l,uint n=6,uint i=1)
{
	if(2*i<l && 2<=n)
	{
		gen_br(l,n,i+1);
		mpz d=e10[i]+e10[l-i-1];
		root+=d;
		gen_br(l,n-2,i+1);
		root-=d;
	}
	else check();
}

void gen_tr(uint l,uint n,uint i=1)
{
	if(2*i+1<l && 2<=n)
	{
		gen_tr(l,n,i+1);
		mpz d=e10[i]+e10[l-i-1];
		root+=d;
		gen_tr(l,n-2,i+1);
		root-=d;
	}
	else check();
}

int main()
{
	S.push_back(1);
	S.push_back(4);
	S.push_back(9);

	{
		mpz z=1;
		for(uint n=0; n<64; ++n,z*=10)
			e10[n]=z;
	}

	// binary roots
	for(uint l=2; l<=N/2; l+=2)
	{
		root=e10[l-1]+e10[0];
		gen_br(l);
	}

	// ternary roots
	for(uint l=3; l<=N/2; l+=2)
	{
		for(uint y=0; y<=2; ++y)
		{
			root=e10[l-1]+y*e10[l/2]+e10[0];
			gen_tr(l,y<2?6:2);
		}
	}

	// even roots
	for(uint l=2; l<=N/2; ++l)
	{
		root=2*e10[l-1]+2*e10[0];
		check();
	}
	for(uint l=3; l<=N/2; l+=2)
	{
		root=2*e10[l-1]+e10[l/2]+2*e10[0];
		check();
	}

	sort(S);
	/*for(size_t i=0; i<S.size(); ++i)
		std::cout << sqrt(S[i]) << " " << S[i] << std::endl;
	return 1;*/

	uint T=0;
	scanf("%u\n", &T);
	for(uint t=1; t<=T; ++t)
	{
		mpz A,B;
		std::cin >> A >> B;
		bool noway=1;
		assert(1<=A && A<=B && noway);
		uint r=std::upper_bound(S.begin(),S.end(),B)-std::lower_bound(S.begin(),S.end(),A);
		printf("Case #%u: %u\n",t,r); 
	}
	return 0;
}
