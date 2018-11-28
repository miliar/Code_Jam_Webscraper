#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<utility>
#define pb push_back
#define MAXN 1010
#define MOD 1000002013
using namespace std;
typedef long long LL;
typedef double db;
int cas=0,T,N,M,S[MAXN],P[MAXN];
long long org,now;
struct Pass{
	int pos,type,p;
	bool operator<(const Pass &rhs)const{
		if(pos!=rhs.pos) return pos<rhs.pos;
		return type<rhs.type;
	}
}a[MAXN*2];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		org=now=0;
		scanf("%d%d",&N,&M);
		for(int i=1;i<=M;++i){
			scanf("%d%d%d",&a[i].pos,&a[i+M].pos,&a[i].p);
			a[i].type=0;a[i+M].type=1;a[i+M].p=a[i].p;
			int s=a[i].pos,t=a[i+M].pos;
			org=(org+((LL)N*(t-s)%MOD-(LL)((t-s-1)*(t-s)/2)%MOD)*a[i].p%MOD+(LL)MOD)%(LL)MOD;
		}
		sort(a+1,a+1+M+M);
		int h=0;
		for(int i=1;i<=M*2;++i){
			if(a[i].type==0){
				S[++h]=a[i].pos;
				P[h]=a[i].p;
			}
			else{
				int j=a[i].p;
				while(j>0){
					int s=S[h],t=a[i].pos,p=min(j,P[h]);
					now=(now+((LL)N*(t-s)%MOD-(LL)((t-s-1)*(t-s)/2)%MOD)*p%MOD+(LL)MOD)%(LL)MOD;
					j-=p;P[h]-=p;
					if(P[h]==0) h--;
				}
			}
		}
		printf("Case #%d: %lld\n",++cas,(org+(LL)MOD-now)%MOD);
	}				
	return 0;
}
