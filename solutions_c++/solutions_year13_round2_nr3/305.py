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

int best;
char in[55];
int dp[55][55][55][55];
int dp2[55][55][55][55];
int n;
set<string> S;
string str;

int cut(int pos, int lastCut, int l1, int l2) {
	int &ret = dp2[pos][lastCut][l1][l2];
	if(ret != -1) return ret;
	
	ret = 1000111;
	// debug("CUT %d %d\n", lastCut+1, pos);
	if( S.count( str.substr(lastCut+1, pos-lastCut) ) )
			return (ret = 0);
	
	if(lastCut+1 <= l1 && l1 <= pos) {
		char tmp = str[l1];
		FOR(c1, 'a', 'z') {
			int cnt = (c1 == str[l1] ? 0 : 1);
			str[l1] = c1;
			// if(lastCut == 0 && pos == 4) printf("%d %s\n", l1, str.substr(lastCut+1, pos-lastCut).c_str());
			if( S.count( str.substr(lastCut+1, pos-lastCut) ) ) {
				MN(ret, cnt); //if(lastCut == 0 && pos == 4) debug("YO\n");
				continue; // can't be better
			}
			
			if(ret <= 2) continue;
			if(lastCut + 1 <= l2 && l2 <= pos) {
				char t2 = str[l2]; ++cnt;
				FOR(c2, 'a', 'z') if(t2 != c2) {
					str[l2] = c2;
					if( S.count( str.substr(lastCut+1,  pos-lastCut) ) ) {
						MN(ret, cnt);
						break;
					}
				}
				str[l2] = t2;
			}
		}
		str[l1] = tmp;
	}
	
	return ret;
}

int f(int pos, int lastCut, int lastC, int last2) {
	if(pos > n) {
		if(lastCut == n) return 0;
		return 1000111;
	}
	
	int &ret = dp[pos][lastCut][lastC][last2];
	if(ret != -1) return ret;
	
	ret = 1000111;
	if(!lastC || pos-lastC >= 5) {
		if(pos - lastCut < 10) ret = min(ret, f(pos+1, lastCut, pos, lastC));
		// cut here
		int k = cut(pos, lastCut, pos, lastC);
		// if(lastCut == 4 && pos == 7) debug("%d %d -> %d\n", lastCut, pos, k);
		ret = min(ret, f(pos+1, pos, pos, lastC) + k);
	}
	
	if(pos - lastCut < 10) ret = min(ret, f(pos+1, lastCut, lastC, last2));
	int k = cut(pos, lastCut, lastC, last2);
	
	ret = min(ret, f(pos+1, pos, lastC, last2) + k);
	// if(lastCut == 4 && pos == 7) debug("F %d %d %d (%d) = %d\n", lastCut, pos, lastC, k, ret);
	return ret;
}

// void coba(int pos, int lastCut, int lastC, int now) {
	// if(now >= best) return;
	// if(pos > n) {
		// if(lastCut == n)
			// best = min(best, now);
		// return;
	// }
	
	// if(!lastCut || lastCut - pos >= 5) {
		// char tmp = str[pos];
		// FOR(c, 'a', 'z') if(c != str[pos]) {
			// str[pos] = c;
			// if(pos - lastCut < 10) coba(pos+1, lastCut, pos, now+1);
			// // cut here
			// if( S.count( str.substr(lastCut+1, pos-lastCut) ) )
				// coba(pos+1, pos, pos, now+1);
		// }
		// str[pos] = tmp;
	// }
	
	// if(pos - lastCut < 10) coba(pos+1, lastCut, pos, now);
	// if( S.count( str.substr(lastCut+1, pos-lastCut) ) )
				// coba(pos+1, pos, pos, now);
// }

int main() {
	int TC = SI;
	FILE * fs = fopen("dict.txt", "r");
	while( fscanf(fs, "%s", in) != EOF ) S.insert(in);
	
	FOR(tc, 1, TC) {
		printf("Case #%d: ", tc);
		scanf("%s", in);
		n = strlen(in);
		str = "#";
		str = str + in;
		
		best = 205;
		debug("COBA %s\n", str.c_str());
		
		memset(dp, -1, sizeof dp);
		memset(dp2, -1, sizeof dp2);
		best = f(1, 0, 0, 0);
		// coba(1, 0, 0, 0);
		printf("%d\n", best);
	}
	
}