#include <stdio.h>
#include <string.h>
#include <math.h>

void convert( int n , char bn[] )
{
	int len = 0;

	while( n )
	{
		bn[len++] = n % 2;
		n /= 2;
	}
}

void renewlawn( char nlawn[][10] , char bi[] , char bj[] , int n , int m )
{
	int i, j;

	for ( i = 0 ; i < n ; ++i )
		for ( j = 0 ; j < m ; ++j )
			nlawn[i][j] = 2 - ( ( bi[i] || bj[j] ) ? 1 : 0 );
}

int check( char lawn[][10] , char nlawn[][10] , int n , int m )
{
	int i, j;

	for ( i = 0 ; i < n ; ++i )
		for ( j = 0 ; j < m ; ++j )
			if ( lawn[i][j] != nlawn[i][j] )
				return 0;

	return 1;
}

int main()
{
	FILE *fpi;
	FILE *fpo;

	int n, m;
	char lawn[10][10];
	char nlawn[10][10];
	char bi[10];
	char bj[10];
	int h;
	int k, t;
	int i, j;
	int pown;
	int powm;
	int flag;

	fpi = fopen( "gcjb.in" , "r" );
	fpo = fopen( "gcjb.out" , "w" );

	fscanf( fpi , "%d" , &t );
	k = 1;
	while ( k <= t )
	{
		fscanf( fpi , "%d%d" , &n , &m );
		for ( i = 0 ; i < n ; ++i )
			for ( j = 0 ; j < m ; ++j )
			{
				fscanf( fpi , "%d" , &h );
				lawn[i][j] = h;
			}

		pown = (int)pow( 2 , n + 1 );
		powm = (int)pow( 2 , m + 1 );

		flag = 0;

		for ( i = 0 ; i < n ; ++i )
		{
			flag = 0;
			if ( lawn[i][0] == 1 )
			{
				for ( j = 0 ; j < m ; ++j )
					if ( lawn[i][j] == 2 )
					{
						flag++;
						break;
					}
				for ( j = 0 ; j < n ; ++j )
					if ( lawn[j][0] == 2 )
					{
						flag++;
						break;
					}
			}

			if ( flag >= 2 ) break;

			flag = 0;
			if ( lawn[i][m-1] == 1 )
			{
				for ( j = 0 ; j < m ; ++j )
					if ( lawn[i][j] == 2 )
					{
						flag++;
						break;
					}
				for ( j = 0 ; j < n ; ++j )
					if ( lawn[j][m-1] == 2 )
					{
						flag++;
						break;
					}
			}
			if ( flag >= 2 ) break;
		}

		if ( flag >= 2 )
		{
			fprintf( fpo , "Case #%d: NO\n" , k++ );
			continue;
		}

		for ( j = 0 ; j < m ; ++j )
		{
			flag = 0;
			if ( lawn[0][j] == 1 )
			{
				for ( i = 0 ; i < n ; ++i )
					if ( lawn[i][j] == 2 )
					{
						flag++;
						break;
					}
				for ( i = 0 ; i < m ; ++i )
					if ( lawn[0][i] == 2 )
					{
						flag++;
						break;
					}
			}
			if ( flag >= 2 ) break;

			flag = 0;
			if ( lawn[n-1][j] == 1 )
			{
				for ( i = 0 ; i < n ; ++i )
					if ( lawn[i][j] == 2 )
					{
						flag++;
						break;
					}
				for ( i = 0 ; i < m ; ++i )
					if ( lawn[n-1][i] == 2 )
					{
						flag++;
						break;
					}
			}
			if ( flag >= 2 ) break;
		}

		if ( flag >= 2 )
		{
			fprintf( fpo , "Case #%d: NO\n" , k++ );
			continue;
		}


		flag = 0;
		for ( i = 0 ; i < pown && !flag ; ++i )
			for ( j = 0 ; j < powm && !flag ; ++j )
			{
				memset( bi , 0 , sizeof( bi ) );
				memset( bj , 0 , sizeof( bj ) );
				convert( i , bi );
				convert( j , bj );
				renewlawn( nlawn , bi , bj , n , m );

				if ( check( lawn , nlawn , n , m ) )
					flag = 1;
			}


		fprintf( fpo , "Case #%d: %s\n" , k++ , ( flag ? "YES" : "NO" ) );
	}

	return 0;
}
