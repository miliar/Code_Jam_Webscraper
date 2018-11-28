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

// Binary Indexed Tree
class BinaryIndexedTree
{
private:
	int N;
	vector<int> data;

public:
	BinaryIndexedTree( const int n ) : N( n ), data( n + 1, 0 ) {}

	int sum( int i )
	{
		int res = 0;
		while ( 0 < i )
		{
			res += data[i];
			i -= i & -i;
		}
		return res;
	}

	void add( int i, const int x )
	{
		while ( i <= N )
		{
			data[i] += x;
			i += i & -i;
		}
	}
};
// int sum( 1-indexed pos )
// int add( pos, value )

int solve()
{
	int n;
	cin >> n;

	VI as( n );
	FOR( a, as )
	{
		cin >> a;
	}

	{
		VI bs = as;
		sort( ALL( bs ) );
		transform( ALL( as ), as.begin(), [&]( const int a ){ return lower_bound( ALL( bs ), a ) - bs.begin(); } );
	}

	VI v2idx( n );
	REP( i, 0, n )
	{
		v2idx[ as[i] ] = i + 1;
	}

	BinaryIndexedTree bit( n );

	int res = 0;
	REP( i, 0, n )
	{
		const int m = n - i;
		const int p = v2idx[i] - bit.sum( v2idx[i] ) - 1;

		res += min<int>( p, m - 1 - p );

		bit.add( v2idx[i], 1 );
	}

	return res;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;

	REP( i, 0, t )
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}


