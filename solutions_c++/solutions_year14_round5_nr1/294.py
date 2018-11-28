#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <cassert>
#include <cmath>
#include <deque>
#include <map>
#include <cstring>
#include <set>

using namespace std;

typedef pair<int,int> P;
typedef long long LL;

LL x[1000005];
LL cx[1000005];

inline LL intervall( int u, int v ) {
	return cx[v]-(u==0?0:cx[u-1]);
}

int main() {
	int cases;

	cin >> cases;

	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int N;
		LL p, q, r, s;
		cin >> N >> p >> q >> r >> s;

		assert( N <= 1000000 );
		for( int i = 0; i < N; ++i ) {
			x[i] = (((LL)i*p+q)%r)+s;
			if( i == 0 ) cx[0] = x[0]; else cx[i] = x[i] + cx[i-1];
		}

		if( N == 1 ) {
			cout << "0.0000000" << endl;
			continue;
		}

		LL sum = intervall( 0, N-1 );
		if( N == 2 ) {
			printf( "%.20f\n", (double)min(x[0],x[1])/(double)sum );
			continue;
		}

		LL best = 0;
		for( int i = 0; i < N-2; ++i ) {
			int u = i+1;
			int v = N-2;
			LL mindiff = sum+1;
			LL minleft = 0;
			LL minright = 0;
			while( u <=v ) {
				int w =(u+v)/2;
				LL left = intervall( i+1, w );
				LL right = intervall( w+1, N-1 );

				if( llabs(left-right) < mindiff ) {
					minleft = left;
					minright = right;
					mindiff =llabs(left-right);
				}

				if( left < right ) {
					u = w+1;
				} else {
					v = w-1;
				}
			}
			LL opp = intervall( 0, i );
			opp = max( opp, minleft );
			opp = max( opp, minright );
			best = max( best, sum - opp );
		}
		printf( "%.20f\n", (double)best/(double)sum );
	}
	return 0;
}

