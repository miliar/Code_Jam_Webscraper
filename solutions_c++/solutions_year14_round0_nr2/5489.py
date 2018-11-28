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

using namespace std;

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

double solve()
{
	double c, f, x;
	cin >> c >> f >> x;

	double res = LIM<double>::max(), t = 0, r = 2;
	while ( t < res )
	{
		res = min( res, t + x / r );
		t += c / r;
		r += f;
	}

	return res;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;

	cout << setprecision( 7 ) << fixed << endl;

	REP( i, 0, t )
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}
