#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;



int main(void)
{
	string s;
	getline(cin, s);

	int t = atoi(s.c_str());

	int num[10][26];
	for (int i = 0; i < 10; ++i)
	{
		for (int k = 0; k < 26; ++k)
		{
			num[i][k] = 0;
		}
	}
	// SET NUM
	struct NumInfo
	{
		int posCount;
		int pos[5];
	};
	NumInfo numInfo[10];
	for (int i = 0; i < 10; ++i)
	{
		numInfo[i].posCount = 0;
		for (int k = 0; k < 5; ++k)
		{
			numInfo[i].pos[k] = 0;
		}
	}
	char numStr[10][6] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	for (int i = 0; i < 10; ++i)
	{
		for (int k = 0; numStr[i][k] != 0 && k < 6; ++k)
		{
			char charNum = numStr[i][k] - 'A';
			num[i][charNum]++;
			bool exist = false;
			for (int m = 0; m < numInfo[i].posCount; ++m)
			{
				if (numInfo[i].pos[m] == charNum)
				{
					exist = true;
					break;
				}
			}

			if (exist) continue;

			numInfo[i].pos[numInfo[i].posCount] = charNum;
			numInfo[i].posCount++;
		}
	}

	////debugging
	//for (int i = 0; i < 10; ++i)
	//{
	//	cout << numInfo[i].posCount << "\t";
	//	for (int k = 0; k < 5; ++k)
	//	{
	//		cout << numInfo[i].pos[k] << " ";
	//	}
	//	cout << endl;
	//}

	int res[10];
	int count[26];
	for (int i = 1; i <= t; ++i)
	{
		s.clear();
		getline(cin, s);

		const char* pStr = s.c_str();

		for (int k = 0; k < 10; ++k)
		{
			res[k] = 0;
		}
		for (int k = 0; k < 26; ++k)
		{
			count[k] = 0;
		}

		// counting
		for (int k = 0; k < s.length(); ++k)
		{
			if (pStr[k] - 'A' >= 26)
			{
				cout << "ERROR" << endl;
			}
			count[pStr[k] - 'A']++;
		}

		cout << "Case #" << i << ": ";
		
		int cur = 0;
		while (cur < 10)
		{
			int charTypeCnt = numInfo[cur].posCount;
			//check
			bool next = false;
			for (int k = 0; k < charTypeCnt; ++k)
			{
				int pos = numInfo[cur].pos[k];
				if (count[pos] < num[cur][pos])
				{
					next = true;
					break;
				}
			}

			if (next)
			{
				cur+=2;
				if (cur == 10)
				{
					cur = 1;
				}
				continue;
			}

			//reduce count
			for (int k = 0; k < charTypeCnt; ++k)
			{
				int pos = numInfo[cur].pos[k];
				count[pos] -= num[cur][pos];
			}

			//print
			res[cur]++;
		}

		for (int k = 0; k < 10; ++k)
		{
			for (int m = 0; m < res[k]; ++m)
			{
				cout << k;
			}
		}
		cout << endl;
	}

	return 0;
}

