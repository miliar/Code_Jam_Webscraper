# include <iostream>
# include <cstdio>

using namespace std ;

int main ( ) {
	ios_base::sync_with_stdio ( false ) ;
	int tc , count ; cin >> tc ;

	for ( count = 1 ; count <= tc ; ++count ) {
		int n ; cin >> n ;
		int temp = 0 , a[10]={0} , flag , i , j = 1 ;

		if ( n == 0 ) {
			printf ( "Case #%d: INSOMNIA\n" , count ) ;
			continue ;
		}

		while ( j ) {
			flag = 1 ;
			temp = n*j ;
			while ( temp > 0 ) {
				a[temp%10] = 1 ;
				temp /= 10 ;
			}

			for ( i = 0 ; i < 10 ; ++i ) {
				if ( a[i] == 0 )
					flag = 0 ;
			}

			if ( flag == 1 ) {
				printf ( "Case #%d: %d\n" , count , n*j ) ;
				break ;
			}
			
			j += 1 ;
		}
	}

	return 0 ;
}
