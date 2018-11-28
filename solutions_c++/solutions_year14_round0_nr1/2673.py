#include<stdio.h>
int rA, rB;
int A[5][5];
int B[5][5];
int main()
{
	int T;
	int Case = 1;
	scanf("%d", &T);
	while ( T-- ) {
		scanf("%d", &rA);
		for ( int i = 1 ; i <= 4 ; i++ ) {
			for ( int j = 1 ; j <= 4 ; j++ ) {
				scanf("%d", &A[i][j]);
			}
		}
		scanf("%d", &rB);
		for ( int i = 1 ; i <= 4 ; i++ ) {
			for ( int j = 1 ; j <= 4 ; j++ ) {
				scanf("%d", &B[i][j]);
			}
		}
		int ans = -1;
		for ( int i = 1 ; i <= 4 ; i++ ) {
			for ( int j = 1 ; j <= 4 ; j++ ) {
				if ( A[rA][i] == B[rB][j] ) {
					if ( ans == -1 )
						ans = A[rA][i];
					else if ( ans != -1 ) 
						ans = -2;
				}
			}
		}
		if ( ans > 0 )
			printf("Case #%d: %d\n", Case++, ans);
		else if ( ans == -2 )
			printf("Case #%d: Bad magician!\n", Case++);
		else
			printf("Case #%d: Volunteer cheated!\n", Case++);
	}
	return 0;
}
