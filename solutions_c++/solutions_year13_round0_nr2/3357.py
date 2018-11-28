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

string solve()
{
	int h, w;
	cin >> h >> w;

	VVI board( h, VI( w ) );
	FOR( line, board )
	{
		FOR( a, line )
		{
			cin >> a;
		}
	}

	REP( i, 0, h )
	{
		REP( j, 0, w )
		{
			bool horizontal = true, vertical = true;
			int height = board[i][j];

			REP( k, 0, w )
			{
				horizontal &= board[i][k] <= height;
			}
			REP( k, 0, h )
			{
				vertical &= board[k][j] <= height;
			}

			if ( !horizontal && !vertical )
			{
				return "NO";
			}
		}
	}

	return "YES";
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
