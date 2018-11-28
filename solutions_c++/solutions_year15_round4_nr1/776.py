#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define ALL(x) ((x).begin()),((x).end())
#if __cplusplus >= 201103L
#define FOR(i,c) for(auto i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(decltype(n) i=0; i<(n); ++i)
#else
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)
#endif

const long long infty = 999999;

const int dx[8] = {  1, 0,-1, 0, 1,-1,-1, 1 };
const int dy[8] = {  0, 1, 0,-1, 1, 1,-1,-1 };

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

//#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const string dir(">v<^");

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		int R,C;
		cin >> R >> C;

		VS mp(R);
		REP(i,R) cin >> mp[i];

		long long res = 0;
		REP(y,R) REP(x,C) {
			if ( mp[y][x]!='.' ) {
				long long add = infty;
				debug("x,y = %d,%d\n",x,y);
				REP(d,4) {
					int x1=x,y1=y;
					do {
						x1 += dx[d];
						y1 += dy[d];
						if ( x1<0 || x1>=C ||
						     y1<0 || y1>=R ) break;
						debug("x1,y1 = %d,%d\n",x1,y1);
						if ( mp[y1][x1]!='.' ) {
							debug("hit %d,%d\n",x1,y1);
							add = min(add,(dir[d]==mp[y][x] ? 0LL : 1LL));
						}
					} while ( true );
				}
				debug("add = %lld\n",add);
				res += add;
			}
		}

		cout << "Case #" << run << ": ";
		if ( res>=infty ) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << res << endl;
		}
	}

	return 0;
}
