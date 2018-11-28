//Written by technolt~h
 
#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>
 
#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FORN(i,a,b) for(int i=a;i<b;i++)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define RESET(c,x) memset (c, x, sizeof (c))
 
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()
 
#define DEBUG(x) { cerr << #x << " = " << x << endl; }
#define PR(a,n) {cerr<<#a<<" = "; FOR(_,1,n) cerr << a[_] << ' '; cerr <<endl;}
#define PR0(a,n) {cerr<<#a<<" = ";REP(_,n) cerr << a[_] << ' '; cerr << endl;}
#define ll long long
using namespace std;
 
const double PI = 2.0 * acos (0.0);
 
typedef long long LL;
typedef pair <int, int> PII;
 
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

#define maxn 100

ll a[maxn],b;

ll NEED(int nLowest,ll lowest) {
	ll need=0;
	FOR(i,1,nLowest) need+=lowest-a[i];
	FOR(i,nLowest+1,37) if(a[i]<=lowest) need+=lowest+1-a[i];
	return need;
}

bool chk(int nLowest,ll lowest) {
	FOR(i,1,nLowest) if(a[i]>lowest) return false;
	return NEED(nLowest,lowest)<=b;
}

ll profit(int nLowest,ll lowest) {
	ll sum=0;
	FOR(i,1,nLowest) sum+=lowest-a[i];
	return sum;
}


double calc(int nLowest,ll lowest) {
	return profit(nLowest,lowest)*36.0/nLowest-NEED(nLowest,lowest);
}

int main() {
	freopen("a.inp","r",stdin);
	freopen("a.out","w",stdout);
	int ntest; cin >> ntest;
	FOR(test,1,ntest) {
		
		ll n;
		cin >> b >> n;
		FOR(i,1,37) a[i]=0;
		FOR(i,1,n) cin >> a[i];
		
		sort(a+1,a+37+1);
		
		vector<ll> list;
		FOR(i,1,n) {
			list.PB(a[i]);
			if(a[i]) list.PB(a[i]-1);
			list.PB(a[i]+1);
			
			ll low=a[i],high=10000000000000LL;
			ll tmp=-1;
			while(low<=high) {
				ll mid=(low+high)/2;
				if(chk(i,mid)) {
					tmp=mid;
					low=mid+1;
				} else high=mid-1;
			}
			
			if(tmp!=-1) {
				list.PB(tmp);
				if(tmp) list.PB(tmp-1);
				list.PB(tmp+1);
			}
		}
		//FOR(i,0,1000) list.PB(i);
		
		double res=0;
		
		FOR(nLowest,1,37) {
			REP(i,list.size()) {
				ll lowest=list[i];
				if(chk(nLowest,lowest)) {
					double tmp=calc(nLowest,lowest);
					res=max(res,tmp);
				}
			}
		}
		
		cout << "Case #" << test << ": ";
		printf("%.9lf\n",res);
	}
}
