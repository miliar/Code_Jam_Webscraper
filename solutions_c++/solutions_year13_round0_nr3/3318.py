#include <iostream>
#include <cmath>
using namespace std;

bool isPlalindrome(const char* line)
{
	int length = strlen(line);
	for (int i=0, j=length-1; i<length/2; ++i, --j)
	{
		if (line[i] != line[j])
			return false;
	}
	return true;
}

void divideNumber(long number, char* strNum)
{
	int index = 0, item=number%10;
	for(; number; ++index, number/=10, item=number%10)
	{
		strNum[index] = '0' + item;
	}
	strNum[index] = '\0';
}

bool isFairAndSquare (long number, long lowLimit, long highLimit)
{
	char temp[100];
	divideNumber(number, temp);
	if (isPlalindrome(temp))
	{
		long squNum = number * number;
		if (squNum >= lowLimit && squNum <= highLimit)
		{
			divideNumber(squNum, temp);
			if (isPlalindrome(temp))
				return 1;
		}
	}
	return 0;
}

int countFairAndSquare(long llimit, long hlimit)
{
	int count = 0;
	for (long i=1; i<=sqrt(hlimit); ++i)
	{
		if (isFairAndSquare(i, llimit, hlimit))
			count ++;
	}
	return count;
}

int main()
{
	int group = 0;
	FILE* pInput = fopen("c.in", "r");
	FILE* pOut = fopen("c.out", "w");
	fscanf(pInput, "%d", &group);
	long low=0, high=0;
	for (int i=0; i<group; ++i)
	{
		fscanf(pInput, "%d%d", &low, &high);
		fprintf(pOut, "Case #%d: %d\n", i+1, countFairAndSquare(low, high));
		//cout<<"Case #"<<i+1<<": ";
		//cout<<countFairAndSquare(low, high)<<endl;
	}
	fclose(pInput);
	fclose(pOut);
	
	return 0;
}
