#include <stdio.h>
#include <iostream>

using namespace std;

int  main()
{
	int t,nc=1;
	int maze[4][4] , cards[ 4 ];
	int ans;
	int row;
	int n;

	scanf("%d" , &t );
	while( t-- )
	{

		ans = 0;

		scanf( "%d" , &row );
		for (int i = 0; i < 4 ; i++ )
			for (int j = 0; j < 4; j++ )
			{
				scanf("%d" , &n );
				maze[ i ][ j ] = n;
				if( i == row -1 )
					cards[ j ] = n;
			}


		scanf( "%d" , &row );
		for (int i = 0; i < 4 ; i++ )
			for (int j = 0; j < 4; j++ )
				scanf("%d" , &maze[ i ][ j ] );
				
		for (int i = 0; i < 4 ; i++ )
			for (int j = 0; j < 4; j++ )
				if( cards[ i ] == maze[ row-1 ][ j ] )
				{
					ans++;
					n = maze[ row-1 ][ j ];
				}


		if( ans == 0 )
			printf("Case #%d: Volunteer cheated!\n",nc++);
		else if( ans == 1 )
			printf("Case #%d: %d\n", nc++ ,n );
		else
			printf("Case #%d: Bad magician!\n" , nc++ );
			
				
	}



	return 0;
}