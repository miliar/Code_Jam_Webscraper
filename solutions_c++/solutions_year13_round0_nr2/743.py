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

const int MAX = 105;

bool row[MAX], col[MAX];
int inp[MAX][MAX];
vi num;

int main() {
	int TC = SI;
	FOR(tc, 1, TC) {
		printf("Case #%d: ", tc);
		
		num.clear();
		memset(row, 0, sizeof row);
		memset(col, 0, sizeof col);
		
		int n = SI, m = SI;
		rep(i,n) rep(j,m) { inp[i][j] = SI; num.pb(inp[i][j]); }
		
		UNIQUE(num); reverse( All(num) );
		bool ok = 1;
		rep(t, sz(num)) {
			int k = num[t];
			rep(i,n) rep(j,m) if( inp[i][j] == k && row[i] && col[j] ) ok = 0;
			if(!ok) break;
			
			rep(i,n) rep(j,m) if( inp[i][j] == k ) { row[i] = 1; col[j] = 1; }
		}
		
		puts(ok ? "YES" : "NO");
	}
}