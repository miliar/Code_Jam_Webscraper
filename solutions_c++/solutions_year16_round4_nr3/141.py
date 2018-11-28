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
const int N = 20, M = N * N * 4;

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

bool rev[N][N];
int fa[M], _f[M];
int num[N][N][4];
int po[ N<<2 ];
int n, m;

int getfa( int x )
{
	if ( fa[x]==x ) return x;
	return fa[x] = getfa( fa[x] );
}

void link( int x, int y )
{
	fa[ getfa( x ) ] = getfa( y );
}

void preprocessing()
{
	int ti = 0;
	scanf( "%d%d", &n, &m );
	fo ( i, 0, ( n+m )<<1 ) scanf( "%d", &po[i] ), --po[i];
	fo ( i, 0, n ) fo ( j, 0, m ) fo ( k, 0, 4 )
		_f[ti] = fa[ num[i][j][k] = ti ] = ti, ++ti;
	fo ( i, 0, n - 1 ) fo ( j, 0, m )
		link( num[i][j][2], num[ i+1 ][j][0] );
	fo ( i, 0, n ) fo ( j, 0, m - 1 )
		link( num[i][j][1], num[i][ j+1 ][3] );
	fo ( i, 0, M ) _f[i] = fa[i];
}

bool check()
{
	fo ( i, 0, M ) fa[i] = _f[i];
	fo ( i, 0, n ) fo ( j, 0, n )
	{
		if ( rev[i][j] ) link( num[i][j][0], num[i][j][3] ), link( num[i][j][1], num[i][j][2] );
		else link( num[i][j][0], num[i][j][1] ), link( num[i][j][2], num[i][j][3] );
	}
	fo ( i, 0, ( n+m )<<1 ) 
		fo ( j, 0, ( n+m )<<1 )
			if ( po[i]==po[j]^1 )
			{
				//int x = 
			}
	return 1;
}

void search( int x, int y )
{
	if ( x==n )
	{
		if ( check() )
		{
			fo ( i, 0, n ) 
			{
				fo ( j, 0, n ) printf( rev[i][j] ? "/" : "\\" );
				printf( "\n" );
			}
		}
		return;
	}
	rev[x][y] = 1;
	search( x+( y+1==n ), ( y+1 )%n );
	rev[x][y] = 0;
	search( x+( y+1==n ), ( y+1 )%n );
}

int main()
{
	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );

	preprocessing();
	search( 0, 0 );

	fclose( stdin ), fclose( stdout );
	return 0;
}

