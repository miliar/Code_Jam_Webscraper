#include <stdio.h>

int T;
int m, n;
short platform[100][100];
short mimic[10][10];
int column[100];
int row[100];
bool flag = false;

int main()
{
	scanf( "%d", &T );
	for( int p = 0; p < T; ++p )
	{
		flag = false;
		scanf( "%d %d", &m, &n );
		for( int i =0; i < 100; ++i )
		{
			column[i] = 0;
			row[i] = 0;
			mimic[i/10][i%10] = 2;
		}
		for( int i = 0; i < m; ++i )
			for( int j = 0; j < n; ++j )
				scanf( "%d", &platform[i][j] );
		for( int i = 0; i < m; ++i )
		{
			for( int j = 0; j < n; ++j )
			{
				column[j] += platform[i][j];
				row[i] += platform[i][j];
			}
		}
		for( int i = 0; i < m; ++i )
			if( row[i] == n )
				for( int j = 0; j < n; ++j )
					mimic[i][j] = 1;
		for( int j = 0; j < n; ++j )
			if( column[j] == m )
				for( int i = 0; i < m; ++i )
					mimic[i][j] = 1;
		for( int i = 0; i < m; ++i )
			for( int j = 0; j < n; ++j )
				if( platform[i][j] != mimic[i][j] )
				{
					flag = true;
					break;
				}
		if( flag )
			printf( "Case #%d: NO\n" , p+1 );
		else
			printf( "Case #%d: YES\n", p+1 );
	}
	return 0;
}