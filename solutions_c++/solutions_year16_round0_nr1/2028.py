#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

typedef long long ll ;

bool bz[20] ;
int T , tot ;
ll n , ans ;

void DIV( ll m ) {
	while ( m ) {
		int num = m % 10 ;
		if ( !bz[num] ) tot -- ;
		bz[num] = 1 ;
		m /= 10 ;
	}
}

int main() {
	freopen( "A.in" , "r" , stdin ) ;
	freopen( "A.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int k = 1 ; k <= T ; k ++ ) {
		memset( bz , 0 , sizeof(bz) ) ;
		scanf( "%I64d" , &n ) ;
		printf( "Case #%d: " , k ) ;
		if ( n == 0 ) { printf( "INSOMNIA\n" ) ; continue ; }
		tot = 10 ;
		for (ll i = 1 ; tot ; i ++ ) {
			ll m = n * i ;
			DIV( m ) ;
			ans = m ;
		}
		printf( "%I64d\n" , ans ) ;
	}
	return 0 ;
}
