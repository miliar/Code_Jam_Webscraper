#include <cstdio>

int main() {
	
	int T;
	scanf( "%d", &T );
	for ( int t = 1; t <= T; t++ ) {
		
		int cards[17];
		int last_answer = 0;
		int count_answer = 0;
		int row;
		
		for ( int i = 1; i <= 16; i++ ) cards[i] = 0;
		
		scanf( "%d", &row );
		for ( int r = 1; r <= 4; r++ ) {
			for ( int c = 1; c <= 4; c++ ) {
				
				int card;
				scanf( "%d", &card );
				if ( r == row ) {
					cards[card]++;
				}
				
			}
		}
		
		scanf( "%d", &row );
		for ( int r = 1; r <= 4; r++ ) {
			for ( int c = 1; c <= 4; c++ ) {
				
				int card;
				scanf( "%d", &card );
				if ( count_answer > 1 ) {
					continue;
				}
				
				if ( r == row ) {
					cards[card]++;
					if ( cards[card] == 2 ) {
						last_answer = card;
						count_answer++;
					}
				}
				
			}
		}
		
		if ( count_answer == 1 ) {
			printf( "Case #%d: %d\n", t, last_answer );
		} else if ( count_answer == 0 ) {
			printf( "Case #%d: Volunteer cheated!\n", t );
		} else {
			printf( "Case #%d: Bad magician!\n", t );
		}
		
	}
	
}