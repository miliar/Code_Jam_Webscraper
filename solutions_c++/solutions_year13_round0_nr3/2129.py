#include<stdio.h>
int main()
{
	int T;
	int A, B;
	int a[5] = {1,4,9,121,484};
	scanf("%d", &T);
	int Case = 1;
	while ( T-- ) {
		scanf("%d%d", &A, &B);
		int count = 0;
		for ( int i = 0 ; i < 5 ; i++ ) {
			if ( A <= a[i] && a[i] <= B )
				count++;
		}
		printf("Case #%d: %d\n", Case++, count);
	}
	return 0;
}
