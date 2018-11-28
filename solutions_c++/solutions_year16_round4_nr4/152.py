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
const int N = 5;

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

char s[N][N];
bool cho[N];
int n, m, ret;
int p[N];

void preprocessing()
{
	scanf( "%d", &n );
	fo ( i, 0, n ) scanf( "%s", s[i] );
	ret = Inf;
}

bool search( int y )
{
	if ( y==n ) return 1;
	int x = p[y], any = 0;
	fo ( j, 0, n )
		if ( s[x][j]=='1' && !cho[j] ) 
		{
			cho[j] = 1;
			if ( !search( y + 1 ) )
				return 0;
			cho[j] = 0, any = 1;
		}
	return any;
}

bool check()
{
	fo ( i, 0, n ) p[i] = i;
	do
	{
		fill( cho, cho + n, 0 );
		if ( !search( 0 ) ) return 0;
	} while ( next_permutation( p, p + n ) );
	return 1;
}

void search( int x, int y, int cnt )
{
	if ( cnt >= ret ) return;
	if ( x==n )
	{
		if ( check() ) ret = min( ret, cnt );
		return;
	}
	if ( s[x][y]=='1' ) 
	{
		search( x+( y+1==n ), ( y+1 )%n, cnt );
		return;
	}
	else
	{
		s[x][y] = '1';
		search( x+( y+1==n ), ( y+1 )%n, cnt+1 );
		s[x][y] = '0';
		search( x+( y+1==n ), ( y+1 )%n, cnt );
	}
}

int main()
{
	freopen( "d.in", "r", stdin );
	freopen( "d.out", "w", stdout );

	int T; scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		printf( "Case #%d: ", Case+1 );
		preprocessing();
		search( 0, 0, 0 );
		printf( "%d\n", ret );
	}

	fclose( stdin ), fclose( stdout );
	return 0;
}

