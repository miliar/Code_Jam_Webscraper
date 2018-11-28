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

using namespace std; using namespace placeholders;

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
template < typename T > inline T fromString( const string &s ) { T res; istringstream iss( s ); iss >> res; return res; };
template < typename T > inline string toString( const T &a ) { ostringstream oss; oss << a; return oss.str(); };

#define REP2( i, n ) REP3( i, 0, n )
#define REP3( i, m, n ) for ( int i = ( int )( m ); i < ( int )( n ); ++i )
#define GET_REP( a, b, c, F, ... ) F
#define REP( ... ) GET_REP( __VA_ARGS__, REP3, REP2 )( __VA_ARGS__ )
#define FOR( e, c ) for ( auto &e : c )
#define ALL( c ) ( c ).begin(), ( c ).end()
#define AALL( a, t ) ( t* )a, ( t* )a + sizeof( a ) / sizeof( t )
#define DRANGE( c, p ) ( c ).begin(), ( c ).begin() + ( p ), ( c ).end()

#define SZ( v ) ( (int)( v ).size() )
#define PB push_back
#define EM emplace
#define EB emplace_back
#define BI back_inserter

#define EXIST( c, e ) ( ( c ).find( e ) != ( c ).end() )

#define MP make_pair
#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl

constexpr int dy[] = { -1, 0, 1, 0 };
constexpr int dx[] = { 0, 1, 0, -1 };
const string arrows = "^>v<";

// Å¬”ï—p—¬ O( F |E| log |V| )
class MinimumCostFlow
{
private:
	struct Edge
	{
		int to, cap, cost, rev;
		Edge( int t, int c, int d, int r ) : to( t ), cap( c ), cost( d ), rev( r ) {}
	};

	const int V;
	vector< vector<Edge> > G;

public:
	MinimumCostFlow( int v ) : V( v ), G( V ) {};

	void connect( int from, int to, int cap, int cost )
	{
		G[ from ].push_back( Edge( to, cap, cost, G[ to ].size() ) );
		G[ to ].push_back( Edge( from, 0, -cost, G[ from ].size() - 1 ) );
		return;
	}

	int solve( int s, int t, int f )
	{
		int res = 0;
		vector<int> h( V, 0 ), prevv( V ), preve( V );

		while ( 0 < f )
		{
			vector<int> distance( V, INT_MAX );
			distance[s] = 0;

			priority_queue< pair<int,int>, vector< pair<int,int> >, greater< pair<int,int> > > que;
			que.push( make_pair( 0, s ) );
			
			while ( !que.empty() )
			{
				int d = que.top().first;
				int v = que.top().second;
				que.pop();

				if ( distance[v] < d )
				{
					continue;
				}

				for ( int i = 0; i < (int)G[v].size(); ++i )
				{
					Edge &e = G[v][i];
					if ( 0 < e.cap && distance[v] + e.cost + h[v] - h[ e.to ] < distance[ e.to ] )
					{
						distance[ e.to ] = distance[v] + e.cost + h[v] - h[ e.to ];
						prevv[ e.to ] = v;
						preve[ e.to ] = i;
						que.push( make_pair( distance[ e.to ], e.to ) );
					}
				}
			}

			if ( distance[t] == INT_MAX )
			{
				return -1;
			}

			for ( int i = 0; i < V; ++i )
			{
				h[i] += distance[i];
			}

			int d = f;
			for ( int v = t; v != s; v = prevv[v] )
			{
				d = min( d, G[ prevv[v] ][ preve[v] ].cap );
			}
			f -= d;
			res += d * h[t];
			for ( int v = t; v != s; v = prevv[v] )
			{
				Edge &e = G[ prevv[v] ][ preve[v] ];
				e.cap -= d;
				G[v][ e.rev ].cap += d;
			}
		}

		return res;
	}

	int solve2( const int s, const int t, int f )
	{
		const int INF = INT_MAX / 2;
		int res = 0;

		while ( f > 0 )
		{
			vector<int> dist( V, INF );
			dist[s] = 0;
			vector<int> prevv( V ), preve( V );

			bool update = true;
			while ( update )
			{
				update = false;

				for ( int v = 0; v < V; v++ )
				{
					if ( dist[v] == INF )
					{
						continue;
					}
					for ( int i = 0; i < (int)G[v].size(); i++ )
					{
						Edge &e = G[v][i];
						if ( e.cap > 0 && dist[ e.to ] > dist[v] + e.cost )
						{
							dist[ e.to ] = dist[v] + e.cost;
							prevv[ e.to ] = v;
							preve[ e.to ] = i;
							update = true;
						}
					}
				}
			}

			if ( dist[t] == INF )
			{
				return -1;
			}

			int d = f;
			for ( int v = t; v != s; v = prevv[v] )
			{
				d = min( d, G[ prevv[v] ][ preve[v] ].cap );
			}
			f -= d;
			res += d * dist[t];
			for ( int v = t; v != s; v = prevv[v] )
			{
				Edge &e = G[ prevv[v] ][ preve[v] ];
				e.cap -= d;
				G[v][ e.rev ].cap += d;
			}
		}

		return res;
	}
};
// MinimumCostFlow( |V| )
// connect( from, to, cap, cost )
// solve( s, t, f ) :  Primal-Dual O( F |E| log |V| )
// solve2( s, t, f ) : Bellman-Ford O( F |E| |V| )

int solve()
{
	int H, W;
	cin >> H >> W;

	auto inside = [&]( const int y, const int x ){ return 0 <= y && y < H && 0 <= x && x < W; };

	VS board( H );
	cin >> board;

	int num = 0;
	map< PII, int > arr2id;

	REP( i, H )
	{
		REP( j, W )
		{
			if ( board[i][j] == '.' )
			{
				continue;
			}

			arr2id[ MP( i, j ) ] = num++;
		}
	}

	VT< VPII > mapping( num );

	REP( i, H )
	{
		REP( j, W )
		{
			if ( board[i][j] == '.' )
			{
				continue;
			}

			const int id = arr2id[ MP( i, j ) ];

			REP( d, 4 )
			{
				for ( int y = i, x = j; inside( y, x ); y += dy[d], x += dx[d] )
				{
					if ( ( y == i && x == j ) || board[y][x] == '.' )
					{
						continue;
					}

					const int to = arr2id[ MP( y, x ) ];
					mapping[ id ].EB( to, arrows[d] != board[i][j] );
					break;
				}
			}
		}
	}

	MinimumCostFlow mcf( num * 2 + 2 );
	// [ 0, num ) := from
	// [ num, 2 * num ) := to
	const int SRC = 2 * num;
	const int SINK = SRC + 1;

	REP( i, num )
	{
		mcf.connect( SRC, i, 1, 0 );
		mcf.connect( num + i, SINK, num, 0 );
	}

	REP( from, num )
	{
		FOR( e, mapping[ from ] )
		{
			const int to = e.fst;
			const int cost = e.snd;

			mcf.connect( from, num + to, 1, cost );
		}
	}

	return mcf.solve( SRC, SINK, num );
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int T;
	cin >> T;

	REP( i, T )
	{
		const int res = solve();
		cout << "Case #" << i + 1 << ": ";
		if ( res == -1 )
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << res << endl;
		}
	}

	return 0;
}
