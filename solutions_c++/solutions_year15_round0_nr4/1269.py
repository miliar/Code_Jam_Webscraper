#include <cstdio>
#include <cstring>
#include <map>
#include <math.h>
#include <algorithm>
using namespace std ;

typedef long long LL ;

#define rep( i , a , b ) for ( int i = ( a ) ; i <  ( b ) ; ++ i )
#define For( i , a , b ) for ( int i = ( a ) ; i <= ( b ) ; ++ i )
#define rev( i , a , b ) for ( int i = ( a ) ; i >= ( b ) ; -- i )
#define clr( a , x ) memset ( a , x , sizeof a )

const int MAXN = 1005 ;
const int INF = 0x3f3f3f3f ;

int G[5][5][5] ;

void preprocess () {
	clr ( G , 0 ) ;
	G[2][1][1] = 1 ;
	G[2][1][3] = 1 ;
	G[2][3][1] = 1 ;
	G[2][3][3] = 1 ;
	G[3][1][1] = 1 ;
	G[3][1][2] = 1 ;
	G[3][1][3] = 1 ;
	G[3][1][4] = 1 ;
	G[3][2][1] = 1 ;
	G[3][2][2] = 1 ;
	G[3][2][4] = 1 ;
	G[3][3][1] = 1 ;
	G[3][4][1] = 1 ;
	G[3][4][2] = 1 ;
	G[3][4][4] = 1 ;
	G[4][1][1] = 1 ;
	G[4][1][2] = 1 ;
	G[4][1][3] = 1 ;
	G[4][1][4] = 1 ;
	G[4][2][1] = 1 ;
	G[4][2][2] = 1 ;
	G[4][2][3] = 1 ;
	G[4][2][4] = 1 ;
	G[4][3][1] = 1 ;
	G[4][3][2] = 1 ;
	G[4][3][3] = 1 ;
	G[4][4][1] = 1 ;
	G[4][4][2] = 1 ;
}

void solve () {
	int a , b , c ;
	scanf ( "%d%d%d" , &a , &b , &c ) ;
	if ( G[a][b][c] ) printf ( "RICHARD\n" ) ;
	else printf ( "GABRIEL\n" ) ;
}

int main () {
	int T ;
	freopen ( "D-small-attempt1.in" , "r" , stdin ) ;
	freopen ( "D-small-attempt1.out" , "w" , stdout ) ;
	preprocess () ;
	scanf ( "%d" , &T ) ;
	For ( i , 1 , T ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}