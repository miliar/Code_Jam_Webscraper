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

#define maxn 

ll n,p;

ll worst(ll x) {
	ll better=x-1;
	ll worse=(1LL<<n)-x;
	ll res=0;
	FOR(i,1,n) {
		if(better>0) {
			better--;
			if(better%2==0){
				better/=2;
				worse/=2;
			} else {
				better/=2;
				worse/=2;
				worse++;				
			}
			res=res*2+1;
		} else {
			res=res*2;
		}
	}
	
	return res;
}

ll best(ll x) {
	ll better=x-1;
	ll worse=(1LL<<n)-x;
	ll res=0;
	FOR(i,1,n) {
		if(worse>0) {
			worse--;
			worse/=2;
			res=res*2;
		} else res=res*2+1;
	}
	
	return res;
}

int main() {
	freopen("a.inp","r",stdin);
	freopen("a.out","w",stdout);
	int ntest;cin >> ntest;
	FOR(test,1,ntest) {
		cin >> n >> p;
				
		cout << "Case #" << test << ": ";
		
		ll low=1,high=(1LL<<n);
		while(low<high) {
			ll mid=(low+high+1)/2;
			if(worst(mid)+1<=p) low=mid;
			else high=mid-1;
		}
		cout << low-1 << " ";
		
		
		low=1,high=(1LL<<n);
		while(low<high) {
			ll mid=(low+high+1)/2;
			if(best(mid)+1<=p) low=mid;
			else high=mid-1;
		}
		
		cout << low-1 << endl;
	}
}

