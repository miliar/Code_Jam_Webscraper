#include <fstream>
#include <string>
using namespace std;

int main()
{
	int					nCases, nIndex = 0;
	string::size_type	nMaxShyness;
	string				strAudience;
	long long			nResult = 0, nAudienceCount = 0;

	ifstream	InFile("A-large-Jam.in");
	ofstream	OutFile("A-large-Jam.out", ios_base::ate || ios_base::out);

	InFile >> nCases;

	if (OutFile.is_open())
	{
		while (nCases--)
		{
			InFile >> nMaxShyness >> strAudience;
			nResult = 0;
			nAudienceCount = 0;

			if (strAudience[0] != '0')
				nAudienceCount = strAudience[0] - '0';

			for (string::size_type i = 1; i <= nMaxShyness; ++i)
			{
				if (strAudience[i] == '0')
					continue;

				if (nAudienceCount < (long long)i)
				{
					nResult += ((long long)i - nAudienceCount);
					nAudienceCount += ((long long)i - nAudienceCount);
				}

				nAudienceCount += ((long long)strAudience[i] - (long long)'0');
			}

			OutFile << "Case #" << ++nIndex << ": " << nResult << endl;
		}
	}

	InFile.close();
	OutFile.close();
	return 0;
}
