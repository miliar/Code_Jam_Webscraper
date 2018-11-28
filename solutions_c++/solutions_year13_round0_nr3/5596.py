// 01_X.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <basetsd.h>
#include <iostream>
#include <math.h>

#define SMALL_DATASET

#ifdef SMALL_DATASET
# define FILE_NAME_IN  "C-small-attempt2.in"
# define FILE_NAME_OUT "C-small-attempt2.out"
#else
# define FILE_NAME_IN  "B-large-practice.in"
# define FILE_NAME_OUT "B-large-practice.out"
#endif

bool isPalindromes(UINT64 num)
{
	bool ret = true;
	static char str[1000];
	_ui64toa_s(num, str, sizeof(str), 10);
	int lenStr = strlen(str)-1;
	int pos=0;

	while (pos < lenStr)
	{
		if (str[pos]!=str[lenStr])
		{
			ret = false;
			break;
		}
		pos++;
		lenStr--;
	}

	if ( pos )
	{
	}

	return ret;
}

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

  for (int i=0; i<num_of_test_cases; i++)
  {
	  static char str[1000];
	  int count = 0;
	  UINT64 A,B;
	  UINT64 minA;

	  fscanf_s(FileIn, "%s", str, sizeof(str));
	  A = _strtoui64(str, 0, 10);
	  fscanf_s(FileIn, "%s", str, sizeof(str));
	  B = _strtoui64(str, 0, 10);

	  minA = (UINT64)sqrt((long double)A);
	  if ((minA*minA) < A)
	  {
		  minA++;
	  }

	  while(minA*minA <= B)
	  {
		  if (isPalindromes(minA))
		  {
			  if (isPalindromes(minA*minA))
			  {
				  count++;
			  }
		  }
		  minA++;
	  }

    fprintf(FileOut, "Case #%d: %d\n",i+1, count );
  }

  /* Close all files */
  _fcloseall();

  return 0;
}



