#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef long double ld;

/*ld memo[202][202][202];
ld solve(int yc,int rc,int idx){
	if(idx==n)return (2*yc==k&&!rc);
	ld &ret=memo[yc][rc][idx];
	if(ret==ret)return ret;
	ret=solve(yc,rc,idx+1);
	if(rc)
		ret=max(ret,p[idx]*solve(yc+1,rc-1,idx+1)+(1-p[idx])*solve(yc,rc-1,idx+1));
	return ret;
}*/

const int mN=16;
int n,k,t;
ld p[mN];
int m;
ld memo[mN][mN];
ld solve(int yc,int idx){
	if(idx==n)return 2*yc==k;
	ld &ret=memo[yc][idx];
	if(ret==ret)return ret;
	if(m&(1<<idx))return ret=p[idx]*solve(yc+1,idx+1)+(1-p[idx])*solve(yc,idx+1);
	return ret=solve(yc,idx+1);
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	sc(t);
	lop(C,t){
		sc(n),sc(k);
		lop(i,n){
			cin>>p[i];
		}
		ld b=0;
		lop(mask,(1<<n)){
			if(__builtin_popcount(mask)!=k)continue;
			m=mask;
			memset(memo,-1,sizeof memo);
			b=max(b,solve(0,0));
		}
		printf("Case #%d: ",C+1);
		cout<<fixed<<setprecision(13)<<b<<endl;

	}

};
