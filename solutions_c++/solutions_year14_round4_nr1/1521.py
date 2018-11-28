#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int arr[10100];
bool visit[10100];

int main () {
	
	freopen ( "a.in", "r", stdin );
	freopen ( "a.out", "w", stdout );

	int n, ntc, x, tc = 0;
	
	scanf ( "%d", &ntc );
	
	while ( ntc -- ) {
		
		tc ++;
		
		scanf ( "%d %d", &n, &x );
		
		for ( int i = 0; i < n; i ++ ) {
			scanf ( "%d", &arr[i] );
			visit[i] = false;
		}
		
		sort ( arr, arr + n );
		
		int cont = 0;
		
		for ( int i = n - 1; i >= 0; i -- ) {
			if ( visit[i] ) continue;
			
			visit[i] = true;
			cont ++;
			
			for ( int j = i - 1; j >= 0; j -- ) {
				if ( visit[j] ) continue;
				if ( arr[i] + arr[j] <= x  ) {
					visit[j] = true;
					break;
				}
			}
		}
		
		printf ( "Case #%d: %d\n", tc, cont );
		
	}

	return 0;
}
