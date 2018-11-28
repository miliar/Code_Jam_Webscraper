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

int m, n;
VS ss( m );

VT<VS> ts;
int res1, res2;

void construct()
{
	int size = 0;

	FOR( t, ts )
	{
		if ( t.empty() )
		{
			return;
		}
	}

	FOR( t, ts )
	{
		set<string> prefixes;
		prefixes.insert( string() );
		
		FOR( s, t )
		{
			string tmp;
			FOR( c, s )
			{
				tmp += c;
				prefixes.insert( tmp );
			}
		}

		size += prefixes.size();
	}

	if ( res1 < size )
	{
		res1 = size;
		res2 = 1;
	}
	else if ( size == res1 )
	{
		res2++;
	}

	return;
}

void dfs( const int idx )
{
	if ( idx == m )
	{
		construct();
		return;
	}

	REP( i, 0, n )
	{
		ts[i].PB( ss[ idx ] );
		dfs( idx + 1 );
		ts[i].pop_back();
	}

	return;
}

void solve()
{
	cin >> m >> n;
	
	ss = VS( m );
	FOR( s, ss )
	{
		cin >> s;
	}

	res1 = res2 = 0;
	ts = VT<VS>( n );
	dfs( 0 );

	return;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;

	REP( i, 0, t )
	{
		solve();
		cout << "Case #" << i + 1 << ": " << res1 << ' ' << res2 << endl;
	}

	return 0;
}
