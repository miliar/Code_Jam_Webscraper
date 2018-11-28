#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int t;
long long n,m;
struct P{
	long long s,e,p;
};
P z[1100];

long long MOD=1000002013;

map<long long,long long>mp;
long long stk[11000][2];
long long sn;

int main(){
	int h,i,j,k;
	long long ans1,ans2,tmp;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%lld%lld",&n,&m);
		ans1=ans2=0;
		mp.clear();
		for(i=0;i<m;i++){
			scanf("%lld%lld%lld",&z[i].s,&z[i].e,&z[i].p);
			tmp=(2*n-z[i].e+z[i].s+1)*(z[i].e-z[i].s)/2;
			tmp%=MOD;
			tmp*=z[i].p;
			tmp%=MOD;
			ans1+=tmp;
			ans1%=MOD;
			mp[z[i].s]+=z[i].p;
			mp[z[i].e]-=z[i].p;
		}
		sn=0;
		for(map<long long,long long>::iterator iter=mp.begin();iter!=mp.end();iter++){
			if(iter->second>0){
				stk[sn][0]=iter->first;
				stk[sn][1]=iter->second;
				sn++;
			}else if(iter->second<0){
				long long v=-iter->second,ee,ss;
				while(v){
					if(stk[sn-1][1]>v){
						stk[sn-1][1]-=v;
						ee=iter->first;
						ss=stk[sn-1][0];
						tmp=(2*n-ee+ss+1)*(ee-ss)/2;
						tmp%=MOD;
						tmp*=v;
						tmp%=MOD;
						ans2+=tmp;
						ans2%=MOD;
						break;
					}else{
						v-=stk[sn-1][1];
						ee=iter->first;
						ss=stk[sn-1][0];
						tmp=(2*n-ee+ss+1)*(ee-ss)/2;
						tmp%=MOD;
						tmp*=stk[sn-1][1];
						tmp%=MOD;
						ans2+=tmp;
						ans2%=MOD;
						sn--;
					}
				}
			}
		}
		printf("Case #%d: %lld\n",h,((ans1-ans2)%MOD+MOD)%MOD);
	}
	return 0;
}
