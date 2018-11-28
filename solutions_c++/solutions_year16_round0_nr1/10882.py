/*
 * Fixa Kattis, Johan!
 */

#pragma GCC target ("avx,avx2")
#pragma GCC optimize ("Ofast")
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <iomanip>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

#define deb( x ) ( #x ) << " = " << ( x )
#define endl "\n"
#define LOOPV( i, v ) for ( size_t i = 0; i < v.size ( ); ++ i )
#define RLOOPV( i, v ) for ( size_t i = v.size ( ) - 1; -1 < i; -- i )
#define FOR( i, s, e ) for ( unsigned i = s; i < e; ++ i )
#define FORE( i, s, e ) for ( unsigned i = s; i <= e; ++ i )
#define RFOR( i, s, e ) for ( int i = e; i < s; -- i )
#define RFORE( i, s, e ) for ( int i = e; i <= s; -- i )
#define REPD( n ) for ( ; n; -- n )
#define REPN( i, n ) for ( unsigned i = 0; i < n; ++ i )
#define REPNE( i, n ) for ( unsigned i = 0; i <= n; ++ i )
#define WIN( v ) while ( cin >> v )

using namespace std;

template < typename T > std::ostream & operator<< ( ostream & os, const vector < T > & v ) { os << "{ "; LOOPV ( i, v ) { os << v [ i ]; if ( i != v.size ( ) - 1 ) os << ", "; } os << " }"; return os; }
template < typename T1, typename T2 > std::ostream & operator<< ( ostream & os, const pair < T1, T2 > p ){ os << "{ " << p.first << ", " << p.second << " }"; return os; }

/* Template end */

int main ( ) {

	cin.tie ( 0 ); cout.tie ( 0 );
	cin.sync_with_stdio ( 0 );

	int nTestCases;
	cin >> nTestCases;
	for(int tc = 0; tc < nTestCases; ++ tc) {

		cout << "Case #" << tc + 1 << ": ";

		long long n;
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA\n";
			continue;
		}

		vector <bool> found ('9'-'0'+1, false);

		for(long long i = 1; true; ++ i) {

			long long in = i*n;
			string s(to_string(in));
			for(auto c:s) found[c-'0'] = true;
			bool done = true;
			for(auto e:found) if(!e) done = false;
			if(done) {
				cout << in << endl;
				break;
			}

		}

	}

}