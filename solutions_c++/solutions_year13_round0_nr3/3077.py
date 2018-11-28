#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <numeric>
#include <iterator>

using namespace std;

typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;

#define REP( i, m, n ) for ( int i = (int)( m ); i < (int)( n ); ++i )
#define FOR( v, c ) for ( auto &v : c )

#define EACH( it, c ) for ( auto it = c.begin(); it != c.end(); ++it )
#define ALL( c ) (c).begin(), (c).end()

#define PB( n ) push_back( n )
#define MP( a, b ) make_pair( ( a ), ( b ) )
#define EXIST( c, e ) ( (c).find( e ) != (c).end() )

#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl
#define DEBUG( x ) cerr << __FILE__ << ":" << __LINE__ << ": " << #x << " = " << ( x ) << endl

bool isPalindrome( int n )
{
	OSS oss;
	oss << n;
	
	string str( oss.str() ), rev;
	reverse_copy( ALL( str ), back_inserter( rev ) );

	return str == rev;
}

int solve()
{
	int a, b;
	cin >> a >> b;

	int res = 0;
	REP( i, 1, b + 1 )
	{
		res += isPalindrome( i ) && a <= i * i && i * i <= b && isPalindrome( i * i );
	}
	return res;
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;

	REP( it, 0, t )
	{
		cout << "Case #" << it + 1 << ": " << solve() << endl;
	}

	return 0;
}
