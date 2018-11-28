#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int min( int a , int b ) {
	if ( a < b ) return a ;
	return b ;
}

int main() {
	freopen( "D-small-attempt0.in" , "r" , stdin ) ;
	freopen( "D-small-attempt0.out" , "w" , stdout ) ;

	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		int x , r , c ;
		cin >> x >> r >> c ;
		string ans = "" ;
		if ( x == 1 )
			ans = "GABRIEL" ;
		if ( x == 2 ) {
			if ( r * c % 2 == 0 )
				ans = "GABRIEL" ;
			else 
				ans = "RICHARD" ;
		}
		if ( x == 3 ) {
			if ( r * c % 3 == 0 && min( r , c ) >= 2 )
				ans = "GABRIEL" ;
			else
				ans = "RICHARD" ;
		}
		if ( x == 4 ) { 
			if ( r * c % 4 == 0 && min( r , c ) >= 3 )
				ans = "GABRIEL" ;
			else
				ans = "RICHARD" ;
		}
		printf( "Case #%d: " , t ) ;
		cout << ans << endl;
	}
}
