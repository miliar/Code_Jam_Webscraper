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

const int N = 10005;
int a[N];

int main() {
	int cases;

	cin >> cases;

	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int n;
		int X;
		cin >> n >> X;
		assert( n <= N );
		for( int i = 0; i < n; ++i ) {
			cin >> a[i];
		}
		sort( a, a+n );
		int u = 0;
		int v = n-1;

		int cnt = 0;
		while( u <= v ) {
			++cnt;
			if( u == v ) {
				break;
			}
			if( a[u]+a[v] > X ) {
				--v;
			} else {
				--v;
				++u;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}

