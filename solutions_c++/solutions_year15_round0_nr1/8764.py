#include<stdio.h>

int main ( void )	{
	int T;
	int test, i, k, n, ans;
	char str[1010];

	scanf ( "%d", &T );

	for ( test = 1 ; test <= T ; test++ )	{
		scanf ( "%d", &n );
		scanf ( "%s", str );

		k = str[0] - '0';
		ans = 0;

		for ( i = 1 ; i <= n ; i++ )	{
			if ( k < i )	{
				ans += ( i - k );
				k = i;
			}

			k += str[i] - '0';
		}

		printf ( "Case #%d: %d\n", test, ans );
	}

	return 0;
}