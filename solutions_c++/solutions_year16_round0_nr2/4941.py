#include <string>
#include  <fstream>
#include <algorithm>
using namespace std;

char ReverseBanCake (char ch) { if (ch == '+') return '-'; return'+'; }

int main()
{
	unsigned int		T, nIndex = 0;
	string				strPanCakes;

	strPanCakes.reserve(100);

	ifstream	InFile("B-large.in");
	ofstream	OutFile("B-large.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open() && InFile.is_open())
	{
		InFile >> T;

		while (T--)
		{
			InFile >> strPanCakes;

			int iEnd = strPanCakes.length() - 1;
			int iSteps = 0;

			while (iEnd >= 0)
			{
				while ((iEnd >= 0) && (strPanCakes[iEnd] == '+'))
					--iEnd;

				if (!(iEnd < 0 ))
				{
					int	iStart = 0;

					while ((iStart < iEnd) && (strPanCakes[iStart] == '+'))
						++iStart;

					if (iStart != 0)
					{
						++iSteps;
						std::fill_n(strPanCakes.begin(), iStart, '-');
					}

					std::transform(strPanCakes.begin(), strPanCakes.begin() + iEnd + 1, strPanCakes.begin(), ReverseBanCake);
					std::reverse(strPanCakes.begin(), strPanCakes.begin() + iEnd + 1);
					--iEnd;
					++iSteps;
				}
			}

			OutFile << "Case #" << ++nIndex << ": " << iSteps << endl;	
		}
	}

	return 0;
}
