#include <bits/stdc++.h>
using namespace std ;

const int MAXN = 205 ;

int n , K ;

double p[MAXN] ;
double dp[MAXN][MAXN] ;

void solve () {
	double ans = 0 ;
	scanf ( "%d%d" , &n , &K ) ;
	for ( int i = 1 ; i <= n ; ++ i ) {
		scanf ( "%lf" , &p[i] ) ;
	}
	sort ( p + 1 , p + n + 1 ) ;
	for ( int i = 0 ; i <= K ; ++ i ) {
		memset ( dp , 0 , sizeof dp ) ;
		dp[0][0] = 1 ;
		for ( int j = 1 ; j <= K ; ++ j ) {
			double c ;
			if ( j <= i ) c = p[j] ;
			else c = p[n - ( j - i ) + 1] ;
			for ( int k = 0 ; k <= K ; ++ k ) {
				dp[j][k] = dp[j - 1][k] * ( 1 - c ) + ( !k ? 0 : dp[j - 1][k - 1] * c );
			}
		}
		ans = max ( ans , dp[K][K >> 1] ) ;
	}
	printf ( "%.6f\n" , ans ) ;
}

int main () {
	int T ;
	freopen ( "B-large.in" , "r" , stdin ) ;
	freopen ( "B-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}