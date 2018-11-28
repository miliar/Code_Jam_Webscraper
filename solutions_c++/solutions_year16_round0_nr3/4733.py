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

	int j, l, Ncases;

	cin >> Ncases;
	int nLength = 0;
	int jamCoins = 0;
	char cZero = '0';
	char cOne = '1';
	l = 0;

	cin >> nLength >> jamCoins;
	cout << "Case #1:" << endl;

	// Number of jam coins
	//for (i = 0; i<jamCoins; i++)
	while (jamCoins > 0)
	{
		short found = 0;
		string divisors;	// , vals;
		long long val = 0;
		char jamString[17], incStr[15];
		while (found < 9)
		{
			memset(jamString, 0x00, 17);
			memset(jamString, cZero, 16);
			memset(incStr, 0x00, 15);
			jamString[16] = 0;
			jamString[0] = cOne;
			jamString[15] = cOne;

			_itoa(l++, incStr, 2);
			memcpy(&jamString[15 - strlen(incStr)], incStr, strlen(incStr));
			
			for (j = 2; j < 11; j++)
			{
				bool gotIt = false;
				long long k;
				val = strtoll(jamString, '\0', j);
				/*vals += " ";
				char tmp1Str[50];
				memset(tmp1Str, 0x00, 50);
				_i64toa(val, tmp1Str, 10);
				vals.append(tmp1Str);*/
				for (k = 2; k*k < val; k++)
				{
					if ((val % k) == 0)
					{
						divisors.append(" ");
						char tmpStr[50];
						memset(tmpStr, 0x00, 50);
						_i64toa(k, tmpStr, 10);
						divisors.append(tmpStr);
						gotIt = true;
						break;
					}
				}
				if (gotIt)
					found++;
				else
				{
					found = 10;
					break;
				}
			}
		}
		if (found == 9)
		{
			//cout << jamString << ":" << vals << " -- " << divisors << endl;
			cout << jamString << divisors << endl;
			jamCoins--;
		}
	}

	return 0;
}

