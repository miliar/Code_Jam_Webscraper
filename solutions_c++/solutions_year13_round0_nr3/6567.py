#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <math.h>

unsigned long int limit = 100, countFS, A, B, mid, Sqr;
bool isPalindrome, isSquare;
int i, j, k, m;

int main ()
{
	FILE * pInFile;
	FILE * pOutFile;
	
	pInFile = fopen ("C:\\Users\\Lenovo-PC\\Desktop\\in.txt","r");
	pOutFile = fopen ("C:\\Users\\Lenovo-PC\\Desktop\\out.txt","w");

	for (i = 1; i <= limit; i++)
	{
		fscanf (pInFile, "%d %d", &A, &B);
		
		countFS = 0;
		for (j = A; j <= B ; j++)
		{
			isPalindrome = false;
			isSquare = false;

			Sqr = sqrtl(j);
			if(j == Sqr * Sqr)
			{
				isSquare = true;

				char strNumber[15] = {"\0"};
				itoa(Sqr,strNumber,10);

				for(k = 0; k < strlen(strNumber); k++)
				{
					for(m = strlen(strNumber) - 1; m >= 0; m--)
					{
						if(strNumber[k] == strNumber[m])
						{
							isPalindrome = true;
						}
						else
						{
							isPalindrome = false;
						}
					}
				}
			}
			else
			{
				isSquare = false;
			}

			if(isSquare == true && isPalindrome == true)
			{
				char strNumber[15] = {"\0"};
				itoa(j,strNumber,10);

				for(k = 0; k < strlen(strNumber); k++)
				{
					for(m = strlen(strNumber) - 1; m >= 0; m--)
					{
						if(strNumber[k] == strNumber[m])
						{
							isPalindrome = true;
						}
						else
						{
							isPalindrome = false;
						}
					}
				}
			}

			if(isSquare == true && isPalindrome == true)
			{
				countFS = countFS + 1;
			}
		}	

		fprintf (pOutFile, "Case #%d: ", i);
		fprintf (pOutFile, "%d\n", countFS);
	}

	fclose (pInFile);
	fclose (pOutFile);
	printf("\nOutput Generated!!!");
	scanf("END");
    return 0;
}