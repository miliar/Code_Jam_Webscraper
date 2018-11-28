#include <string>
#include <utility>
#include <cmath>
#include  <fstream>
#include <algorithm>
using namespace std;

unsigned int CoinJamTable[17][51][51][10];

unsigned int TestPrimility(unsigned int iNumber, unsigned int iBase)
{
	long long			llNumber = 0;
	unsigned int		iStop;
	unsigned long long	iBaseValue = 1;

	while (iNumber)
	{
		if (iNumber & 1)
			llNumber += iBaseValue;

		iBaseValue *= iBase;
		iNumber >>= 1;
	}

	if ((llNumber & 1) == 0)
		return 2;

	iStop = sqrt((long double)llNumber);

	for (unsigned int x = 3; x <= iStop; x+=2)
	{
		if ((llNumber % x) == 0)
			return x;
	}

	return 0;
}

#include <set>

int main()
{
	/*PreCompute*/
	for (int i = 2; i <= 16; ++i)
	{
		long long llbase = pow((long double)2, i - 1) + 1;

		int	j = 1;
		long double	iPartEnd = pow((long double)2, i - 2) - 1;

		for (int iPart = 0; iPart <= iPartEnd; ++iPart)
		{
			int	iBase;

			unsigned int	arrayRes[10] = {llbase + (iPart << 1)};

			for (iBase = 2; iBase <= 10; ++iBase)
			{
				unsigned int result = TestPrimility(llbase + (iPart << 1), iBase);

				if (result != 0)
					arrayRes[iBase - 1] = result;
				else
					break;
			}

			if (iBase == 11)
			{
				for (int x = j; x <= 50; ++x)
				{
					for (int iIterator = 0; iIterator < 10; ++iIterator)
						CoinJamTable[i][x][j][iIterator] = arrayRes[iIterator];
				}

				if (++j > 50)
					break;
			}
		}
	}

	ifstream		InFile("C-small-attempt1.in");
	ofstream		OutFile("C-small-attempt1.out", ios_base::ate || ios_base::out);

	unsigned int	T, iIndex = 0;

	if (OutFile.is_open() && InFile.is_open())
	{
		InFile >> T;

		while (T--)
		{
			unsigned int	N, J;
			InFile >> N >> J;

			OutFile << "Case #" << ++iIndex << ":" << endl;

			for (int i = 1; i <= J; ++i)
			{
				unsigned int iNumber = CoinJamTable[N][J][i][0];

				string	strNumber;

				while (iNumber)
				{
					if (iNumber & 1)
						strNumber += '1';
					else
						strNumber += '0';

					iNumber >>= 1;
				}

				reverse(strNumber.begin(), strNumber.end());

				for (int x = 0; x < N - strNumber.length(); ++x)
					OutFile << '0';

				OutFile << strNumber << " ";

				for (int x = 1; x < 9; ++x)
					OutFile << CoinJamTable[N][J][i][x] << " ";

				OutFile << CoinJamTable[N][J][i][9] << endl;
			}
		}
	}

	return 0;
}