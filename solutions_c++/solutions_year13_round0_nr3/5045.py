// 01_X.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <basetsd.h>
#include <iostream>
#include <math.h>

#define SMALL_DATASET

#ifdef SMALL_DATASET
# define FILE_NAME_IN  "C-small-attempt0.in"
# define FILE_NAME_OUT "C-small-attempt0.out"
#else
# define FILE_NAME_IN  ""
# define FILE_NAME_OUT ""
#endif

#define STRING_SIZE		255

bool isPalindrome(UINT64 num)
{
	bool toRet = true;
	static char str[1000];
	int pos = 0;
	int strLength = 0;

	_ui64toa_s(num, str, sizeof(str), 10);
	strLength = strlen(str) - 1;

	while (pos < strLength)
	{
		if (str[pos] != str[strLength])
		{
			toRet = false;
			break;
		}

		pos++;
		strLength--;
	}

	return toRet;
}




int _tmain(int argc, _TCHAR* argv[])
{
  FILE * fileIn;
  FILE * fileOut;

  fopen_s(&fileIn, FILE_NAME_IN, "r");
  _ASSERT(fileIn!=NULL);

  fopen_s(&fileOut, FILE_NAME_OUT, "w+");
  _ASSERT(fileOut!=NULL);

  int num_of_test_cases;
  fscanf_s(fileIn, "%d", &num_of_test_cases);

  for (int i=0; i<num_of_test_cases; i++)
  {
	  static char str[STRING_SIZE];
	  int resNb = 0;
	  UINT64 endPoint1 = 0;
	  UINT64 endPoint2 = 0;
	  UINT64 interPoint = 0;

	  fscanf_s(fileIn, "%s", str, sizeof(str));
	  endPoint1 = _strtoui64(str, 0, 10);
	  fscanf_s(fileIn, "%s", str, sizeof(str));
	  endPoint2 = _strtoui64(str, 0, 10);

	  interPoint = (UINT64)sqrt((long double)endPoint1);

	  if ((interPoint * interPoint) < endPoint1) interPoint++;

	  while(interPoint * interPoint <= endPoint2)
	  {
		  if (isPalindrome(interPoint))
		  {
			  if (isPalindrome(interPoint * interPoint))
				  resNb++;
		  }
		  interPoint++;
	  }

    fprintf(fileOut, "Case #%d: %d\n",i+1, resNb );
  }

  _fcloseall();

  #define SHOW_FILE(x) "type "##x
  system(SHOW_FILE(FILE_NAME_IN));
  printf("\n");
  system(SHOW_FILE(FILE_NAME_OUT));
  printf("\n");
  system("PAUSE");
  return 0;

}



