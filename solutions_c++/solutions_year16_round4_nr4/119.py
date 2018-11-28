#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
namespace MF{
	#define MAXN 25252
	#define MAXM 364364
	#define wint int
	const wint wEPS=0;
	const wint wINF=1001001001;
	int n,m,ptr[MAXN],next[MAXM],zu[MAXM];
	wint capa[MAXM],tof;
	int lev[MAXN],see[MAXN],que[MAXN],*qb,*qe;
	void init(int _n){
		n=_n;m=0;memset(ptr,~0,n*4);
	}
	void ae(int u,int v,wint w0,wint w1=0){
		next[m]=ptr[u];ptr[u]=m;zu[m]=v;capa[m]=w0;++m;
		next[m]=ptr[v];ptr[v]=m;zu[m]=u;capa[m]=w1;++m;
	}
	wint augment(int src,int ink,wint flo){
		if(src==ink) return flo;
		wint f;
		for(int &i=see[src];~i;i=next[i]) if(capa[i]>wEPS && lev[src]<lev[zu[i]]){
			if((f=augment(zu[i],ink,min(flo,capa[i])))>wEPS){
				capa[i]-=f;capa[i^1]+=f;return f;
			}
		}
		return 0;
	}
	bool solve(int src,int ink,wint flo=wINF){
		wint f;
		int i,u,v;
		for(tof=0;tof+wEPS<flo;){
			qb=qe=que;
			memset(lev,~0,n*4);
			for(lev[*qe++=src]=0,see[src]=ptr[src];qb!=qe;){
				for(i=ptr[u=*qb++];~i;i=next[i]) if(capa[i]>wEPS && !~lev[v=zu[i]]){
					lev[*qe++=v]=lev[u]+1;see[v]=ptr[v];
					if(v==ink) goto au;
				}
			}
			return 0;
		au:	for(;(f=augment(src,ink,flo-tof))>wEPS;tof+=f);
		}
		return 1;
	}
}
string s[28];
int n,allo;
bool cal(int mask){
	rep(i,n){
		int now=((mask>>(n*i))&allo);
		if(now==allo) continue;
		if(now==0) return false;
		MF::init(n*2+2);
		rep(j,n){
			if((now&(1<<j))) MF::ae(n+j,n*2+1,1);
		}
		rep(j,n){
			if(i==j) continue;
			int n2=((mask>>(n*j))&allo);
			MF::ae(n*2,j,1);
			rep(k,n){
				if((n2&(1<<k))) MF::ae(j,n+k,1);
			}
		}
		MF::solve(n*2,n*2+1);
		if(MF::tof>=__builtin_popcount(now)) return false;
		//if((now&other)>=now) return false;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cin>>n;
		rep(j,n) cin>>s[j];
		int mask=0,ret=114514;allo=(1<<n)-1;
		rep(j,n*n){
			if(s[j/n][j%n]=='1') mask+=(1<<j);
		}
		rep(j,(1<<(n*n))){
			if((j&mask)>0) continue;
			if(cal(j+mask)) ret=min(ret,__builtin_popcount(j));
		}
		printf("Case #%d: %d\n",i+1,ret);
	}
}
