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
typedef long long int ll;
typedef std::vector<int> vi;
typedef std::vector<uint> vu;
template <typename T> void sort(std::vector<T> &x) { std::sort(x.begin(),x.end()); }
uint const mod=1000002013;

struct wat
{
	wat() {}
	wat(uint _p,int _d): p(_p),d(_d),s(0) {}
	bool operator< (wat const &rhs) const
	{
		if(p!=rhs.p)
			return p<rhs.p;
		return d<rhs.d;
	}
	uint p;
	int d;
	ll s;
};

uint cost(uint N,uint d,uint p)
{
	uint c=(ull(d)*N-ull(d)*(d-1)/2)%mod;
	uint r=ull(c)*p%mod;
	return r;
}

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,M=0;
		scanf("%u%u",&N,&M);
		std::map<uint,uint> s;
		uint c0=0;
		for(uint i=0; i<M; ++i)
		{
			uint o,e,p;
			scanf("%u%u%u",&o,&e,&p);
			s[o]=(s[o]+p)%mod;
			s[e]=(s[e]+mod-p)%mod;
			c0=(c0+cost(N,e-o,p))%mod;
		}
		uint sum=0;
		for(std::map<uint,uint>::iterator i=s.begin(); i!=s.end(); ++i)
		{
			sum=(sum+(*i).second)%mod;
			(*i).second=sum;
		}

		uint c1=0;
		for(std::map<uint,uint>::iterator b=s.begin(); b!=s.end();++b)
			if(0<(*b).second)
			{
				uint p=(*b).second;
				(*b).second=0;
				std::map<uint,uint>::iterator e=b;
				++e;
				for(; e!=s.end(); ++e)
					if(p<=(*e).second)
						(*e).second-=p;
					else
					{
						uint off=p-(*e).second;
						uint co=cost(N,(*e).first-(*b).first,off);
						c1=(c1+co)%mod;
						p=(*e).second;
						(*e).second=0;
					}
			}

		uint r=(c0+mod-c1)%mod;
		printf("Case #%u: %u\n",t,r);
	}
}
