#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1000 +100 ;
const int MAXANS = 1000 + 100 ;

int n ;
int a[ MAXN ] ;

int main() {
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;

	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		cin >> n ;
		for ( int i = 0 ; i < n ; i ++ ) 
			cin >> a[ i ] ;

		int ans = -1 ;
		for ( int p = 1 ; p <= MAXANS ; p ++ ) {
			int cici = 0 ;
			for ( int i = 0 ; i < n ; i ++ ) 
				if ( a[ i ] > p ) {
					cici += ( a[ i ] / p ) ;
					if ( a[ i ] % p == 0 ) cici -- ;
				}
			// cout << p << ' ' << cici << endl;
			if ( ans == -1 || cici + p < ans ) {
				ans = cici + p ;
			}
		}

		printf( "Case #%d: %d\n" , t , ans ) ;		
	}
}
