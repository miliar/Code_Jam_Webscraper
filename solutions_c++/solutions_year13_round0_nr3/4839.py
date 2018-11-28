#include <stdio.h>
#include <string.h>

int ispld( long long n )
{
	char s[15];
	int i, len;

	len = 0;
	while ( n )
	{
		s[len++] = n % 10;
		n /= 10;
	}

	for ( i = 0 ; i < len / 2 ; ++i )
		if ( s[i] != s[len-1-i] )
			return 0;

	return 1;
}

int main()
{
	FILE *fpi;
	FILE *fpo;

	long long pld[2000];
	long long cnt;
	long long a, b;
	long long i, j;
	long long k, t;
	long long spld;
	long long fpldCnt;

	fpi = fopen( "gcjc.in" , "r" );
	fpo = fopen( "gcjc.out" , "w" );

	cnt = 0;

	//1 digit
	for ( i = 1 ; i <= 9 ; ++i )
	{
		pld[cnt++] = i;
	}

	//2 digits
	for ( i = 1 ; i <= 9 ; ++i )
	{
		pld[cnt++] = i * 10 + i;
	}

	//3 digits
	for ( i = 1 ; i <= 9 ; ++i )
	{
		for ( j = 0 ; j <= 9 ; ++j )
			pld[cnt++] = i * 100 + j * 10 + i;
	}

	//4 digits
	for ( i = 10 ; i <= 99 ; ++i )
	{
		pld[cnt++] = i * 100 + i % 10 * 10 + i / 10;
	}

	//5 digits
	for ( i = 10 ; i <= 99 ; ++i )
	{
		for ( j = 0 ; j <= 9 ; ++j )
			pld[cnt++] = i * 1000 + j * 100 + i % 10 * 10 + i / 10;
	}

	//6 digits
	for ( i = 100 ; i <= 999 ; ++i )
	{
		pld[cnt++] = i * 1000 + i % 10 * 100 + i / 10 % 10 * 10 + i / 100;
	}

	fscanf( fpi , "%lld" , &t );
	k = 1;
	while ( k <= t )
	{
		fscanf( fpi , "%lld%lld" , &a , &b );

		fpldCnt = 0;
		for ( i = 0 ; i < cnt ; ++i )
		{
			spld = pld[i] * pld[i];

			if ( spld >= a && spld <= b && ispld( spld ) )
			{
				fpldCnt++;
			}

			if ( spld > b )
				break;
		}

		fprintf( fpo , "Case #%lld: %lld\n" , k++ , fpldCnt );
	}
}
