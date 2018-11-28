#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

typedef long long ll ;

int T , k , c , s ;

int main() {
	freopen( "D.in" , "r" , stdin ) ;
	freopen( "D.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int test = 1 ; test <= T ; test ++ ) {
		printf( "Case #%d:" , test ) ;
		scanf( "%d%d%d" , &k , &c , &s ) ;
		int Num = k / c + (k % c != 0) ;
		if ( s < Num ) { printf( " IMPOSSIBLE\n" ) ; continue ; }
		ll tot = Num * c ;
		for (int i = 1 ; i <= Num ; i ++ ) {
			ll Mul = 1 , Ans = 0 , delta ;
			for (int j = 1 ; j <= c ; j ++ ) {
				delta = min( tot , (ll) k ) ;
				Ans += ( j > 1 ? delta - 1 : delta ) * Mul ;
				Mul *= k ;
				tot -- ;
			}
			printf( " %I64d" , Ans ) ;
		}
		cout << endl ;
	}
	return 0 ;
}
