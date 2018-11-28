#include <conio.h>
#include <stdio.h>

int main()
{
	int i, T;
	long long r, t;
	long long rem;
	long long sol;

	scanf( "%d", &T );
	for( i=0; i<T; i++ )
	{
		scanf( "%lld", &r );
		scanf( "%lld", &t );
		
		sol = 0;
		rem = (r+1)*(r+1) - r*r;
		while( t > 0 )
		{
			t -= rem;
			rem += 4;
			if( t >= 0 )
				sol++;
		}

		printf( "Case #%d: %lld\n", i+1, sol );
	}

	getch();
	return 0;
}