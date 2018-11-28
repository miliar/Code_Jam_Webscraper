#include <iostream>
#include <cstdio>

int main()
{
	int test;
	int n,m, u = 1;
	scanf ( "%d", &test );
	while (u <= test) {
		scanf ( "%d%d", &n, &m );
		int a[n][m];
		int mar[n];
		int marc[m];
		int b[n][m];
		for ( int i = 0; i < n; i++) {
			for ( int j = 0; j < m; j++) {
				scanf ( "%d", &a[i][j] );
				b[i][j] = 100;
			}
		}

		int max = -1,max1 = -1;
		for ( int i = 0; i < n; i++) {
			max1 = -1;
			for ( int j = 0; j < m; j++) {
				if ( max1 < a[i][j] ) {
					max1 = a[i][j];
					mar[i] = max1;
//					printf ( "max1 = %d\n", max1 );
				}
			}
		}
		for ( int i = 0; i < m; i++) {
			max = -1;
			for ( int j = 0; j < n; j++) {
				if ( max < a[j][i] ) {
					max = a[j][i];
					marc[i] = max;
//					printf ( "max = %d\n", max );
				}
			}
		}
	//	for ( int i = 0; i < n; i++) {
	//		printf ( "%d\t", mar[i] );
	//	}
	//	printf ( "\n");
	//	for ( int i = 0; i < m; i++) {
	//		printf ( "%d\t", marc[i] );
	//	}
	//	printf ( "\n");
		for ( int i = 0; i < n; i++) {
			for ( int j = 0; j < m; j++) {
				if ( b[i][j] > mar[i] ) {
					b[i][j] = mar[i];
				}
			}
		}
		for ( int i = 0; i < m; i++) {
			for ( int j = 0; j < n; j++) {
				if ( b[j][i] > marc[i] ) {
			      		 b[j][i] = marc[i];
				}
			}
		}
		int flag = 0;
		for ( int i = 0; i < n; i++) {
			for ( int j = 0; j < m; j++) {
				if ( a[i][j] != b[i][j] ) {
					flag = 1;
					break;
				}
			}
		}	
		if ( flag == 1 ) {
			printf ( "Case #%d: NO\n", u);
		}else {
			printf ( "Case #%d: YES\n", u);
		}
		u++;
	}
	return 0;
}

