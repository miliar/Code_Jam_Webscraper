#include <vector>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

bool isPalindrome(long long int x)
{
	stringstream ss;
	ss << x;
	string str = ss.str();
	unsigned int size = str.length();

	for(unsigned int i=0; i<size/2; i++)
	{
		if (str[i] != str[size-i-1])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	ifstream inputFile;
	int a, b;
	unsigned int numberOfInputs;
	unsigned int inputNumber=0;
	inputFile.open("C-small-attempt0.in");

	if ( inputFile.good() )
	{
		inputFile >> numberOfInputs;
		while (inputNumber<numberOfInputs)
		{
			if (inputFile >> a >> b)
			{
				int count=0;
				for (long long int i=ceil(sqrt(a)); i<=sqrt(b); i++)
				{
					if( isPalindrome(i) && isPalindrome(i*i) )
					{
						count++;
					}
				}

				cout << "Case #" << ++inputNumber << ": " << count << endl;
			}
		}
	}

	return 0;
}
