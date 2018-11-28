#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int row[3][5];

int main() {

	freopen("a.in", "r", stdin);
	freopen("SalidaA.txt", "w", stdout);

	int tc, ntc = 0;
	int x, y, num;
	
	scanf("%d", &tc);
	
	while ( tc -- ) {
		ntc ++;
		
		scanf("%d", &x);
		
		for ( int i = 0; i < 4; i ++ ) {
			row[0][i] = 0;
			for ( int j = 0; j < 4; j ++ ) {
				scanf("%d", &num);
				row[0][i] |= (1 << num);
			}
		}
		
		scanf("%d", &y);
		
		for ( int i = 0; i < 4; i ++ ) {
			row[1][i] = 0;
			for ( int j = 0; j < 4; j ++ ) {
				scanf("%d", &num);
				row[1][i] |= (1 << num);
			}
		}
		
		int ans = row[0][x - 1] & row[1][y - 1], cont = 0, z;
		
		printf( "Case #%d: ", ntc );
		
		if ( ans == 0 ) {
			printf("Volunteer cheated!\n");
		} else {
			for ( int i = 1; i <= 16; i ++ ) {
				if ( ans & (1 << i) ) {
					cont ++;
					z = i;
				}
			}
			if ( cont > 1 )
				printf("Bad magician!\n");
			else
				printf("%d\n", z);
		}
	}

	return 0;
}
