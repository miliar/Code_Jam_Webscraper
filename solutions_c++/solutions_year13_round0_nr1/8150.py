// TicTacToe.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//


#include "stdafx.h"
#include "stdio.h"

int CalcGame( char *pGame );
int CalcLine( char *pLine );


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp, *Outfp;
	int i,j,k;
	int testcase = 0;
	char game[4][4];
	int tmpResult;
		
	if ( ( fp=fopen("A-small-attempt1.in","r") ) == NULL )
	{
		fprintf(stderr, "Error ");
		return 0;
	}

	if ( ( Outfp=fopen("A-small-attempt0.out","w") ) == NULL )
	{
		fprintf(stderr, "Error ");
		return 0;
	}
		
	fscanf( fp, "%d", &testcase );
//	printf( "testcase %d\n", testcase );

	for ( i = 0; i < testcase ; i++ )
	{
		for ( j= 0 ; j < 4 ; j++ )
		{
			fscanf( fp, "%s", &game[j] );

//			for ( k = 0 ; k < 4 ; k++ )
//			{
//				printf( "%c", game[j][k] );
//			}
//			printf( "\n" );
		}
//		printf( "\n" );

		tmpResult = CalcGame( (char*)game );

		switch ( tmpResult )
		{
			case 0 :
				printf( "Case #%d: X won\n", i+1 );
				fprintf(Outfp, "Case #%d: X won\n", i+1 );
			break;

			case 1 :
				printf( "Case #%d: O won\n", i+1 );
				fprintf(Outfp, "Case #%d: O won\n", i+1 );
			break;

			case 2 :
				printf( "Case #%d: Game has not completed\n", i+1 );
				fprintf(Outfp, "Case #%d: Game has not completed\n", i+1 );
			break;

			case 3 :
				printf( "Case #%d: Draw\n", i+1 );
				fprintf(Outfp, "Case #%d: Draw\n", i+1 );
			break;
		}
	}

	fclose(fp);
	fclose(Outfp);
	
    getchar();
	return 0;
}

// retrun 0 : X won
// retrun 1 : O won
// retrun 2 : not completed
// retrun 3 : Draw
int CalcGame( char *pGame )
{
	int i, j;
	int notCompletedCount = 0;
	char tmpGame[4][4];
	char tmpLine[4];
	int tmpResult = -1;

	memcpy( tmpGame, pGame, 4*4 );

	for ( i = 0; i < 4; i++ )
	{
		for ( j = 0; j < 4; j++ )
		{
			tmpLine[j] = tmpGame[i][j];
		}

		tmpResult = CalcLine( tmpLine );

		if ( tmpResult == 0 || tmpResult == 1 )
			return tmpResult;
		else
		if ( tmpResult == 2 )
		{
			notCompletedCount++;
			tmpResult = -1;
		}
	}

	for ( i = 0; i < 4; i++ )
	{
		for ( j = 0; j < 4; j++ )
		{
			tmpLine[j] = tmpGame[j][i];
		}

		tmpResult = CalcLine( tmpLine );

		if ( tmpResult == 0 || tmpResult == 1 )
			return tmpResult;
		else
		if ( tmpResult == 2 )
		{
			notCompletedCount++;
			tmpResult = -1;
		}
	}
	

	for ( i = 0 ; i < 4 ; i++ )
	{
		tmpLine[i] = tmpGame[i][i];
	}

	tmpResult = CalcLine( tmpLine );

	if ( tmpResult == 0 || tmpResult == 1 )
		return tmpResult;
	else
	if ( tmpResult == 2 )
	{
		notCompletedCount++;
		tmpResult = -1;
	}
	
	for ( i = 0 ; i < 4 ; i++ )
	{
		tmpLine[i] = tmpGame[( 3 - i )][i];
	}

	tmpResult = CalcLine( tmpLine );

	if ( tmpResult == 0 || tmpResult == 1 )
		return tmpResult;
	else
	if ( tmpResult == 2 )
	{
		notCompletedCount++;
		tmpResult = -1;
	}

	if ( notCompletedCount >= 1 )
		return 2;

	return 3;
}

// retrun 0 : X won
// retrun 1 : O won
// retrun 2 : not completed
// retrun 3 : Draw
int CalcLine( char* pLine )
{
	int i = 0;
	int XCount = 0;
	int OCount = 0;
	int TCount = 0;
	int dotCount = 0;

	for ( i = 0; i < 4 ;i++ )
	{
		if ( pLine[i] == 'X' )
			XCount++;
		else
		if ( pLine[i] == 'O' )
			OCount++;
		else
		if ( pLine[i] == 'T' )
			TCount++;
		else
		if ( pLine[i] == '.' )
			dotCount++;
	}

	if ( XCount + TCount == 4 )
		return 0;

	if ( OCount + TCount == 4 )
		return 1;

	if ( ( dotCount + TCount + XCount == 4 ) || ( dotCount + TCount + OCount == 4 ) )
		return 2;

	return 3;
}

