#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FORe(i,a,b)	for(int i=(a);i<=(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define REP1(i,b)	FORe(i,1,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FROMTO(it,b,e)	for(LET(it,(b));it!=(e);++it)
#define FOREACH(it,c)	FROMTO(it,(c).begin(),(c).end())

ll gcd(ll a, ll b){
	if (a && b) for(ll x; b; b = x){
		x = a % b;
		a = b;
	}
	return a;
}
ll gcd(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))gcd) : 0LL;
}

ll lcm(ll a, ll b){
	return (a && b) ? a / gcd(a, b) * b : 0LL;
}
ll lcm(ll a[], int n){
	return n > 0 ? accumulate(a + 1, a + n, a[0], (ll(*)(ll,ll))lcm) : 0LL;
}

#define SCAN(p,f)	scanf("%" #f " ",p)
#define GET(t,x,f)	t x;SCAN(&x,f)
#define GETi(x)		GET(int,x,d)
#define GETl(x)		GET(ll,x,lld)
#define GETc(x)		GET(char,x,c)
#define GETf(x)		GET(float,x,f)
#define GETd(x)		GET(double,x,lf)

int ans[10000];
int main(){
	GETi(TTT);
	REP1(ttt, TTT){
		GETl(N);
		GETl(X);
		GETl(Y);
		if(X<0)X=-X;
		ll f=0,fixed=0,rest=N;
		while(1){
			int g=(fixed-1)*2+1;
			f+=g*2+3;
			if(f>N)break;
			rest=N-f;
			fixed++;
		}
		double ret=0;
		if(X+Y<=(fixed-1)*2){
			ret=1;
		}else if(rest==0 || X+Y>fixed*2){
			ret=0;
		}else if(f-N==1){
			ret=(X==0)?0:1;
		}else{
			REP(i,fixed*2+1)ans[i]=0;
			ll mask = 1L<<(int)rest;
			for(ll i=0;i<mask;++i){
				ll left=0,right=0;
				for(ll j=0,m=1;j<rest;++j,m*=2){
					if(left!=fixed*2 && ((m&i) || right==fixed*2)){
						left++;
					}else{
						right++;
					}
				}
				REP(i,left){
					ans[i]++;
				}
			}
			ret=ans[Y]/(double)mask;
		}
		
		printf("Case #%d: %.7f\n", ttt, ret);
	}
	return 0;
}
