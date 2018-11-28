#include "stdafx.h"
#include <iostream>

#define INITIAL_LAWN_HEIGHT 100
#define MAX_DIMENSION       100

typedef struct {
	int cells[ MAX_DIMENSION ][ MAX_DIMENSION ];
	int nSize;
	int mSize;
} LAWN;

static bool Lawn_IsEqual( LAWN &desiredLawn, LAWN &lawn)
{
	// check sizes
	if( lawn.nSize != desiredLawn.nSize ) return false;
	if( lawn.mSize != desiredLawn.mSize ) return false;

	// check data
	for( int i = 0; i < desiredLawn.nSize; i++ )
	{
		for( int j = 0; j < desiredLawn.mSize; j++ )
		{
			if( desiredLawn.cells[i][j] != lawn.cells[i][j] )
			{
				return false;
			}
		}
	}

	return true;
}

static int Lawn_GetRowMax( LAWN& lawn, int rowIndex )
{
	if( rowIndex < 0 || rowIndex >= lawn.nSize )
	{
		return INITIAL_LAWN_HEIGHT;
	}

	int max = 0;
	for( int i = 0; i < lawn.mSize; i++ )
	{
		if( lawn.cells[rowIndex][i] > max )
		{
			max = lawn.cells[rowIndex][i];
		}
	}

	return max;
}

static int Lawn_GetColumnMax( LAWN& lawn, int columnIndex )
{
	if( columnIndex < 0 || columnIndex >= lawn.mSize )
	{
		return INITIAL_LAWN_HEIGHT;
	}

	int max = 0;
	for( int i = 0; i < lawn.nSize; i++ )
	{
		if( lawn.cells[i][columnIndex] > max )
		{
			max = lawn.cells[i][columnIndex];
		}
	}

	return max;
}

static bool Lawnmower_IsPossible( LAWN& desiredLawn )
{
	// create a initial lawn that matches the size.
	LAWN lawn;
	lawn.nSize = desiredLawn.nSize;
	lawn.mSize = desiredLawn.mSize;
	
	// init the lawn cells to be the intial size
	for( int i = 0; i < lawn.nSize; i++ )
	{
		for( int j = 0; j <lawn.mSize; j++ )
		{
			lawn.cells[i][j] = INITIAL_LAWN_HEIGHT;
		}
	}

	// iterate through desired lawn and cut our lawn to match the max values.
	// cut rows
	for( int i = 0; i < lawn.nSize; i++ )
	{
		// get desired height
		int rowMax = Lawn_GetRowMax( desiredLawn, i );

		// cut the grass with the desired height set.
		for( int j = 0; j <lawn.mSize; j++ )
		{
			if( rowMax < lawn.cells[i][j] )
			{
				lawn.cells[i][j] = rowMax;
			}
		}
	}

	// cut columns
	for( int i = 0; i <lawn.mSize; i++ )
	{
		// get desired height
		int columnMax = Lawn_GetColumnMax( desiredLawn, i );

		// cut the grass with the desired height set.
		for( int j = 0; j <lawn.nSize; j++ )
		{
			if( columnMax < lawn.cells[j][i] )
			{
				lawn.cells[j][i] = columnMax;
			}
		}
	}

	return Lawn_IsEqual( desiredLawn, lawn );
}

static void Lawnmower_ReadInput()
{
	char  Buffer[ 32 ];
	int  numTestCases;

	// read number of test cases
	scanf( "%d", &numTestCases );

	for( int i = 0; i < numTestCases; ++i )
	{
		// create a lawn
		LAWN desiredLawn;
		memset( &desiredLawn, 0, sizeof(desiredLawn) );

		// read N x M info
		scanf( "%d", &desiredLawn.nSize );
		scanf( "%d", &desiredLawn.mSize );
		
		// make sure the n x m sizes are valid.
		if( desiredLawn.nSize > 100 ) break;
		if( desiredLawn.mSize > 100 ) break;

		// read the desired lawn's data
		for( int j = 0; j < desiredLawn.nSize; j++ )
		{
			for( int k = 0; k < desiredLawn.mSize; k++ )
			{
				scanf( "%d", &desiredLawn.cells[j][k] );
			}
		}

		// check if its possible to create the desired lawn
		if( Lawnmower_IsPossible( desiredLawn ) )
		{
			printf( "Case #%d: YES\n", i + 1 );
		}
		else
		{
			printf( "Case #%d: NO\n", i + 1 );
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	Lawnmower_ReadInput();

	return( 0 );
}

