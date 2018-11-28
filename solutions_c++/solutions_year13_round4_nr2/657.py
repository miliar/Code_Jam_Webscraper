#include <iostream>
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

	for(int run=1; run<=nruns; run++) {

		LL n;
		LL p, minp, maxp;

		cin >> n >> p;

		LL N = (1<<n);

		LL lowwin;
		for(lowwin=0; (1<<(n-lowwin))>p; lowwin++);
		maxp = N - (1<<lowwin);
//		cerr << n << " p = " << p << " " << lowwin << endl;

		LL hiloss;
		for(hiloss=0; N-(1<<(n-hiloss))<p; hiloss++);
		minp = (1<<hiloss)-2;
		if ( minp>=N ) minp = N-1;

//		cerr << hiloss << endl;

		cout << "Case #" << run << ": ";
		cout << minp << " " << maxp << endl;

	}

	return 0;
}
