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
const char note[4] = "PRS";
const int lose[3] = { 1, 2, 0 };

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

char s[N], S[N];
int a[N];
int R, P, Sc;
int n, m;

void solve( int sig, int l, int r )
{
	if ( r-l==1 ) { a[l] = sig; return; }
	int ano = lose[sig], mid = ( l + r ) >> 1;
	solve( sig, l, mid ), solve( ano, mid, r );
	bool flag = 0;
	fo ( k, 0, mid-l ) 
		if ( a[ l+k ] > a[ mid+k ] ) 
		{
			flag = 1;
			break;
		}
	if ( flag ) fo ( k, 0, mid-l )
		swap( a[ l+k ], a[ mid+k ] );
}

void preprocessing()
{
	fill( s, s + N, 0 ), fill( S, S + N, 0 );
	scanf( "%d%d%d%d", &n, &R, &P, &Sc ), m = 1<<n;
	fo ( i, 0, 3 ) 
	{
		solve( i, 0, m );
		int cnt[3] = { 0, 0, 0 };
		fo ( k, 0, m ) ++cnt[ a[k] ];
		if ( cnt[0]!=P || cnt[1]!=R || cnt[2]!=Sc ) continue;

		fo ( k, 0, m ) s[k] = note[ a[k] ];
		if ( S[0]=='\0' ) fo ( k, 0, ( 1<<n ) ) S[k] = s[k];
		else 
		{
			bool flag = 0;
			fo ( k, 0, ( 1<<n ) ) if ( s[k] < S[k] )
			{
				flag = 1;
				break;
			}
			if ( flag ) fo ( k, 0, ( 1<<n ) ) S[k] = s[k];
		}
	}
	if ( S[0]=='\0' )
	{
		printf( "IMPOSSIBLE\n" );
		return;
	}
	else S[m] = '\0';
	printf( "%s\n", S );
}

int main()
{
	freopen( "a.in", "r", stdin );
	freopen( "a.out", "w", stdout );

	int T; scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		printf( "Case #%d: ", Case+1 );
		preprocessing();
	}

	fclose( stdin ), fclose( stdout );
	return 0;
}

