#include <cstdio>
#include <stdlib.h>
#include <string.h>
#include <set>

int main()
{
	int T, n;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	scanf( "%d", &T );
	for( int t = 1; t <= T; t++ )
	{
		scanf( "%d", &n );
		printf( "Case #%d: ", t );
		if( n == 0 )
		{
			printf( "INSOMNIA\n" );
		}
		else
		{
			std::set<int> digits;
			int iteration = 1;
			while( true )
			{
				int m = n * iteration;
				while( m > 0 )
				{
					digits.insert( m % 10 );
					m /= 10;
				}
				if( digits.size() == 10 )
				{
					printf( "%d\n", n * iteration );
					break;
				}
				iteration++;
			}
		}
	}
}