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
ll best_rank(ll x) {
	ll count_worst = 0;
	ll fr = 0;
	for(int i = 0; i<n; i++) {
		if(2*count_worst+1 <= (1<<n)-x)
			fr = 2*fr, count_worst = 2*count_worst + 1;
		else fr = 2* fr+1;
	}
//	printf(" best rank for guy %Ld is %Ld\n", x, 1+fr);
	return 1+fr;
}
ll worst_rank(ll x) {
	ll count_better = 0;
	ll fr = 0;
	for(int i = 0; i<n; i++) {
		if(2*count_better +1 < x)
			fr = 2*fr+1, count_better = 2*count_better + 1;
		else fr = 2* fr;
	}
//	printf(" worst rank for guy %Ld is %Ld\n", x, 1+fr);
	return 1+fr;
}
ll guy(ll rank) {
	ll low = 1, high = 1LL<< n;
	while(low!=high) {
		ll mid = (low + high+1)>>1;
		if(worst_rank(mid)>rank) high = mid-1;
		else low = mid;
	}
	return low;
}
ll guy2(ll rank) {
	ll low = 1, high = 1LL<< n;
	while(low!=high) {
		ll mid = (low + high+1)>>1;
		if(best_rank(mid)>rank) high = mid-1;
		else low = mid;
	}
	return low;
}
void solve() {
	ll p;
	l(n);
	l(p);
	printf("%Ld %Ld\n", guy(p)-1, guy2(p)-1);
}
int main()
{
	ui T;
	u(T);
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: ", 1+i);
		solve();
	}
}
