#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

long long FindSquare(long long n, long long x0);

bool CanBeASquare(char lastDigit);

bool IsPalindrome(string numberString);

long long GetNumberBack(string numberString);

int main()
{
	ifstream fin("C:\\Users\\KishoreVen\\Downloads\\C-small-attempt0.in", ios::in);
	ofstream fout("output.out", ios::out);

	int t;
	fin>>t;

	long long *results;

	results = new long long[t];

	long long int minNumber, maxNumber;	
	 
	for(long long int i = 0; i < t; i++)
	{
		fin >> minNumber >> maxNumber;

		results[i] = 0;

		for(long long int number = minNumber; number <= maxNumber; number ++)
		{
			string numberString = to_string(number);

			if(CanBeASquare(numberString[numberString.length() - 1]) == true)
			{
				if(IsPalindrome(numberString) == true)
				{
					int stringLength = numberString.length() / 2;

					if(stringLength != 0)
					{
						char *x0PointerString = new char[stringLength + 1];

						x0PointerString[0] = '1';

						for(int i = 1; i < stringLength; i++)
						{
							x0PointerString[i] = '0';
						}

						x0PointerString[stringLength] = '\0';

						string x0String(x0PointerString);					

						long long x0 = GetNumberBack(x0String);

						long long sqrtNumber = FindSquare(number, x0);

						if(sqrtNumber != -1)
						{
							string sqrtNumberString = to_string(sqrtNumber);
							
							if(IsPalindrome(sqrtNumberString) == true)
							{
								results[i]++;							
							}
						}

						delete[] x0PointerString;
					}					
					else
					{
						long long sqrtNumber = FindSquare(number, 1);

						if(sqrtNumber != -1)
						{
							string sqrtNumberString = to_string(sqrtNumber);
							
							if(IsPalindrome(sqrtNumberString) == true)
							{
								results[i]++;							
							}							
						}
					}
				}
			}
		}
	}

	fin.close();

	for(long long int i = 0; i < t; i++)
	{
		fout<<"Case #"<<i + 1<<": "<<results[i]<<endl;		
	}

	delete[] results;

	fout.close();	

	return 0;
}


long long GetNumberBack(string numberString)
{
	istringstream buffer(numberString);
	
	long long int backToNumber;

	buffer>>backToNumber;

	return backToNumber;
}


bool CanBeASquare(char lastDigit)
{
	if(lastDigit == '1' || lastDigit == '4' || lastDigit == '5' || lastDigit == '6' || lastDigit == '9')
	{
		return true;
	}

	return false;
}


bool IsPalindrome(string numberString)
{
	int j = numberString.length() - 1;

	if(j == 0)
	{
		return true;
	}

	for(int i = 0; i < j; i++, j--)
	{
		if(numberString[i] != numberString[j])
		{
			return false;
		}
	}

	return true;
}


long long FindSquare(long long n, long long x0)
{
	long long previous = 0;

	long long current = x0;

	double actualCurrent;

	int i = 0;

	int max = 25;

	for(i = 0; current - previous != 0 && i < max; i++)
	{
		previous = current;	

		actualCurrent = ((long double)current * (long double)current + (long double)n ) / (2.0 * (long double)current);	

		current = (current * current + n ) / (2 * current);
	}

	if(i == max)
	{
		return -1;
	}

	if(actualCurrent - current == 0)
	{
		return current;		
	}

	return -1;
}