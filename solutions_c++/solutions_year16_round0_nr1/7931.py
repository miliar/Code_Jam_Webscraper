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
const int N = 100005;

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

bool done[10];
int n;

void chk( int &cnt, int x )
{
	for ( ; x; x/=10 )
		cnt += !done[ x%10 ], done[ x%10 ] = 1;
}

void preprocessing()
{
	scanf( "%d", &n );
	fill( done, done + 10, 0 );
}

int solve()
{
	if ( !n ) return -1;
	int cnt = 0;
	for ( int i=n; cnt<10; i+=n )
	{
		chk( cnt, i );
		if ( cnt==10 ) return i;
	}
	return -1;
}

int main()
{
	freopen( "count.in", "r", stdin );
	freopen( "count.out", "w", stdout );

	int T; scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		preprocessing();
		int temp = solve();
		printf( "Case #%d: ", Case + 1 );
		if ( temp<0 ) printf( "INSOMNIA\n" );
		else printf( "%d\n", temp );
	}

	fclose( stdin ), fclose( stdout );
	return 0;
}

