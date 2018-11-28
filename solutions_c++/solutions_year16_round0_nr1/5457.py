// TEST2.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
	ifstream oFileIn("aa.in");
	ofstream oFileOut("bb.out");

	int iT = 0;
	oFileIn >> iT;


	for (int i = 1; i <= iT; ++i)
	{
		unsigned long long iN = 0;
		oFileIn >> iN;

		if (iN == 0)
		{
			oFileOut << "Case #" << i << ": " << "INSOMNIA" << "\n";
			continue;
		}

		int j = 1;
		map<char, char> mapNums;
		char zNum[200];
		unsigned long long iAns = iN;

		while (mapNums.size() < 10)
		{
			iAns = iN * j;

			snprintf(zNum, 200, "%llu", iAns);


			int iIndex = 0;
			while (zNum[iIndex] != '\0')
			{
				mapNums[zNum[iIndex]] = '0';

				++iIndex;
			}

			++j;
		}



		oFileOut << "Case #" << i << ": " << iAns << "\n";

	}

	oFileIn.close();
	oFileOut.close();

	return 0;
}

