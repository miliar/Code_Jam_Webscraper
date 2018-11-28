// 01_X.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <basetsd.h>
#include <iostream>

//#define SMALL_DATASET

#ifdef SMALL_DATASET
# define FILE_NAME_IN  "A-small-attempt0.in"
# define FILE_NAME_OUT "A-small-attempt0.out"
#else
# define FILE_NAME_IN  "A-large.in"
# define FILE_NAME_OUT "A-large.out"
#endif

int _tmain(int argc, _TCHAR* argv[])
{
  FILE * FileIn;
  FILE * FileOut;

  /* Open input file */
  fopen_s(&FileIn, FILE_NAME_IN, "r");
  _ASSERT(FileIn!=NULL);

  /* Open output file */
  fopen_s(&FileOut, FILE_NAME_OUT, "w+");
  _ASSERT(FileOut!=NULL);

  int num_of_test_cases;
  fscanf_s(FileIn, "%d", &num_of_test_cases);

  for (int testCase=0; testCase<num_of_test_cases; testCase++)
  {
    bool ghnc = false;
	bool playerX = false;
	bool playerO = false;
    char str[5];

	UINT8 playerXH;
	UINT8 playerXV[4] = {0};
	UINT8 playerX1 = 0;
	UINT8 playerX2 = 0;

	UINT8 playerOH;
	UINT8 playerOV[4] = {0};
	UINT8 playerO1 = 0;
	UINT8 playerO2 = 0;

    for (int LineNum=0; LineNum<4; LineNum++)
    {
		playerXH = 0;
		playerOH = 0;
		fscanf_s(FileIn, "%s", str, sizeof(str) );
		for ( int pos=0; pos<4; pos++)
		{
			switch ( str[pos])
			{
			case '.':
				ghnc = true;
				break;
			case 'X':
				playerXH++;
				playerXV[pos]++;
				if ( LineNum == pos )
				{
					playerX1++;
				}
				if ( LineNum == 3-pos )
				{
					playerX2++;
				}

				break;
			case 'O':
				playerOH++;
				playerOV[pos]++;
				if ( LineNum == pos )
				{
					playerO1++;
				}
				if ( LineNum == 3-pos )
				{
					playerO2++;
				}
				break;
			case 'T':
				playerXH++;
				playerOH++;
				playerXV[pos]++;
				playerOV[pos]++;
				if ( LineNum == pos )
				{
					playerX1++;
					playerO1++;
				}
				if ( LineNum == 3-pos )
				{
					playerX2++;
					playerO2++;
				}
				break;
			}
		}
		if ( playerXH == 4 )
		{
			playerX = true;
		}
		if ( playerOH == 4 )
		{
			playerO = true;
		}
    }

	if ( playerX1 == 4 || playerX2 == 4 )
	{
		playerX = true;
	}
	for ( int i=0; i<4; i++)
	{
		if ( playerXV[i] == 4 )
		{
			playerX = true;
		}
	}

	if ( playerO1 == 4 || playerO2 == 4 )
	{
		playerO = true;
	}
	for ( int i=0; i<4; i++)
	{
		if ( playerOV[i] == 4 )
		{
			playerO = true;
		}
	}

	if ( playerX )
	{
		fprintf(FileOut, "Case #%d: X won\n",testCase+1);
	}
	else if ( playerO )
	{
		fprintf(FileOut, "Case #%d: O won\n",testCase+1);
	}
	else if ( ghnc )
	{
		fprintf(FileOut, "Case #%d: Game has not completed\n",testCase+1);
	}
	else
	{
		fprintf(FileOut, "Case #%d: Draw\n",testCase+1);
	}

//	fscanf_s(FileIn, "%s", str, sizeof(str) );
  }

  /* Close all files */
  _fcloseall();

#define SHOW_FILE(x) "type "##x
  system(SHOW_FILE(FILE_NAME_IN));
  printf("\n");
  system(SHOW_FILE(FILE_NAME_OUT));
  printf("\n");
  system("PAUSE");
  return 0;
}



