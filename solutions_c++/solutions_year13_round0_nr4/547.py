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

bool inget[(1<<20) + 5];
vi ans;
int n;
int cnt[205], kunci[45];
vi daftar[45];

bool cari(int bm) {
	// debug("%d\n", bm);
	if( inget[bm] ) return 0;
	else if( __builtin_popcount(bm) == n ) return 1;
	
	rep(i, n) if( !(bm & (1 << i)) && cnt[ kunci[i] ] ) {
		--cnt[ kunci[i] ];
		ans.pb(i+1);
		rep(j, sz(daftar[i])) cnt[ daftar[i][j] ] += 1;
		
		if( cari(bm | (1<<i)) ) return 1;
		
		ans.pop_back();
		rep(j, sz(daftar[i])) --cnt[ daftar[i][j] ];
		++cnt[ kunci[i] ];
	}
	
	inget[bm] = 1;
	return 0;
}

int main() {
	int TC = SI;
	FOR(tc, 1, TC) {
		printf("Case #%d:", tc);
		int k = SI; n = SI;
		
		memset(inget, 0, sizeof inget);
		memset(kunci, 0, sizeof kunci);
		memset(cnt, 0, sizeof cnt);
		ans.clear();
		
		while(k--) { int a = SI; ++cnt[a]; }
		rep(i,n) {
			kunci[i] = SI;
			k = SI;
			daftar[i].clear();
			while(k--) {
				int a = SI;
				daftar[i].pb(a);
			}
		}
		
		if( cari(0) ) { rep(i,n) printf(" %d", ans[i]); puts(""); }
		else puts(" IMPOSSIBLE");
	}
}