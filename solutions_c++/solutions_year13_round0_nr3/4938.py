#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <math.h>

using namespace std;

static ifstream fi;
static ofstream fo;

void redirectInput(const std::string& fileName)
{
	fi.open(fileName, std::ios_base::in);
	std::cin.rdbuf(fi.rdbuf());
}

void redirectOutput(const std::string& fileName)
{
	fo.open(fileName, std::ios_base::out);
	std::cout.rdbuf(fo.rdbuf());
}

enum GameState
{
	ePlaying,
	eYes,
	eNo,
	eDraw,
};

bool isPalindrome(int n) 
{
	int p = n;
	int r = 0;

	while (p != 0) 
	{
		int d = p % 10;
		r = r * 10 + d;
		p = p / 10;
	}

	return (n == r);
}

bool isFairAndSquare(int n)
{
	if (isPalindrome(n))
	{
		int sqrN = (int) sqrt(float(n));
		if (sqrN * sqrN == n)
		{
			return isPalindrome(sqrN);
		}
	}

	return false;
}

void main()
{
	redirectInput("in.txt");
	redirectOutput("out.txt");

	int caseCount;
	std::string str;
	int i,j;

	int min, max;
	int nCount;

	cin >> caseCount;
	cin.get();

	if (caseCount < 1 || caseCount > 100)
		return;

	for (i = 0; i < caseCount; ++i)
	{
		cin >> min;
		cin.get();
		cin >> max;
		cin.get();

		nCount = 0;

		// Lawn pattern loading
		for (j = min; j <= max; ++j)
		{
			if (isFairAndSquare(j))
				nCount ++;
		}
				
		cout << "Case #" << (i + 1) << ": " << nCount << endl;
	}
}
