#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

double Naomi[1111];
double Ken[1111];

int main() {
	
	freopen( "d.in", "r", stdin );
	freopen( "SalidaD.txt", "w", stdout );
	
	int tc, ntc = 0;
	int y, z, n;
	
	scanf("%d", &tc);
	
	while ( tc -- ) {
		
		scanf("%d", &n);
		ntc ++;
		
		for ( int i = 0; i < n; i ++ ) cin >> Naomi[i];
		for ( int i = 0; i < n; i ++ ) cin >> Ken[i];
		
		sort ( Naomi, Naomi + n );
		sort ( Ken, Ken + n );
		
		reverse ( Naomi, Naomi + n );
		reverse ( Ken, Ken + n );
		
		y = z = 0;
		int j = 0, jf;
		
		for ( int i = 0; i < n; i ++ ) {
			if ( Naomi[i] > Ken[j] )
				z ++;
			else
				j ++;
		}
		
		
		j = 0;
		jf = n - 1;
		
		for ( int i = 0; i < n; i ++ ) {
			if ( Naomi[j] > Ken[i] ) {
				y ++;
				j ++;
			}
		}
		
		printf("Case #%d: %d %d\n", ntc, y, z);
	}

	return 0;
}
