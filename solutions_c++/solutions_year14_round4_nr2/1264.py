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
typedef vector<VI>  VVI;
typedef vector<VVI> VVVI;
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

const int infty = 1999999999;

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

int nsort(vector<int> a)
{
	int res = 0;
	REP(i,a.size()) REP(j,i) if ( a[j]>a[i] ) res++;
	return res;
}

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		int n;

		cin >> n;
		vector<int> a(n), b(n);
		REP(i,n) { cin >> a[i]; b[i] = i; }

		int ls = 0;
		REP(i,n) if ( a[i]>ls ) ls = a[i];

		int best = infty;
		do {
			int i,dir = 1;
			for(i=0; i<n-1; i++) {
				if ( a[b[i]]==ls ) dir = -1;
				if ( dir*(a[b[i+1]]-a[b[i]])<=0 ) break;
			}
			if ( i>=n-1 ) {
				int curr = nsort(b);
				if ( curr<best ) best = curr;
			}
		} while ( next_permutation(ALL(b)) );


		cout << "Case #" << run << ": ";
		cout << best << endl;
	}

	return 0;
}
