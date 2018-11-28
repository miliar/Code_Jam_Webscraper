#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std ;

typedef long long LL ;

#define clr( a , x ) memset ( a , x , sizeof a )
#define ls ( o << 1 )
#define rs ( o << 1 | 1 )
#define lson ls , l , m
#define rson rs , m + 1 , r
#define mid ( ( l + r ) >> 1 )
#define root 1 , 1 , cnt

const int MAXN = 105 ;

char G[MAXN][MAXN] ;
int U[MAXN][MAXN] , D[MAXN][MAXN] , L[MAXN][MAXN] , R[MAXN][MAXN] ;
int n , m ;

void solve () {
	clr ( U , 0 ) ;
	clr ( D , 0 ) ;
	clr ( L , 0 ) ;
	clr ( R , 0 ) ;
	scanf ( "%d%d" , &n , &m ) ;
	for ( int i = 0 ; i < n ; ++ i ) {
		scanf ( "%s" , G[i] ) ;
	}
	for ( int i = 0 ; i < n ; ++ i ) {
		for ( int j = 0 ; j < m ; ++ j ) {
			if ( i && G[i - 1][j] != '.' ) U[i][j] = 1 ;
			else if ( i ) U[i][j] = U[i - 1][j] ;
			if ( j && G[i][j - 1] != '.' ) L[i][j] = 1 ;
			else if ( j ) L[i][j] = L[i][j - 1] ;
		}
	}
	for ( int i = n - 1 ; i >= 0 ; -- i ) {
		for ( int j = m - 1 ; j >= 0 ; -- j ) {
			if ( i < n - 1 && G[i + 1][j] != '.' ) D[i][j] = 1 ;
			else if ( i < n - 1 ) D[i][j] = D[i + 1][j] ;
			if ( j < m - 1 && G[i][j + 1] != '.' ) R[i][j] = 1 ;
			else if ( j < m - 1 ) R[i][j] = R[i][j + 1] ;
		}
	}
	int ans = 0 ;
	for ( int i = 0 ; i < n ; ++ i ) {
		for ( int j = 0 ; j < m ; ++ j ) if ( G[i][j] != '.' ) {
			if ( !U[i][j] && !D[i][j] && !L[i][j] && !R[i][j] ) {
				printf ( "IMPOSSIBLE\n" ) ;
				return ;
			}
			if ( G[i][j] == '>' && !R[i][j] ) ++ ans ;
			if ( G[i][j] == '<' && !L[i][j] ) ++ ans ;
			if ( G[i][j] == '^' && !U[i][j] ) ++ ans ;
			if ( G[i][j] == 'v' && !D[i][j] ) ++ ans ;
		}
	}
	printf ( "%d\n" , ans ) ;
}

int main () {
	int T ;
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d: " , i ) ;
		solve() ;
	}
	return 0 ;
}