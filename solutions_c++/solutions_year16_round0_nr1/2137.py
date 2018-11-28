#include <bits/stdc++.h>
using namespace std ;

typedef long long LL ;

#define clr( a , x ) memset ( a , x , sizeof a ) 

int vis[10] ;

void solve () {
	int n , cnt = 10 ;
	scanf ( "%d" , &n ) ;
	if ( !n ) {
		printf ( "INSOMNIA\n" ) ;
		return ;
	}
	memset ( vis , 0 , sizeof vis ) ;
	for ( int i = 1 ; ; ++ i ) {
		int t = n * i ;
		while ( t ) {
			if ( !vis[t % 10] ) -- cnt ;
			vis[t % 10] = 1 ;
			t /= 10 ;
		}
		if ( !cnt ) {
			printf ( "%d\n" , n * i ) ;
			return ;
		}
	}
}

int main () {
	int T ;
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}