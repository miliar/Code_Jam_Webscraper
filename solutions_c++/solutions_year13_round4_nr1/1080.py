#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define MODN 1000002013
#define MAXN 1000010000
/*
cost(k) = k(2n+1-k)/2

       |----|---------|
       o1 - e1
         o2 --------- e2
o2 = e1-k
   cost: cost(e1-o1)+cost(e2-o2)
if swap: cost(e2-o1)+cost(e1-o2)
------------------------------------
             (e1-e2)(o1-o2)

       |----|-----|---|-----|
       o1 - e1    o3 ------ e3
         o2 --------- e2

*/
long long N;
int M;

struct TMove
{
	long long o,e,p;
	bool operator<(const TMove& z) const{
		return o<z.o || (o==z.o && (e>z.e || (e==z.e && p<z.p)));
	}
};

TMove m[2001];

long long cost(long long k){
	return (k*(N*2+1-k)/2) % MODN;
}
long long cost(TMove& tm){
	return ((((tm.e-tm.o)*(2ll*N+1ll-(tm.e-tm.o))/2) % MODN) * tm.p) % MODN;
}

int main(int argc, char *argv[]) {
	freopen("A-small-attempt5.in","r",stdin);
	freopen("A-small-attempt5.out","w",stdout);
	//freopen("A-test.in","r",stdin);

	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lld%d",&N,&M);
		long long totalCost=0;
		set<TMove> s;
		map<long long, long long> mm;
		for(int i=0;i<M;i++){
			scanf("%lld%lld%lld",&m[i].o,&m[i].e,&m[i].p);
			mm[m[i].o*MAXN+m[i].e]+=m[i].p;
		}
		for(map<long long, long long>::iterator it=mm.begin();it!=mm.end();it++){
			TMove mz;
			mz.o=it->first/MAXN;
			mz.e=it->first%MAXN;
			mz.p=it->second;
			s.insert(mz);
			totalCost=(totalCost+cost(mz)) % MODN;
		}
		long long reducedCost=0;
		while(s.size()>0){
			TMove mi=*s.begin();
			s.erase(s.begin());
			if(s.size()>0){
				mm.clear();
				for(set<TMove>::iterator it=s.begin();it!=s.end();it++){
					TMove mj = *it;
					if(mj.o>mi.e || (mj.e<=mi.e)) mm[mj.o*MAXN+mj.e]+=mj.p;
					else{//mj.o<=mi.e && mj.e>mi.e
						if(mi.p>=mj.p){
							mi.p-=mj.p;
							if(mi.p) mm[mi.o*MAXN+mi.e]+=mi.p;
							swap(mj.e,mi.e);
							mi.p=mj.p;
							mm[mj.o*MAXN+mj.e]+=mj.p;;
						}else{
							mj.p-=mi.p;
							if(mj.p) mm[mj.o*MAXN+mj.e]+=mj.p;
							mj.p=mi.p;
							swap(mj.e,mi.e);
							mm[mj.o*MAXN+mj.e]+=mj.p;;
						}
					}
				}
				s.clear();
				for(map<long long, long long>::iterator it=mm.begin();it!=mm.end();it++){
					TMove mz;
					mz.o=it->first/MAXN;
					mz.e=it->first%MAXN;
					mz.p=it->second;
					s.insert(mz);
				}
			}
			reducedCost=(reducedCost+cost(mi)) % MODN;
		}
		printf("Case #%d: %lld\n",t,(totalCost+2*MODN-reducedCost)%MODN);
	}
}