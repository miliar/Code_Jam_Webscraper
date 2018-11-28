// imiro
#define OYE using namespace std
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

OYE;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<char> vc;
typedef vector<string> vs;

#define REP(i,s,n) for(int (i)=(s), _n = (n);(i)<_n;(i)++)
#define FOR(i,s,n) for(int (i)=(s), _n = (n);(i)<=_n;(i)++)
#define rep(i,n) REP(i,0,n)

#define All(v) (v).begin(), (v).end()
#define Reversed(v) (v).rbegin(), (v).rend()
#define sz(v) (int) v.size()
#define LB(v,x) (lower_bound(All(v),x) - (v).begin())
#define UB(v,x) (upper_bound(All(v),x) - (v).begin())
#define UNIQUE(v) { sort(All(v)); (v).erase( unique(All(v)), (v).end() ); }

#define SQR(a) ((a)*(a))
#define MX(x,y) (x) = max( (x), (y) )
#define MN(x,y) (x) = min( (x), (y) )

#define mp make_pair
#define pb push_back
#define ji first
#define ro second

#define SI ({int __x_; scanf("%d", &__x_); __x_;})

inline void OPEN(string a, bool out = false) {
	freopen(string(a + ".in").c_str(), "r", stdin);
	if(out) freopen(string(a + ".out").c_str(), "w", stdout);
}

#ifdef DEBUGGING
#define debug(...) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#define FOPEN(x) 
#else
#define debug(...)
#define FOPEN(x) OPEN(x,1)
#endif

#define EPS 1e-7

int main() {
	int TC = SI;
	FOR(tc, 1, TC) {
		printf("Case #%d: ", tc);
		debug("Case #%d: ", tc);
		int a = SI;
		int n = SI;
		
		vi arr;
		rep(i,n) {
			int x = SI;
			arr.pb(x);
		}
		
		sort( All(arr) );
		ll x = a;
		
		int e = -1;
		rep(i, sz(arr)) 
		if(x > arr[i]) {
			x += arr[i];
		} else {
			e = i;
			break;
		}
		
		if(e == -1) {
			puts("0");
			debug("0\n");
			continue;
		}
		
		vi ar; REP(i,e,sz(arr)) ar.pb( arr[i] );
		
		int ans = sz(ar); // erase all
		int now = ans;
		// debug("ans = %d\n", ans);
		
		rep(i, sz(ar)) { // try not to erase this
			--now;
			if(x == 1) break;
			while(x <= ar[i]) {
				++now;
				x += x-1;
			}
			// debug("L %d %d %lld %d\n", i, now, x, ar[i]);
			x += ar[i];
			MN(ans, now);
		}
		
		printf("%d\n", ans);
		debug("%d\n", ans);
	}
}