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

const LL modp = 1000002013;

int n,m;

LL travelcost(LL d)
{
	return ((2*n - d)*(1+d)/2 ) % modp;
}

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		map<int,pair<LL,LL> > onoff;
		LL cost = 0, real = 0, loss;

		cin >> n >> m;
		REP(i,m) {
			LL o, e, p;
			cin >> o >> e >> p;
			onoff[o].first += p;
			onoff[e].second += p;
			cost = (cost + travelcost(e-o)*p) % modp;
//			cerr << cost << endl;
		}

		priority_queue<pair<int,LL> > entry;
		FOR(it,onoff) {
			if ( it->second.first > 0 )
				entry.push(make_pair(it->first,it->second.first));

			LL off = it->second.second;
			while ( off > 0 ) {
				int o = entry.top().first;
				LL p = entry.top().second;
				entry.pop();
				LL pp = min(p,off);
				real = (real + travelcost(it->first - o)*pp) % modp;
				off -= pp;
				p -= pp;
				if  ( p > 0 ) entry.push(make_pair(o,p));
			}
		}

//		cerr << cost << " " << real << endl;

		loss = (cost - real + modp) % modp;

		cout << "Case #" << run << ": ";
		cout << loss << endl;

	}

	return 0;
}
