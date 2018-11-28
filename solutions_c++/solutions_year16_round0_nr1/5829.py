// GCJ.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <math.h>
#include <functional>

//#define verbose

using namespace std;

int main()
{
	// First let's read the file
	freopen("gcj.in", "r", stdin);
	freopen("gcj.out", "w", stdout);

	int i, j, k, Ncases;

	cin >> Ncases;

	// Test cases
	for (i=0; i<Ncases; i++)
	{
		int baseNum = 0;
		bool s0 = false, s1 = false, s2 = false, s3 = false, s4 = false, s5 = false, s6 = false, s7 = false, s8 = false, s9 = false;
		char numStr[20];
		memset(numStr, 0x00, 20);

		cin >> baseNum;
		if (baseNum == 0)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		//cout << "Case #" << i + 1 << ": " << baseNum << " ";
		k = 2;
		int currNum = baseNum;
		int lastNum = currNum;

		while (!(s0 && s1 && s2 && s3 && s4 && s5 && s6 && s7 && s8 && s9))
		{
			// convert the number to a string and parse
			memset(numStr, 0x00, 20);
			_itoa(currNum, numStr, 10);
			int digits = strlen(numStr);
			for (j = 0; j < digits; j++)
			{
				char tmpChar = numStr[j];
				short digVal = tmpChar - 48;
				switch (digVal)
				{
				case 0:
					s0 = true;
					break;
				case 1:
					s1 = true;
					break;
				case 2:
					s2 = true;
					break;
				case 3:
					s3 = true;
					break;
				case 4:
					s4 = true;
					break;
				case 5:
					s5 = true;
					break;
				case 6:
					s6 = true;
					break;
				case 7:
					s7 = true;
					break;
				case 8:
					s8 = true;
					break;
				case 9:
					s9 = true;
					break;
				}
			}
			//cout << lastNum << ":";
			lastNum = currNum;
			currNum = baseNum * k++;
		}

		//cout << lastNum << endl;
		cout << "Case #" << i + 1 << ": " << lastNum << endl;
	}

	return 0;
}

