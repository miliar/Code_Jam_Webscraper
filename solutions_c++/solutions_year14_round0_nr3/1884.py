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

bool isZeroCell( const VS &board, const int Y, const int X )
{
	const int H = board.size(), W = board[0].size();

	auto inside = [=]( const int y, const int x ){ return 0 <= y && y < H && 0 <= x && x < W; };

	REP( dy, -1, 2 )
	{
		REP( dx, -1, 2 )
		{
			if ( !( dy | dx ) )
			{
				continue;
			}

			const int ny = Y + dy;
			const int nx = X + dx;

			if ( inside( ny, nx ) && board[ ny ][ nx ] == '*' )
			{
				return false;
			}
		}
	}

	return true;
}

int dfs( const VS origBoard, VS &board, const int y, const int x )
{
	const int H = board.size(), W = board[0].size();

	if ( !( 0 <= y && y < H && 0 <= x && x < W ) || board[y][x] != '.' )
	{
		return 0;
	}

	int res = board[y][x] == '.';
	board[y][x] = '*';

	if ( !isZeroCell( origBoard, y, x ) )
	{
		return res;
	}

	REP( dy, -1, 2 )
	{
		REP( dx, -1, 2 )
		{
			if ( !( dy | dx ) )
			{
				continue;
			}

			const int ny = y + dy;
			const int nx = x + dx;
			res += dfs( origBoard, board, ny, nx );
		}
	}

	return res;
}

VS solve( const int R, const int C, const int M )
{
	if ( M + 1 == R * C )
	{
		VS res( R, string( C, '*' ) );
		res[0][0] = 'c';
		return res;
	}

	REP( h, 0, R )
	{
		REP( w, 0, C )
		{
			VS board( R, string( C, ' ' ) );
			int cnt = 0;

			REP( i, 0, R )
			{
				REP( j, 0, C )
				{
					board[i][j] = i <= h && j <= w && cnt < R * C - M ? '.' : '*';
					cnt += board[i][j] == '.';
				}
			}

			if ( cnt != R * C - M )
			{
				continue;
			}

			REP( i, 0, R )
			{
				REP( j, 0, C )
				{
					VS b = board;
					if ( board[i][j] == '.' && dfs( board, b, i, j ) == R * C - M )
					{
						board[i][j] = 'c';
						return board;
					}
				}
			}
		}
	}

	return VS( 1, "Impossible" );
}

inline void printBoard( const VS &board )
{
	copy( ALL( board ), ostream_iterator<string>( cout, "\n" ) );
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
		int r, c, m;
		cin >> r >> c >> m;
		cout << "Case #" << i + 1 << ":" << endl;

		{
			VS res = solve( r, c, m );
			if ( res[0] != "Impossible" )
			{
				printBoard( res );
				continue;
			}
		}
		{
			VS res = solve( c, r, m );
			if ( res[0] != "Impossible" )
			{
				VS res2( r, string( c, ' ' ) );
				REP( i, 0, r )
				{
					REP( j, 0, c )
					{
						res2[i][j] = res[j][i];
					}
				}

				printBoard( res2 );
				continue;
			}
		}
		cout << "Impossible" << endl;
	}

	return 0;
}
