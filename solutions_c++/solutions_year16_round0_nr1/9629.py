#include <bits/stdc++.h>

using namespace std;

int main()
{
	int test;
	cin >> test;

	for( int te = 1; te <= test; te++ )
	{
		long long n;
		cin >> n;

		long long m = n;
		int upto = 10000;

		int msk = 0;

		for( int i = 1; i <= upto; i++, m += n )
		{
			long long t = m;

			/* printf( "%11lld - ", t ); */

			while( t )
			{
				msk |= ( 1 << ( t % 10 ) );
				t /= 10;
			}

			/* int tm = msk;
			for( int j = 0; j < 10; j++ )
			{
				printf( "%d", tm % 2 );
				tm /= 2;
			}
			puts( "" ); */

			if( __builtin_popcount( msk ) == 10 )
			{
				printf( "Case #%d: %lld\n", te, m );

				break;
			}
		}

		if( __builtin_popcount( msk ) != 10 )
		{
			printf( "Case #%d: INSOMNIA\n", te );
		}
	}

	return 0;
}