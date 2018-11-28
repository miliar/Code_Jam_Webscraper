#include <bits/stdc++.h>
using namespace std ;

typedef long long LL ;

#define clr( a , x ) memset ( a , x , sizeof a ) 

const int MAXN = 1 << 10 ;

int prime[MAXN] ;
int pri[MAXN] , cnt ;
int ans[11] ;
int n , m ;

void preprocess () {
	for ( int i = 2 ; i < MAXN ; ++ i ) {
		if ( !prime[i] ) pri[cnt ++] = i ;
		for ( int j = 0 ; j < cnt && i * pri[j] < MAXN ; ++ j ) {
			prime[i * pri[j]] = 1 ;
			if ( i % pri[j] == 0 ) continue ;
		}
	}
}

void solve () {
	scanf ( "%d%d" , &n , &m ) ;
	LL S = ( 1LL << ( n - 1 ) ) + 1 ;
	LL T = ( 1LL << n ) - 1 ;
	for ( LL i = S ; i <= T ; i += 2 ) {
		int ok = 1 ;
		for ( int j = 2 ; j <= 10 ; ++ j ) {
			int flag = 0 ;
			for ( int k = 0 ; k < 10 ; ++ k ) {
				LL v = i ;
				LL t = 1 , res = 0 ;
				while ( v ) {
					( res += ( v & 1 ) * t ) %= pri[k] ;
					( t *= j ) %= pri[k] ;
					v >>= 1 ;
				}
				if ( !res ) {
					flag = 1 ;
					ans[j] = pri[k] ;
					break ;
				}
			}
			if ( !flag ) ok = 0 ;
		}
		if ( ok ) {
			for ( int j = n - 1 ; j >= 0 ; -- j ) {
				printf ( "%d" , ( i >> j ) & 1 ) ;
			}
			for ( int j = 2 ; j <= 10 ; ++ j ) {
				printf ( " %d" , ans[j] ) ;
			}
			puts ( "" ) ;
			if ( 0 == -- m ) break ;
		}
	}
}

int main () {
	int T ;
	freopen ( "C-large.in" , "r" , stdin ) ;
	freopen ( "C-large.out" , "w" , stdout ) ;
	preprocess () ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d:\n" , i ) ;
		solve () ;
	}
	return 0 ;
}