#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

//#define DEBUG
ll power(ll x,ll y){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%mod;
    else y/=2,x=x*x%mod;
  }
  return t;
}
#ifdef DEBUG
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define dprintf(fmt,...)
#endif
#define ld long double 
ld arr[205][205];
ld p[205],tmp[205];
int n,k;
ld calc(){
	REP(i,k+1) REP(j,k+1) arr[i][j] = 0;
	arr[0][0]=1;
	REP(i,k){
		REP(j,k)if(arr[i][j]!=0.0) {
			arr[i+1][j]+=(1-tmp[i])*arr[i][j];
			arr[i+1][j+1]+=tmp[i]*arr[i][j];
		}
	}
	return arr[k][k/2];
}
int main(){
	int t; scanf("%d",&t);
	REP(aa,t){
		
		scanf("%d%d",&n,&k);
		REP(i,n) {
			double a; scanf("%lf",&a);
			p[i]=a;
		}
		sort(p,p+n);
		ld ans=0;
		REP(i,n) {
			if(i+k<=n) {
				REPP(j,i,i+k) tmp[j-i]=p[j];
				ans=max(ans,calc());
			}
		}
		REP(i,k+1){
			REP(j,i) tmp[j]=p[j];
			int x=i;
			for(int j=n-1;(i+n-j)<=k;j--) tmp[x++]=p[j];
			ans=max(ans,calc());	
		}
		printf("Case #%d: %.12lf\n",aa+1,(double)ans);
	}
  return 0;
}
	