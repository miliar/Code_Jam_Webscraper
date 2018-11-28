#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <bitset>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef double db;
typedef long long LL;
typedef pair< int, int > PII;
typedef pair< LL, LL > PLL;
typedef pair< db, db > PDD;

const db dInf = 1E90;
const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 205;

#define it iterator
#define rbg rbegin()
#define ren rend()
#define fdi( i, x ) for ( typeof( x.rbg ) i=x.rbg; i!=x.ren; ++i )
#define foi( i, x ) for ( typeof( x.begin() ) i=x.begin(); i!=x.end(); ++i )
#define fd( i, y, x ) for ( int i=( y )-1, LIM=x; i>=LIM; --i )
#define fo( i, x, y ) for ( int i=x, LIM=y; i<LIM; ++i )
#define mkp( A, B ) make_pair( A, B )
#define pub( x ) push_back( x )
#define pob( x ) pop_back( x )
#define puf( x ) push_front( x )
#define pof( x ) pop_front( x )
#define fi first
#define se second

pair < db, int > a[N];
bool cho[N], CHO[N];
db f[N][ N+N ];
int n, m, K;
db p[N], ret;

void preprocessing()
{
	scanf( "%d%d", &n, &m ), K = m / 2;
	fo ( i, 0, n ) scanf( "%lf", &p[i] );
	sort( p, p + n );
	ret = 0;
}

void update( db &x, db v ) { if ( v > x ) x = v; }

void solve()
{
	fill( f[0], f[ m+1 ], 0 ), f[0][K] = 1;
	int cnt = 0;
	fo ( i, 0, n ) 
	{
		if ( !cho[i] ) continue;
		fo ( k, -K, K+1 )
		{
			if ( !f[cnt][ k+K ] ) continue;
			f[ cnt+1 ][ k+K-1 ] += f[cnt][ k+K ] * ( 1-p[i] );
			f[ cnt+1 ][ k+K+1 ] += f[cnt][ k+K ] * p[i];
		}
		++cnt;
	}
	if ( ret < f[m][K] )
	{
		ret = f[m][K];
		//fo ( k, 0, n ) CHO[k] = cho[k];
	}
	//update( ret, f[m][K] );
}

void search()
{
	fill( cho, cho + n, 0 );
	fo ( i, 0, m ) cho[i] = 1;
	int bg = m, last = n;
	solve();

	fo ( i, 0, m )
	{
		cho[ --bg ] = 0, cho[ --last ] = 1;
		solve();
	}
}

/*void search( int x, int cnt )
{
	if ( x==n ) 
	{
		if ( cnt!=m ) return;
		solve(); return;
	}
	cho[x] = 0;
	search( x + 1, cnt );
	cho[x] = 1;
	search( x + 1, cnt + 1 );
	cho[x] = 0;
}*/

int main()
{
	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	int T; scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		printf( "Case #%d: ", Case+1 );
		preprocessing();
		search();
		printf( "%.10lf\n", ret );
		/*fo ( k, 0, n ) a[k] = mkp( p[k], CHO[k] );
		sort( a, a + n );
		fo ( k, 0, n ) printf( "%.2lf ", a[k].fi );
		printf( "\n" );
		fo ( k, 0, n ) printf( "%d    ", a[k].se );
		printf( "\n" );
		printf( "\n" );*/
	}

	fclose( stdin ), fclose( stdout );
	return 0;
}

