// 01_X.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <basetsd.h>
#include <iostream>

using namespace System;
using namespace System::IO;


#define SMALL_DATASET

#ifdef SMALL_DATASET
# define FILE_NAME_IN  "B-small-practice.in"
# define FILE_NAME_OUT "B-small-practice.out"
#else
# define FILE_NAME_IN  "B-large-practice.in"
# define FILE_NAME_OUT "B-large-practice.out"
#endif

int _tmain(int argc, _TCHAR* argv[])
{
  FILE * FileIn;
  FILE * FileOut;

  StreamReader ^ fileIn = gcnew StreamReader(FILE_NAME_IN);

  /* Open input file */
  //fopen_s(&FileIn, FILE_NAME_IN, "r+");
  //_ASSERT(FileIn!=NULL);

  /* Open output file */
  fopen_s(&FileOut, FILE_NAME_OUT, "w+");
  _ASSERT(FileOut!=NULL);

  int num_of_test_cases;
  //fscanf_s(FileIn, "%d", &num_of_test_cases);

  String ^ line = fileIn->ReadLine();
  num_of_test_cases = UInt32::Parse(line);


  array<Char>^sep = gcnew array<Char>{' '};
  array<String^>^splitArray;

  //int i=0;
  for (int i=0; i<num_of_test_cases; i++)
  {
    /* IMPLEMENTATION */

	int ROWS,COLUMNS = 0;

	//fscanf_s(FileIn, "%d%d", &ROWS, &COLUMNS);

    line = fileIn->ReadLine();
    splitArray = line->Split( sep, StringSplitOptions::RemoveEmptyEntries );

	ROWS = UInt32::Parse(splitArray[0]);
	COLUMNS = UInt32::Parse(splitArray[1]);


	int ** lawn;
	lawn = new int *[ROWS];

	for (int row=0; row < ROWS; row++ )
      lawn[row] = new int[COLUMNS];


	
	for( int row = 0 ; row < ROWS ; row++ )
	{
	  line = fileIn->ReadLine();
	   splitArray = line->Split( sep, StringSplitOptions::RemoveEmptyEntries );
	  for (int column = 0  ; column < COLUMNS ; column++ )
	  {
		lawn[row][column] = UInt32::Parse(splitArray[column]);
	  }
	}

    Boolean yes = true;
	for( int row = 0 ; row < ROWS && yes; row++ )
	{
	  for (int column = 0  ; column < COLUMNS && yes; column++ )
	  {
		int currItem = lawn[row][column];

		for (int m = 0; m < COLUMNS && yes; m++)
		{
		  if (lawn[row][m] <= currItem)    // ak cislo je mensie alebo rovne
		  {    
			if (lawn[row][m] < currItem)   // ak je mensie
			{
			  for (int n = 0; n < ROWS && yes; n++) // vsetky ostatne musia byt take iste
			  {
				 if (lawn[n][m] != lawn[row][m])
				 {
				   yes = false;
				 }
			  }
			}
		  }
		  else
		  {
		   yes = false;
		  }
		}

		if (yes == false)
		{
			yes = true;
			for (int n = 0; n < ROWS; n++)
			{
			  if (lawn[n][column] <= currItem)
			  {
			   if (lawn[n][column] < currItem)
			   {
				 for (int m = 0; m < COLUMNS && yes; m++)
		         {
			       if (lawn[n][m] != lawn[n][column])
				   {
				     yes = false;
				   }
				 }
			   }
		      }
			  else
			  {
			   yes = false;
			  }
			}
		}

	  }
	}

	
	for( int row = 0 ; row < ROWS ; row++ )
		delete [] lawn[row];
	delete [] lawn;
	

    fprintf(FileOut, "Case #%d: %s\n",i+1, yes == true ? "YES" : "NO" );
    /* END OF IMPLEMENTATION */
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



