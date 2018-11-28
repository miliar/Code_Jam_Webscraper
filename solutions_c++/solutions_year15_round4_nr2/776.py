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
typedef pair<double,double> pdou;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
double eps=1e-6,inf=1e10;
vector<pdou> hi,lo,hi2,lo2;
double V,X,same,hisum,losum;
double cal(void){
	double r,c;losum=0.0;hisum=0.0;same=0.0;
	int n;
	hi.clear();lo.clear();
	cin>>n>>V>>X;
	rep(i,n){
		cin>>r>>c;
		if(fabs(c-X)<eps) same+=r;
		else if(c<X) lo.pb(mp(X-c,r)),losum+=r;
		else hi.pb(mp(c-X,r)),hisum+=r;
	}
	if(hi.size()<1 || lo.size()<1){
		if(same>eps) return V/same;
		else return -1.0;
	}
	double x=V*hi[0].fi/(hi[0].fi+lo[0].fi),y=V-x;
	return max(x/lo[0].se,y/hi[0].se);
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		//cerr<<i<<endl;
		double ret=cal();
		if(ret<-eps) printf("Case #%d: IMPOSSIBLE\n",i+1);
		else printf("Case #%d: %.12f\n",i+1,ret);
	}
}
