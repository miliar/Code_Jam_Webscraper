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

const int infty = 999999999;

const int dx[8] = {  1, 0,-1, 0, 1,-1,-1, 1 };
const int dy[8] = {  0, 1, 0,-1, 1, 1,-1,-1 };

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

int main()
{
	int nruns;
	cin >> nruns;

	cout << setprecision(10);

	for(int run=1; run<=nruns; run++) {

		int N;
		double V,T,minT,maxT;
		cin >> N >> V >> T;

		vector<double> r(N), t(N);
		REP(i,N) cin >> r[i] >> t[i];

		minT = maxT = t[0];
		REP(i,N) {
			minT = min(minT,t[i]);
			maxT = max(maxT,t[i]);
		}

		if ( T < minT-1E-7 || T > maxT+1E-7 ) {
			cout << "Case #" << run << ": IMPOSSIBLE" << endl;
			continue;
		}

		double res;
		if ( N==1 ) {
			res = V/r[0];
		} else {
			if ( fabs(t[0]-t[1])<1E-7 ) {
				res = V/(r[0]+r[1]);
			} else {
				res = 0;
				REP(i,2) res = max(res,(T-t[1-i])/(t[i]-t[1-i])*V/r[i]);
			}
		}

		cout << "Case #" << run << ": ";
		cout << res << endl;
	}

	return 0;
}
