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

const int dy[] = { 0, 1, 0, -1 };
const int dx[] = { 1, 0, -1, 0 };

// Å‘å—¬i Dinic –@ j O( |E||V|^2 )
class Dinic
{
	struct Edge
	{
		int to, cap, rev;
		Edge( int t, int c, int r ) : to( t ), cap( c ), rev( r ) {}
	};

	vector< vector<Edge> > G;
	vector<int> distance, done;

public:
	Dinic( int V ) : G( V ), distance( V ), done( V )
	{
		return;
	}

	void connect( int from, int to, int cost )
	{
		G[ from ].push_back( Edge( to, cost, G[ to ].size() ) );
		G[ to ].push_back( Edge( from, 0, G[ from ].size() - 1 ) );
		return;
	}

	int solve( int s, int t )
	{
		int res = 0;
		while ( true )
		{
			bfs( s );
			if ( distance[t] < 0 )
			{
				return res;
			}

			fill( done.begin(), done.end(), 0 );
			for ( int f; ( f = dfs( s, t, numeric_limits<int>::max() ) ) > 0; res += f );
		}
	}

private:
	void bfs( int s )
	{
		fill( distance.begin(), distance.end(), -1 );
		distance[s] = 0;
		
		queue<int> que;
		que.push( s );
		while ( !que.empty() )
		{
			int v = que.front();
			que.pop();

			for ( int i = 0; i < (int)G[v].size(); ++i )
			{
				Edge &e = G[v][i];
				if ( e.cap > 0 && distance[ e.to ] < 0 )
				{
					distance[ e.to ] = distance[v] + 1;
					que.push( e.to );
				}
			}
		}

		return;
	}

	int dfs( int v, int t, int f )
	{
		if ( v == t )
		{
			return f;
		}

		for ( int &i = done[v]; i < (int)G[v].size(); ++i )
		{
			Edge &e = G[v][i];
			if ( e.cap > 0 && distance[v] < distance[ e.to ] )
			{
				int d = dfs( e.to, t, min( f, e.cap ) );
				if ( d > 0 )
				{
					e.cap -= d;
					G[ e.to ][ e.rev ].cap += d;
					return d;
				}
			}
		}

		return 0;
	}
};
// Dinic( |V| )
// connect( from, to, cap )
// solve( s, t )

int solve()
{
	int w, h, b;
	cin >> w >> h >> b;

	VVI board( h, VI( w ) );
	REP( i, 0, b )
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		REP( y, y1, y2 + 1 )
		{
			REP( x, x1, x2 + 1 )
			{
				board[y][x]++;
			}
		}
	}

	Dinic maxflow( h * w * 2 + 2 );
	// [ 0, h * w ) := in
	// [ h * w, h * w * 2 ) := out
	const int HW = h * w;
	const int SRC = HW * 2;
	const int SINK = SRC + 1;

	REP( i, 0, w )
	{
		if ( board[0][i] == 0 )
		{
			maxflow.connect( SRC, i, 1 );
		}
		if ( board.back()[i] == 0 )
		{
			maxflow.connect( HW + ( h - 1 ) * w + i, SINK, 1 );
		}
	}

	REP( i, 0, h )
	{
		REP( j, 0, w )
		{
			maxflow.connect( i * w + j, HW + i * w + j, 1 );
			if ( board[i][j] == 1 )
			{
				continue;
			}
			
			REP( d, 0, 4 )
			{
				const int ny = i + dy[d];
				const int nx = j + dx[d];
				
				if ( !( 0 <= ny && ny < h && 0 <= nx && nx < w ) || board[ ny ][ nx ] == 1 )
				{
					continue;
				}

				maxflow.connect( HW + i * w + j, ny * w + nx, 1 );
			}
		}
	}

	return maxflow.solve( SRC, SINK );
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
