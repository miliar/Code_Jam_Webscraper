
/*  Problem Statement :
	Print all the number between the range A to B which are sqaures of
	palindromes and are palindromes theselves
	*/

#define PARENT_DIR_NAME "d:/DUMP/"
#define INPUT_FILE_NAME "input.in"
#define OUTPUT_FILE_NAME "output.out"

#define MAX_PATH_LENGTH 1024
#define MAX_INT_DIGITS 100
#include <direct.h>
//#include <sys\types.h>
//#include <sys\stat.h>
#include <string>
#include <math.h>
#include <time.h>
#include <conio.h>

using namespace std;

void loadFileName(char *dir, char *inputTestCasesFileName, char *outputTestCasesFileName)
{
	strcpy(dir, PARENT_DIR_NAME);

	_mkdir(dir);
	// open the input file to be read
	strcpy(inputTestCasesFileName, dir);
	strcat(inputTestCasesFileName, INPUT_FILE_NAME);

	strcpy(outputTestCasesFileName, dir);

	strcat(outputTestCasesFileName, OUTPUT_FILE_NAME);
}

bool compareLeftNRightReverse(char *leftPalindromeStr, const char *rightStr)
{
	int leftLength = strlen(leftPalindromeStr);
	int rightLength = strlen(rightStr);

	if (leftLength != rightLength)
		return false;

	char *pLeft = leftPalindromeStr;
	char *pRight = const_cast<char *>(rightStr) + rightLength - 1;
	
	while(*pLeft == *pRight)
	{
		if (NULL != *pLeft)
		{
			pLeft++;
			pRight--;
		}
		else
			return true;

	}

	if (NULL != *pLeft)
		return false;
}

bool isPalindrome(long long int number, bool isSquare)
{
	if (number < 10)
		return true;

	int numDigits = 0;

	numDigits = floorf(log10f(number) + 1);

	int palindromeFactor = (pow(10.0, numDigits/2));

	int leftPalindrome = number/palindromeFactor;

	int odd = numDigits%2;
	long long int mostSigDigit = (leftPalindrome*10)/palindromeFactor;


	if (odd)
	{
		mostSigDigit /= 10;
	}

	if ((isSquare) && (mostSigDigit == 2 || mostSigDigit == 3 || mostSigDigit == 7 || mostSigDigit == 8))
		return false;

	
	// Ignore the middle digit if odd number of digits
	int rightPalindrome = number - leftPalindrome * palindromeFactor;

	if (1 == odd)
	{
		leftPalindrome /= 10;
	}

	char leftPalindromeStr[MAX_INT_DIGITS];
	char rightPalindromeStr[MAX_INT_DIGITS];

	itoa(leftPalindrome, leftPalindromeStr, 10);
	itoa(rightPalindrome, rightPalindromeStr, 10);

	int numLeftDigits = strlen(leftPalindromeStr);
	int numRightDigits = strlen(rightPalindromeStr);
	
	int diff = numLeftDigits - numRightDigits;
	
	string rightStr;
	rightStr.clear();

	while (diff > 0)
	{
		rightStr += "0";
		diff--;
	}
	rightStr += rightPalindromeStr;

	return compareLeftNRightReverse(leftPalindromeStr, rightStr.c_str());
}

long long int countFairNSquares(long long int A, long long int B)
{
	long long int count = 0;
	long long int number = 0;
	long double doubleA = static_cast<long double>(A);
	long double sqrtNumber = sqrtl(doubleA);

	sqrtNumber = ceill(sqrtNumber);
	long long int intSqrtNum = static_cast<long long int>(sqrtNumber);
	number = intSqrtNum * intSqrtNum;

	for (number; number <= B; number += intSqrtNum + intSqrtNum - 1)
	{
		// If ending with zero
		if (number == 121 || number == 484)
		{
			int d = 0;
		}
		if (intSqrtNum % 10 == 0)
		{
			intSqrtNum++;
			continue;
		}
		if (isPalindrome(intSqrtNum, false) && isPalindrome(number, true))
		{
			count++;
		}
		intSqrtNum++;
	}

	return count;
}

int main()
{
	clock_t time1;
	time1 = clock();

	//time_t timer1;
	//time_t timer2;
	// struct tm y2k;
	int seconds = 0;

	// time(&timer1);

	char dir[MAX_PATH_LENGTH];
	char inputTestCasesFileName[MAX_PATH_LENGTH];
	char outputTestCasesFileName[MAX_PATH_LENGTH];

	// Load the input test cases File name
	loadFileName(dir, inputTestCasesFileName, outputTestCasesFileName);

	// open input File in read mode
	FILE *iFP = fopen(inputTestCasesFileName, "r");
	FILE *oFP = fopen(outputTestCasesFileName, "w");

	// Read Number of Test Cases
	int numTestCases = 0;
	long long int A = 0, B = 0;
	//int d = sizeof(long int);

	fscanf(iFP, "%d", &numTestCases);

	// For each test case, apply the algorithm
	long long int numFairNSquares = 0;
	for (int caseNum = 0; caseNum < numTestCases; caseNum++)
	{
		fscanf(iFP, "%lld %lld", &A, &B);
		
		// Count Fair and Square numbers
		numFairNSquares = countFairNSquares(A, B);
		fprintf(oFP, "Case #%d: %lld\n", caseNum + 1, numFairNSquares);
	}

	clock_t time2;
	time2 = clock();
	time2 -= time1;
	
	seconds = time2/CLOCKS_PER_SEC;

	printf("%d", seconds);

	fclose(iFP);
	fclose(oFP);
	getch();
	getch();
}