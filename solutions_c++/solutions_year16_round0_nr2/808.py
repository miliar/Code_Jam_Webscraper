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
#include <queue>
#include <stack>

#define DBGMODE
#ifdef DBGMODE
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif

#define NMAX 1000000000
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

void solve( istream &is ){
	ofstream ofs( "output.txt" );
	ULL T;
	is >> T;
	for ( ULL tt = 1; tt <= T; ++tt ) {
		ofs << "Case #" << tt << ": ";
		string cakes;
		is >> cakes;
		char prev = cakes[0];
		ULL flips = 0;
		for ( char c : cakes ) {
			if ( prev != c )
				++flips;
			prev = c;
		}
		if ( flips % 2 == 0 && cakes[0] == '-' )
			++flips;
		if ( flips % 2 == 1 && cakes[0] == '+' )
			++flips;
		ofs << flips;
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
