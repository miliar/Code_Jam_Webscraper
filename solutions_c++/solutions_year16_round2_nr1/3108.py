#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;
#pragma warning(disable:4996)

typedef unsigned int uint;

map<int, int> m_charactors;

void clearMap()
{
	for (int i = 0; i < 26; ++i)
	{
		m_charactors[i] = 0;
	}
}

void analyseString(const string& str)
{
	for (int i = 0; i < str.size(); ++i)
	{
		++m_charactors[(int)str[i] - 65];
	}
}

int getZeroCount()
{
	int zCount = m_charactors[25];
	m_charactors[25] = m_charactors[25] - zCount;
	m_charactors[4] = m_charactors[4] - zCount;
	m_charactors[17] = m_charactors[17] - zCount;
	m_charactors[14] = m_charactors[14] - zCount;

	return zCount;
}

int getTwoCount()
{
	int wCount = m_charactors[22];
	m_charactors[22] = m_charactors[22] - wCount;
	m_charactors[19] = m_charactors[19] - wCount;
	m_charactors[14] = m_charactors[14] - wCount;

	return wCount;
}

int getFourCount()
{
	int uCount = m_charactors[20];
	m_charactors[20] = m_charactors[20] - uCount;
	m_charactors[14] = m_charactors[14] - uCount;
	m_charactors[5] = m_charactors[5] - uCount;
	m_charactors[17] = m_charactors[17] - uCount;

	return uCount;
}

int getThreeCount()
{
	int rCount = m_charactors[17];
	m_charactors[17] = m_charactors[17] - rCount;
	m_charactors[19] = m_charactors[19] - rCount;
	m_charactors[7] = m_charactors[7] - rCount;
	m_charactors[4] = m_charactors[4] - rCount*2;

	return rCount;
}

int getSixCount()
{
	int xCount = m_charactors[23];
	m_charactors[23] = m_charactors[23] - xCount;
	m_charactors[8] = m_charactors[8] - xCount;
	m_charactors[18] = m_charactors[18] - xCount;

	return xCount;
}

int getSevenCount()
{
	int sCount = m_charactors[18];
	m_charactors[18] = m_charactors[18] - sCount;
	m_charactors[4] = m_charactors[4] - sCount*2;
	m_charactors[21] = m_charactors[21] - sCount;
	m_charactors[13] = m_charactors[13] - sCount;

	return sCount;
}

int getEightCount()
{
	int gCount = m_charactors[6];
	m_charactors[6] = m_charactors[6] - gCount;
	m_charactors[4] = m_charactors[4] - gCount;
	m_charactors[8] = m_charactors[8] - gCount;
	m_charactors[7] = m_charactors[7] - gCount;
	m_charactors[19] = m_charactors[19] - gCount;

	return gCount;
}

int getOneCount()
{
	int oCount = m_charactors[14];
	m_charactors[14] = m_charactors[14] - oCount;
	m_charactors[13] = m_charactors[13] - oCount;
	m_charactors[4] = m_charactors[4] - oCount;

	return oCount;
}

int getFiveCount()
{
	int fCount = m_charactors[5];
	m_charactors[5] = m_charactors[5] - fCount;
	m_charactors[8] = m_charactors[8] - fCount;
	m_charactors[21] = m_charactors[21] - fCount;
	m_charactors[4] = m_charactors[4] - fCount;

	return fCount;
}

int getNineCount()
{
	return m_charactors[4];
}

int main()
{
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\input.in", "r", stdin);
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\output.txt", "w", stdout);

	size_t testCases;
	cin >> testCases;
	size_t caseNumber = 1;

	while (caseNumber <= testCases)
	{
		string S;
		cin >> S;
		clearMap();
		analyseString(S);

		map<int, int> digitCount;

		digitCount[0] = getZeroCount();
		digitCount[2] = getTwoCount();
		digitCount[4] = getFourCount();
		digitCount[3] = getThreeCount();
		digitCount[6] = getSixCount();
		digitCount[7] = getSevenCount();
		digitCount[8] = getEightCount();
		digitCount[1] = getOneCount();
		digitCount[5] = getFiveCount();
		digitCount[9] = getNineCount();

		cout << "Case #" << caseNumber << ": ";

		for (int i = 0; i < 10; ++i)
		{
			for (int j = digitCount[i]; j > 0; --j)
			{
				cout << i;
			}
		}

		cout << endl;
		++caseNumber;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}