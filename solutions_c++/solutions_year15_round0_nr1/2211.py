#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1000 + 100 ;
int n ;
int a[ MAXN ] ;

int main() {
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	int test_case ;
	cin >> test_case ;

	for ( int t = 1 ; t <= test_case ; t ++ ) {
		cin >> n ;
		for ( int i = 0 ; i <= n ; i ++ ) {
			char c ;
			cin >> c ;
			while ( c < '0' || c > '9' )
				cin >> c ;
			a[ i ] = c - '0' ;
		}

		int ans = 0 ;
		int stand = 0 ;

		for ( int i = 0 ; i <= n ; i ++ ) {
			if ( stand >= i )
				stand += a[ i ] ;
			else {
				ans += i - stand ;
				stand = i + a[ i ] ;
			}
		}

		printf( "Case #%d: %d\n" , t , ans ) ;
	}
}