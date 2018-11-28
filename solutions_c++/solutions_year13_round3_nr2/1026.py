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

typedef pair< ii, string > antrian;
const int MAX = 505;
bool visit[MAX][MAX][MAX];
int di[] = {0, -1, 0, 1},
	dj[] = {-1, 0, 1, 0};

string dir = "SWNE";

int main() {
	int TC = SI;
	FOR(tc, 1, TC) {
		printf("Case #%d: ", tc);
		memset(visit, 0, sizeof visit);
		
		int x = SI, y = SI;
		queue<antrian> Q;
		Q.push( mp( mp(0,0), "" ) );
		
		while( !Q.empty() ) {
			ii pos = Q.front().ji;
			string s = Q.front().ro;
			Q.pop();
			int jump = sz(s)+1;
			if(jump > 100) continue;
			
			if( pos == mp(x,y) ) {
				puts(s.c_str());
				break;
			}
			if(jump==2) debug("%d %d %s\n", pos.ji, pos.ro, s.c_str());
			
			rep(i,4) {
				int na = pos.ji +jump*di[i] + 105, nb = pos.ro+jump*dj[i] + 105;
				if( abs(na-105) > 100 || abs(nb-105) > 100 ) continue;
				if( !visit[na][nb][jump] ) {
					debug("ADD %d %d %s\n", na, nb, (s+dir[i]).c_str());
					Q.push( mp( mp(na-105,nb-105), s+dir[i]) );
					visit[na][nb][jump] = 1;
				}
			}
		}
	}
}