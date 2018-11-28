#include <stdio.h>
#include <vector>
#include <stdlib.h>


using namespace std;


int main()
{

	int T, i;

	scanf( "%d\n", &T );

	int m, n, j, k, f;

	bool morir, nat;

	for ( i=0 ; i<T ; ++i ) {
	
		scanf( "%d %d\n", &n, &m );

		int jardin[n][m];

		for ( j=0 ; j<n ; ++j ) {
			for ( k=0 ; k<m ; ++k ) {
				scanf( "%d", &jardin[j][k] );
			}
		}

		for ( j=0 ; j<n ; ++j ) {
			for ( k=0 ; k<m ; ++k ) {
				morir = false;
				nat = false;
				for ( f=0 ; f<n ; ++f ) {
					if ( jardin[j][k] < jardin[f][k] ) {
						morir = true;
						break;
					}
				}
				for ( f=0 ; f<m ; ++f ) {
					if ( jardin[j][k] < jardin[j][f] ) {
						nat = true;
						break;
					}
				}
				
				if ( morir && nat ) {
					break;
				}
			}
			if (morir && nat) {
				break;
			}
		}


		if (morir && nat) {
			printf( "Case #%d: NO\n", i+1 );
		} else {
			printf( "Case #%d: YES\n", i+1 );
		}

	
	}
	

	return 0;
}
