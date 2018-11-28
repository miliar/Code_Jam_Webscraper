#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <string>
#include <cstring>
#include <bitset>
#include <queue>
#include <stack>

#define DBGMODE
#ifdef DBGMODE
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif
#define NMAX 100000000
#define MOD 1000000009

#define DEBUG(x) cout << '>' << #x << ": " << x << endl;
inline bool EQ( double a, double b ) { return fabs( a - b ) < 1e-9; }

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

inline int two( int n ) { return 1 << n; }
inline int test( int n, int b ) { return ( n >> b ) & 1; }
inline void set_bit( int & n, int b ) { n |= two( b ); }
inline void unset_bit( int & n, int b ) { n &= ~two( b ); }
inline int last_bit( int n ) { return n & ( -n ); }
inline int ones( int n ) { return __builtin_popcount( n ); }

template<class T> void chmax( T & a, const T & b ) { a = max( a, b ); }
template<class T> void chmin( T & a, const T & b ) { a = min( a, b ); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Mit nezel Jozsi? :D

bool analyze( string &s, int len ) {
	for ( int i = 0; i < s.size(); i += 2 * len ) {
		int equal = true;
		sort( &s[i], &s[i]+len );
		sort( &s[i] + len, &s[i] + len + len );
		for ( int j = 0; j < len; ++j ) {
			equal &= s[i + j] == s[i + len + j];
		}
		if ( equal )
			return false;
	}
	return true;
}

void subsolve( istream &is, ofstream &ofs ) {
	int N, R, P, S;
	is >> N >> R >> P >> S;
	string s = string( P, 'P' ) + string( R, 'R' ) + string( S, 'S' );

	do {
		bool bad = false;
		string s2 = s;
		for ( int i = 1; i < R+P+S; i *= 2 ) {
			bad = !analyze( s2, i );
			if ( bad )
				break;
		}
		if ( bad )
			continue;
		ofs << s;
		return;
	} while ( next_permutation( s.begin(), s.end() ) );
	ofs << "IMPOSSIBLE";
}

void solve( istream &is ){
	ofstream ofs( "output.txt" );
	int T;
	is >> T;
	for ( int tt = 1; tt <= T; ++tt ) {
		ofs << "Case #" << tt << ": ";
		subsolve( is, ofs );
		ofs << '\n';
	}
}

int main() {
	ios::sync_with_stdio( false );
	cin.tie( nullptr );
	cout.tie( nullptr );

#ifdef DBGMODE
	ifstream ifs( "input.txt" );
	solve( ifs );
#else
	solve( cin );
#endif

	return 0;
}
