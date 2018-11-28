#include <cstdio>

int n , m;
int a[128][128];

void read() {
	int i , j;
	
	scanf ( "%d%d" , &n , &m );
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			scanf ( "%d" , &a[i][j] );
		}
	}
}

int solve() {
	int i , j , k;
	int ok1 , ok2;
	
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			ok1 = ok2 = 1;
			
			for (k = 0; k < n; k++) {
				if ( a[k][j] > a[i][j] ) {
					ok1 = 0;
				}
			}
			
			for (k = 0; k < m; k++) {
				if ( a[i][k] > a[i][j] ) {
					ok2 = 0;
				}
			}
			
			if ( !ok1 && !ok2 ) {
				return 0;
			}
		}
	}
	
	return 1;
}

int main() {
	int cases;
	int i;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: %s\n" , i , solve() ? "YES" : "NO" );
	}
	
	return 0;
}
