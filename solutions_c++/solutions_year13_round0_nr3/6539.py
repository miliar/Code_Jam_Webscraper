// FairandSquare.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include "stdio.h"
#include "string.h"
#include "math.h"
#include <stdlib.h>

bool IsFair( unsigned __int64 pNumber );
bool IsSquar( unsigned __int64 pNumber );

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp, *Outfp;
	int i;
	int testcase = 0;
	int tmpResult = 0;
	char beginNum[100];
	char endNum[100];
	char ParaNum[100];
	unsigned __int64 tmpIndex,tmpBeginIndex, tmpEndIndex;
	unsigned __int64 tmpBeginSqrt, tmpEndSqrt, tmpIndexSqrt;

	if ( ( fp=fopen("C-small-attempt0.in","r") ) == NULL )
	{
		fprintf(stderr, "Error ");
		return 0;
	}

	if ( ( Outfp=fopen("C-small-attempt0.out","w") ) == NULL )
	{
		fprintf(stderr, "Error ");
		return 0;
	}

	fscanf( fp, "%d", &testcase );
	//printf( "testcase %d\n", testcase );

	for ( i = 0; i < testcase ; i++ )
	{
		fscanf( fp, "%s", beginNum );
		fscanf( fp, "%s", endNum );

		tmpBeginIndex = _atoi64( beginNum );
		tmpEndIndex = _atoi64( endNum );

		tmpBeginSqrt = (unsigned __int64)sqrt( tmpBeginIndex * 1.0 );
		tmpEndSqrt = (unsigned __int64)sqrt( tmpEndIndex * 1.0 );

/*
		printf( "----------------------------------\n" );
		printf( " tmpBeginIndex : %I64u\n", tmpBeginIndex );
		printf( " tmpEndIndex : %I64u\n", tmpEndIndex );
		printf( " tmpBeginSqrt : %I64u\n", tmpBeginSqrt );
		printf( " tmpEndSqrt : %I64u\n", tmpEndSqrt );
*/
		tmpResult = 0;

		for ( tmpIndex = tmpBeginSqrt ; tmpIndex <= tmpEndSqrt ; tmpIndex++ )
		{
			tmpIndexSqrt = tmpIndex * tmpIndex;
			
			if ( tmpIndexSqrt < tmpBeginIndex || tmpIndexSqrt > tmpEndIndex )
				continue;

			if ( !IsFair( tmpIndex ) )
				continue;

			if ( !IsFair( tmpIndexSqrt ) )
				continue;

//			printf( "find: %I64u - %I64u\n", tmpIndex, tmpIndexSqrt );
			tmpResult++;
		}

		printf( "Case #%d: %d\n", i+1, tmpResult );
		fprintf(Outfp, "Case #%d: %d\n", i+1, tmpResult );
	}

	fclose(fp);
	fclose(Outfp);
	
    getchar();

	return 0;
}

bool IsFair( unsigned __int64 pNumber )
{
	int i, j;
	char tmpNumStr[100];

	sprintf( tmpNumStr, "%I64u", pNumber );

	int tmpLen = strlen( tmpNumStr );

	if ( tmpLen == 1 )
		return true;

	for ( i = 0, j = tmpLen-1 ; i < j ; i++, j-- )
	{
		if ( tmpNumStr[i] != tmpNumStr[j] )
			return false;
	}

	return true;
}

