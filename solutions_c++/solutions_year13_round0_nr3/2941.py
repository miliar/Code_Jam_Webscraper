#include "FairAndSquare.h"

bool FairAndSquare::isSquare(int number)
{
	int lastDigit = number % 10;
	switch (lastDigit)
	{
	case 0:
		{
			int NofZeroes = 0;
			while (number && number % 10 == 0)
			{
				number /= 10;
				++NofZeroes;
			}
			if (NofZeroes && NofZeroes % 2 == 0)
				return isSquare(number / pow(static_cast<double>(10),NofZeroes));
			else
				return false;
		}
		break;
	case 1:
		{
			if ((number - number % 10) % 4 == 0 && 
				((int)sqrt((double) number) % 10 == 1 || (int)sqrt((double) number) % 10 == 9))
				return true;
			return false;
		}
	case 9:
		{
			if ((number - number % 10) % 4 == 0 &&
				((int)sqrt((double) number) % 10 == 3 || (int)sqrt((double) number) % 10 == 7))
				return true;
			return false;
		}
		break;
	case 4:
		{
			if ((number - number % 10) % 2 == 0 &&
				((int)sqrt((double) number) % 10 == 2 || (int)sqrt((double) number) % 10 == 8))
				return true;
			return false;
		}
		break;
	case 6:
		{
			if ((number - number % 10) % 2 == 1 &&
				((int)sqrt((double) number) % 10 == 4 || (int)sqrt((double) number) % 10 == 6))
				return true;
			return false;
		}
	case 5:
		{
			if(number % 100 == 25)
			{
				if (number >= 10000 && (number - 25) % 10000 == 0 || 
					number >= 1000 && (number - 25) % 1000 == 2 ||
					number >= 1000 && (number - 25) % 1000 == 6 || 
					number >= 1000 && (number - 25) % 1000 == 56 &&
					((int)sqrt((double) number) % 10 == 5))
					return true;
				return false;
			}
			else 
				return false;
		}
		break;
	default:
		return false;
	}
}

bool FairAndSquare::isPallindrom(int number)
{
	int root = ceil(sqrt((double)number));
	string rootStr = to_string(static_cast<long long>(root));
	string rootReverse = rootStr;
	std::reverse(rootReverse.begin(), rootReverse.end());
	string tmp = to_string(static_cast<long long>(number));
	string strReverse = tmp;
	std::reverse(strReverse.begin(), strReverse.end());
	return tmp == strReverse && rootStr == rootReverse;
}

int FairAndSquare::CountInRange(int start, int end)
{
	int counter = 0;
	for (int i = start; i <= end; ++i)
	{
		if (isSquare(i) && isPallindrom(i))
			++counter;
	}
	return counter;
}

void FairAndSquare::start(void)
{
	ifstream in(m_fileInput);
	ofstream out(m_fileOutput);

	int numberOfCases;
	in >> numberOfCases;
	int start; int end;
	int result;
	for (int i = 1; i <= numberOfCases; ++i)
	{
		start = end = result = 0;
		in >> start >> end;
		result = CountInRange(start, end);
		out << "Case #" << i << ": " << result << endl;
	}
}


