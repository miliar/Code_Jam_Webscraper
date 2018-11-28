#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <iterator>
#include <limits>
#include <numeric>
#include <utility>
#include <cmath>

using namespace std; using namespace placeholders;

using LL = long long;
using ULL = unsigned long long;
using VI = vector<int>;
using VVI = vector<VI>;
using VS = vector<string>;
using SS = stringstream;
using PII = pair<int,int>;
using VPII = vector< pair<int,int> >;
template < typename T = int > using VT = vector<T>;
template < typename T = int > using VVT = VT< VT<T> >;
template < typename T = int > using LIM = numeric_limits<T>;

template < typename T > inline T fromString( const string &s ){ T res; istringstream iss( s ); iss >> res; return res; };
template < typename T > inline string toString( const T &a ){ ostringstream oss; oss << a; return oss.str(); };

#define REP( i, m, n ) for ( int i = (int)( m ); i < (int)( n ); ++i )
#define FOR( e, c ) for ( auto &e : c )
#define ALL( c ) (c).begin(), (c).end()
#define AALL( a, t ) (t*)a, (t*)a + sizeof( a ) / sizeof( t )
#define DRANGE( c, p ) (c).begin(), (c).begin() + p, (c).end()

#define PB( n ) push_back( n )
#define MP( a, b ) make_pair( ( a ), ( b ) )
#define EXIST( c, e ) ( (c).find( e ) != (c).end() )

#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl

bool f( const VT<LL> &csum, const int l, const int r )
{
	const int n = csum.size() - 1;

	const LL sum1 = csum[l];
	const LL sum2 = csum[ r + 1 ] - csum[l];
	const LL sum3 = csum[n] - csum[ r + 1 ];

	return sum1 <= sum2 && sum3 <= sum2;
}

LL limited_maximize( const VT<LL> &csum, const int l, const int r, const LL limit )
{
	if ( limit < csum[ l + 1 ] - csum[l] )
	{
		return LIM<LL>::min() / 4;
	}

	int lb = l, ub = r;

	while ( lb + 1 < ub )
	{
		const int mid = ( lb + ub ) / 2;

		( csum[ mid + 1 ] - csum[l] <= limit ? lb : ub ) = mid;
	}

	return csum[ lb + 1 ] - csum[l];
}

double solve()
{
	LL n, p, q, r, s;
	cin >> n >> p >> q >> r >> s;

	VT<LL> as( n );
	REP( i, 0, n )
	{
		as[i] = ( i * p + q ) % r + s;
	}

	const LL S = accumulate( ALL( as ), 0LL );

	VT<LL> csum( 1, 0 );
	partial_sum( ALL( as ), back_inserter( csum ) );

	LL res = 0;

	REP( i, 1, n )
	{
		const LL sum1 = csum[i];
		const LL sum2 = csum[n] - csum[i];

		res = max( res, min( sum1, sum2 ) );

		if ( sum2 < sum1 && sum1 - limited_maximize( csum, 0, i - 1, sum2 ) <= sum2 )
		{
			res = max( res, sum1 );
		}
		if ( sum1 < sum2 && sum2 - limited_maximize( csum, i, n - 1, sum1 ) <= sum1 )
		{
			res = max( res, sum2 );
		}
	}

	REP( l, 1, n )
	{
		int lb = l, ub = n - 1;
		while ( lb + 1 < ub )
		{
			const int mid = ( lb + ub ) / 2;
			( f( csum, l, mid ) ? ub : lb ) = mid;
		}

		if ( f( csum, l, ub ) )
		{
			res = max( res, S - ( csum[ ub + 1 ] - csum[l] ) );
		}
	}

	return double( res ) / S;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;

	cout << setprecision( 11 ) << fixed;

	REP( i, 0, t )
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}
