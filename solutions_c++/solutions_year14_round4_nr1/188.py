#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 100000 + 100 ;

int a[ MAXN ] ;
bool use[ MAXN ] ;

int main() {
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;

	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		int n , m ;
		cin >> n >> m ;
		for ( int i = 0 ; i < n ; i ++ )
			cin >> a[ i ] ;

		sort( a , a + n ) ;
		memset( use , true , sizeof( use ) ) ;

		int ans = 0 ;
		for ( int i = n - 1 ; i >= 0 ; i -- ) 
			if ( use[ i ] ) {
				ans ++ ;
				use[ i ] = false ;
				int l = 0 , r = n - 1 , fnd = -1 ;
				while ( l <= r ) {
					int mid = ( l + r ) / 2 ;
					if ( a[ mid ] > m - a[ i ] )
						r = mid - 1 ;
					else {
						l = mid + 1 ;
						fnd = mid ;
					}
				}
				// cout << i  << ' ' << fnd << endl;
				while ( fnd > 0 && !use[ fnd ] )
					fnd -- ;
				if ( fnd >= 0 )
					use[ fnd ] = false ;
			}

		printf( "Case #%d: %d\n" , t , ans ) ;
	}
}
