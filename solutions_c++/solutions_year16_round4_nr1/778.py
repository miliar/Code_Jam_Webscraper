#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <iterator>
#include <limits>
#include <numeric>
#include <utility>
#include <cmath>
#include <cassert>
#include <cstdio>

using namespace std;
using namespace placeholders;

using LL = long long;
using ULL = unsigned long long;
using VI = vector< int >;
using VVI = vector< vector< int > >;
using VS = vector< string >;
using SS = stringstream;
using PII = pair< int, int >;
using VPII = vector< pair< int, int > >;
template < typename T = int > using VT = vector< T >;
template < typename T = int > using VVT = vector< vector< T > >;
template < typename T = int > using LIM = numeric_limits< T >;

template < typename T > inline istream& operator>>( istream &s, vector< T > &v ){ for ( T &t : v ) { s >> t; } return s; }
template < typename T > inline ostream& operator<<( ostream &s, const vector< T > &v ){ for ( int i = 0; i < int( v.size() ); ++i ){ s << ( " " + !i ) << v[i]; } return s; }
template < typename T > inline T fromString( const string &s ) { T res; istringstream iss( s ); iss >> res; return res; }
template < typename T > inline string toString( const T &a ) { ostringstream oss; oss << a; return oss.str(); }

#define REP2( i, n ) REP3( i, 0, n )
#define REP3( i, m, n ) for ( int i = ( int )( m ); i < ( int )( n ); ++i )
#define GET_REP( a, b, c, F, ... ) F
#define REP( ... ) GET_REP( __VA_ARGS__, REP3, REP2 )( __VA_ARGS__ )
#define FOR( e, c ) for ( auto &&e : c )
#define ALL( c ) begin( c ), end( c )
#define AALL( a, t ) ( t* )a, ( t* )a + sizeof( a ) / sizeof( t )
#define DRANGE( c, p ) ( c ).begin(), ( c ).begin() + ( p ), ( c ).end()

#define SZ( v ) ( (int)( v ).size() )
#define EXIST( c, e ) ( ( c ).find( e ) != ( c ).end() )

template < typename T > inline bool chmin( T &a, const T &b ){ if ( b < a ) { a = b; return true; } return false; }
template < typename T > inline bool chmax( T &a, const T &b ){ if ( a < b ) { a = b; return true; } return false; }

#define PB push_back
#define EM emplace
#define EB emplace_back
#define BI back_inserter

#define MP make_pair
#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl

constexpr char *CHOICES = "RSP";

int tournament[ 1 << 14 ];

bool possible( const int N, VI A, const int W )
{
	tournament[1] = W;
	REP( i, 1 , 1 << N )
	{
		tournament[ i * 2 ] = tournament[i];
		tournament[ i * 2 + 1 ] = ( tournament[i] + 2 ) % 3;
	}

	REP( i, 1 << N, 1 << ( N + 1 ) )
	{
		--A[ tournament[i] ];
	}

	return count( ALL( A ), 0 ) == 3;
}

string smallest( const int N )
{
	static VS strs( 1 << 14 );
	transform( tournament + ( 1 << N ),
			tournament + ( 1 << ( N + 1 ) ), begin( strs ) + ( 1 << N ), []( const int i ){ return string( 1, CHOICES[i] ); } );

	for ( int i = ( 1 << N ) - 1; 0 < i; --i )
	{
		const string &s1 = strs[ i * 2 ], &s2 = strs[ i * 2 + 1 ];
		strs[i] = s1 < s2 ? s1 + s2 : s2 + s1;
	}
	return move( strs[1] );
}

string solve()
{
	int N;
	cin >> N;

	VI A( 3 );
	cin >> A;
	swap( A[1], A[2] );

	string res = "~";
	REP( i, 3 )
	{
		if ( possible( N, A, i ) )
		{
			chmin( res, smallest( N ) );
		}
	}

	return res == "~" ? "IMPOSSIBLE" : res;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );
	cout << setprecision( 12 ) << fixed;

	int T;
	cin >> T;

	REP( i, T )
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}
