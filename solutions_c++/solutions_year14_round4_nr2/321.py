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

int a[1010];

int main() {
	int cases;

	cin >> cases;

	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";

		int n;
		cin >> n;
		assert( n <= 1000 );

		for( int i = 0; i < n; ++i ) {
			cin >> a[i];
		}

		if( n <= 2 ) {
			cout << 0 << endl;
			continue;
		}

		int u = 0;
		int v = n-1;
		int res = 0;

		while( u+2 <= v ) {
			// det maxi,mini;
			int maxi = u;
			int mini = u;
			for( int i = u+1; i <= v; ++i ) {
				if( a[i] > a[maxi] ) maxi = i;
				if( a[i] < a[mini] ) mini = i;
			}
			// check inc
			bool ok = true;
			for( int i = u+1; i <= maxi; ++i ) {
				if( a[i] < a[i-1] ) {
					ok = false;
					break;
				}
			}
			if( ok ) {
				// check dec
				for( int i = maxi+1; i <= v; ++i ) {
					if( a[i] > a[i-1] ) {
						ok = false;
						break;
					}
				}
			}
			if( ok ) break;
			//
			if( mini-u < v-mini ) {
				// to left
				for( int i = mini; i > u; --i ) {
					swap( a[i], a[i-1] );
					++res;
				}
				++u;
			} else {
				// to right
				for( int i = mini; i < v; ++i ) {
					swap( a[i], a[i+1] );
					++res;
				}
				--v;
			}
		}
		cout << res << endl;
	}
	return 0;
}

