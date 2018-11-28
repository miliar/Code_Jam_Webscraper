#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

bool isPalindrome(int num)
{
	string paliStr = to_string(num);

	for (int charN = 0; charN < floor(paliStr.length() / 2); charN++)
	{
		char c1 = paliStr[charN];
		char c2 = paliStr[paliStr.length() - 1 - charN];

		if (c1 != c2)
		{
			return false;
		}
	}

	return true;
}

int isSquare(int num)
{
	double sqN = sqrt(num);

	if (floor(sqN) == sqN)
	{
		return floor(sqN);
	}

	return 0;
}

bool isSqPalindrome(int num)
{
	int sqN = isSquare(num);

	if (sqN == 0)
	{
		return false;
	}

	if (isPalindrome(sqN) && isPalindrome(num))
	{
		return true;
	}

	return false;
}

int main()
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("output.txt");

	int numProblems;
	infile >> numProblems;

	string line;

	getline(infile, line);

	for (int problem = 1; problem <= numProblems; problem++)
	{
		getline(infile, line);

		stringstream ss(line);

		int bound1;
		int bound2;

		ss >> bound1 >> bound2;

		int SQPALINDS = 0;

		for (int i = bound1; i <= bound2; i++)
		{
			if (isSqPalindrome(i))
			{
				SQPALINDS++;
			}
		}

		outfile << "Case #" << problem << ": " << SQPALINDS << endl;
	}
}