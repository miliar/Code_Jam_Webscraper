// FairAndSquare.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <sstream>
using namespace std;

// A function that reurns true only if num contains one digit
int oneDigit(int num)
{
    // comparison operation is faster than division operation.
    // So using following instead of "return num / 10 == 0;"
    return (num >= 0 && num < 10);
}

// A recursive function to find out whether num is palindrome
// or not. Initially, dupNum contains address of a copy of num.
bool isPalUtil(long long int num, long long int* dupNum)
{
    // Base case (needed for recursion termination): This statement
    // mainly compares the first digit with the last digit
    if (oneDigit(num))
        return (num == (*dupNum) % 10);
 
    // This is the key line in this method. Note that all recursive
    // calls have a separate copy of num, but they all share same copy
    // of *dupNum. We divide num while moving up the recursion tree
    if (!isPalUtil(num/10, dupNum))
        return false;
 
    // The following statements are executed when we move up the
    // recursion call tree
    *dupNum /= 10;
 
    // At this point, if num%10 contains i'th digit from beiginning,
    // then (*dupNum)%10 contains i'th digit from end
    return (num % 10 == (*dupNum) % 10);
}
 
// The main function that uses recursive function isPalUtil() to
// find out whether num is palindrome or not
int isPal(long long int num)
{
    // If num is negative, make it positive
    if (num < 0)
       num = -num;
 
    // Create a separate copy of num, so that modifications made
    // to address dupNum don't change the input number.
    __int64 *dupNum = new __int64(num); // *dupNum = num
 
    return isPalUtil(num, dupNum);
}



int main()
{
	FILE* file_input;
	file_input = fopen("C-small-attempt0.in", "r");
	FILE* file_output;
	char line[32];
	int no_of_test_cases = 0;
	long long int min = -1, max = -1;
	fgets(line, 32, file_input);
	sscanf(line, "%d", &no_of_test_cases);
	int result1 = -1, result2 = -1;
	int total_num = 0;
	for(int count = 1; count <= no_of_test_cases; count++)
	{
		fgets(line, 32, file_input);
		char* token = strtok(line, " ");
		sscanf(token, "%lld", &min);
		token = strtok(NULL, " ");
		sscanf(token, "%lld", &max);

		for(;min <= max; min++)
		{
			result1 = isPal(min);
			double sqrt_min = sqrt((double)min);
			std::ostringstream stream;
			stream << sqrt_min;
			std::string temp = stream.str();
			char* ptr = strtok((char*)temp.c_str(), ".");
			int temp_num1 = 0;
			sscanf(ptr, "%d", &temp_num1);
			ptr = strtok(NULL, ".");
			if(ptr != NULL)
			{
				int temp_num2 = 0;
				sscanf(ptr, "%d", &temp_num2);
				if(temp_num2 != 0)
				{
					continue;
				}
			}
			result2 = isPal((long long int) sqrt_min);
			if(result1 && result2)
			{
				total_num++;
			}
		}
		file_output = fopen("C-small-attempt0.out", "a");
		fprintf(file_output, "Case #%d: %d", count, total_num);
		total_num = 0;
		if(count == no_of_test_cases)
		{
			break;
		}
		else
		{
			fprintf(file_output, "\n");
		}
	}
	return 0;
}

