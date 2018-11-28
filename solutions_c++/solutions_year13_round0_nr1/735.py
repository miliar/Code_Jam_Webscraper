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
#define UNIQUE(v) { sort(All(v)); (v).erase( unique(All(v), (v).end()) ); }

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

char board[7][7];
int main() {
	int TC = SI;
	FOR(tc, 1, TC) {
		printf("Case #%d: ", tc);
		rep(i,4) scanf("%s", board[i]);
		
		int win = 0; char c;
		
		// baris
		rep(i,4) {
			c = board[i][0]; if(c == 'T') c = board[i][1];
			if(c == '.') continue;
			bool ok = 1;
			rep(j,4) if( board[i][j] != 'T' && board[i][j] != c ) ok = 0;
			if(ok) win = (c == 'X' ? 1 : 2);
		}
		
		// kolom
		rep(j,4) {
			c = board[0][j]; if(c == 'T') c = board[1][j];
			if(c == '.') continue;
			bool ok = 1;
			rep(i,4) if( board[i][j] != 'T' && board[i][j] != c ) ok = 0;
			if(ok) win = (c == 'X' ? 1 : 2);
		}
		
		c = board[0][0]; if(c == 'T') c = board[1][1];
		bool ok = 1;
		rep(i,4) if( board[i][i] != 'T' && board[i][i] != c ) ok = 0;
		if(ok && c != '.') win = (c == 'X' ? 1 : 2);
		
		c = board[0][3]; if(c == 'T') c = board[1][2];
		ok = 1;
		rep(i,4) if( board[i][4-i-1] != 'T' && board[i][4-i-1] != c ) ok = 0;
		if(ok && c != '.' ) win = (c == 'X' ? 1 : 2);
		
		if(!win) {
			ok = 1;
			rep(i,4) rep(j,4) if( board[i][j] == '.' ) ok = 0;
			if(ok) puts("Draw");
			else puts("Game has not completed");
		} else {
			printf("%c won\n", win == 1 ? 'X' : 'O');
		}
	}
}