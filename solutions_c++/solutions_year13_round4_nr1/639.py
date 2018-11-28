#include"stdio.h"
#include"vector"
#include"set"
#include"map"
#include"assert.h"
#include"algorithm"
#include"math.h"
#include"stdlib.h"
#include"string.h"
#include"string"
using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef const int& ci;
typedef const unsigned int& cui;
typedef const long long& cll;
typedef const unsigned long long& cull;
#define aut(x,y) typeof(y) x = y
#define REP(i,n) for(unsigned int i=0;i<(n);i++)
#define LOOP(i,x,n) for(int i=(x);i<(n);i++)
#define ALL(v) v.begin(),v.end()
#define FOREACH(it,v)   for(typeof((v).begin()) it=(v).begin();it != (v).end();it++)
#define i(x) scanf("%d",&x)
#define u(x) scanf("%u",&x)
#define l(x) scanf("%lld",&x)
#define ul(x) scanf("%llu",&x)
#define MOD 1000002013
ll n;
ll cost(ll d, ll p) {
  return (((n*d-d*(d+1)/2)%MOD)*(p%MOD))%MOD;
}
int solve() {
	map<int, long long> m;
	int  M;
	l(n), i(M);
	ll best=0, worst=0;
	while(M--) {
		int o, e, p;
		i(o), i(e), i(p);
		m[o]+=p;
		m[e]-=p;
		best= (best + cost(e-o, p))%MOD;
	}
	map<int, ll> ct;
	FOREACH(it, m){
		ll p = it->second, s = it->first;
		if(p==0)continue;
		if(p>0)	ct[s] += p;
		else {
			p  = -p;
			for(aut(it2, ct.rbegin()); it2!=ct.rend(); it2++)
				if(p>0) {
					ll pp = min(p, it2->second);
					p -= pp;
					it2->second -= pp;
					worst=(worst+cost(s-it2->first, pp))%MOD;
				}else break;
			assert(p==0);
		}
	}
	//printf("-- %Ld %Ld\n", best, worst);
	return (best%MOD - worst%MOD + MOD) % MOD;
}

int main()
{
	ui T;
	u(T);
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: %d\n", 1+i, solve());
	}
}
