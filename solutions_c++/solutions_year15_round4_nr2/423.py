#include <cassert>
#include <string>
#include <sstream>
#include <iostream>
#include <deque>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <cstdio>

using namespace std;

typedef pair<int,int> PI;
typedef long long LL;

struct source_t {
	double rate;
	double temp;
};

source_t sources[104];

const double EPS = 1.0E-10;

int main() {
	int cases;

	cin >> cases;

	for( int caseno = 1; caseno <= cases; ++caseno ) {
		cout << "Case #" << caseno << ": ";
		int N;
		double volume, temp;
		cin >> N >> volume >> temp;
		for( int i = 0; i < N; ++i ) {
			cin >> sources[i].rate >> sources[i].temp;
		}
		double res;
		if( N == 1 ) {
			if( fabs(temp-sources[0].temp) > EPS ) {
				cout << "IMPOSSIBLE\n";
			} else {
				res = volume / sources[0].rate;
				printf( "%.20f\n", res );
			}
			continue;
		}
		
		if( N > 2 ) assert(0);
		
		if( sources[0].temp > sources[1].temp ) swap( sources[0], sources[1] );
		if( temp < sources[0].temp-EPS || sources[1].temp+EPS < temp ) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if( fabs(sources[0].temp-sources[1].temp) < EPS ) {
			if( fabs(temp-sources[0].temp) < EPS ) {
				res = volume / (sources[0].rate + sources[1].rate);
				printf( "%.20f\n", res );
			} else {
				cout << "IMPOSSIBLE\n";
			}
			continue;
		}
		// temps differ
		// 0 only?
		if( fabs( sources[0].temp-temp ) < EPS ) {
			res = volume / sources[0].rate;
			printf( "%.20f\n", res );
			continue;
		}
		// 1 only?
		if( fabs( sources[1].temp-temp ) < EPS ) {
			res = volume / sources[1].rate;
			printf( "%.20f\n", res );
			continue;
		}
		double V1 = volume * (temp - sources[0].temp) / (sources[1].temp-sources[0].temp);
		double V0 = volume - V1;
		res = V0 / sources[0].rate;
		res = max( res, V1 / sources[1].rate);
		printf( "%.20f\n", res );
	}
	return 0;
}

