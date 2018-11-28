#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdio>
#include <set>
#include <map>
#include <sstream>
#include <cmath>
#include <functional>
#include <cassert>
#include <queue>
#include <cstring>
#include <limits>

using namespace std;

typedef long long LL;

LL worst( LL smaller, LL bigger ) {
	if( smaller == 0 ) return 0;
	LL n = smaller+bigger+1;
	LL new_smaller = (smaller-1)/2;
	if( new_smaller > n/2-1 ) new_smaller = n/2-1;
	return n/2+worst( new_smaller, n/2-new_smaller-1 );
}

LL best( LL smaller, LL bigger ) {
	if( bigger == 0 ) return smaller;
	LL n = smaller+bigger+1;
	LL new_smaller = (smaller+1)/2;
	if( new_smaller > n/2-1 ) new_smaller = n/2-1;
	return best( new_smaller, n/2-new_smaller-1 );
}

int main() {
	int cases;
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cout << "Case #" << caseid << ": ";
		int N;
		LL P;
		cin >> N >> P;
		
		LL teams = (LL)1<<N;
		LL u = 0;
		LL v = teams-1;
		while( u <= v ) {
			LL w = (u+v)/2;
			LL x = worst( w, teams-w-1 );
			if( x <= P-1 ) {
				// can win, try bigger number
				u = w+1;
			} else v = w-1;
		}
		LL res1 = v;
		//
		u = 0;
		v = teams-1;
		while( u <= v ) {
			LL w = (u+v)/2;
			LL x = best( w, teams-w-1 );
			if( x <= P-1 ) {
				// can win try bigger number
				u = w+1;
			} else v = w-1;
		}
		LL res2 = v;
		
		
		cout << res1 << ' ' << res2 << endl;
	}
	return 0;
}

