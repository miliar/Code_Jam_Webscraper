#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
const __int64 maxn=1001;
const __int64 mod=1000002013;
__int64 o[maxn],e[maxn],p[maxn];
__int64 n,m;

void init(){
	scanf("%I64d%I64d",&n,&m);
	for (__int64 i=0;i<m;i++){
		scanf("%I64d%I64d%I64d",&o[i],&e[i],&p[i]);
	}
	return;
}

__int64 calc(){
	__int64 ans=0;
	map<__int64,__int64> hash;
	hash.clear();
	for (__int64 i=0;i<m;i++){
		__int64 tnum;
		if (hash.find(o[i])==hash.end()){
			tnum=0;
		} else {
			tnum=hash[o[i]];
		}
		tnum+=p[i];
		hash[o[i]]=tnum;
		if (hash.find(e[i])==hash.end()){
			tnum==0;
		} else {
			tnum=hash[e[i]];
		}
		tnum-=p[i];
		hash[e[i]]=tnum;
		__int64 dist=e[i]-o[i];
		ans+=((((n*dist)-((dist*dist-dist)/2))%mod)*p[i])%mod;
		ans%=mod;
		if (ans<0){
			ans+=mod;
		}
	}
	map<__int64,__int64> cnt;
	cnt.clear();
	__int64 cur=0;
	for (map<__int64,__int64>::iterator it=hash.begin();it!=hash.end();it++){
		__int64 delta=it->first-cur;
		__int64 tc=it->second;
		map<__int64,__int64> tcnt;
		tcnt.clear();
		if (tc>0){
			tcnt[0]=tc;
		}
		for (map<__int64,__int64>::iterator iter=cnt.begin();iter!=cnt.end();iter++){
			__int64 k=iter->first;
			ans-=((((delta*(n-k))-((delta*delta-delta)/2))%mod)*(iter->second%mod));
			ans%=mod;
			if (ans<0){
				ans+=mod;
			}
			if (tc<0){
				__int64 value=min(-tc,iter->second);
				tc+=value;
				if (iter->second>value){
					tcnt[iter->first+delta]=iter->second-value;
				}
			} else {
				tcnt[iter->first+delta]=iter->second;
			}
		}
		cnt=tcnt;
		cur=it->first;
	}
	return ans%mod;
}

int main(){
	__int64 tcase;
	scanf("%I64d",&tcase);
	for (__int64 i=1;i<=tcase;i++){
		init();
		printf("Case #%I64d: %I64d\n",i,calc());
	}
	return 0;
}
