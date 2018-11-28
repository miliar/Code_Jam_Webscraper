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
#include <bitset> 

using namespace std;

vector<long> vecPrimeNos;

int main()
{

	ifstream oFileIn("aa.in");
	ofstream oFileOut("bb.out");

	ifstream oFilePrimeIn("prime.txt");

	for (long i = 0; i < 10000000; ++i)
	{
		long iPrime;

		oFilePrimeIn >> iPrime;

		vecPrimeNos.push_back(iPrime);
	}

	int iT = 1;
	int iSizeOfPrimeNum = vecPrimeNos.size();
	//oFileIn >> iT;

	for (int i = 1; i <= iT; ++i)
	{
		oFileOut << "Case #" << i << ":" << "\n";

		//int iN;
		int iJ = 50;
		//oFileIn >> iN >> iJ;

		int iFoundCount = 0;
		char zCandidate[20];

		for (int j = 32769; j <= 65535; j = j + 2)
		{

			bitset<16> value = j;
			strncpy(zCandidate, value.to_string().c_str(), 20);

			int aiDevicers[10];

			bool bFoundDevicer = false;

			for (int k = 2; k <= 10; ++k)
			{
				long long int iValue = strtoll(zCandidate, NULL, k);
				bFoundDevicer = false;
				double dLimit = sqrt(iValue);
				
				for (int m = 0; m < iSizeOfPrimeNum && dLimit > vecPrimeNos[m]; m++)
				{
					if (iValue % vecPrimeNos[m] == 0)
					{
						aiDevicers[k - 2] = vecPrimeNos[m];
						bFoundDevicer = true;
						break;
					}

				}

				if (bFoundDevicer == false)
				{
					break;
				}
			}

			if (bFoundDevicer)
			{
				oFileOut << zCandidate;

				for (int k = 2; k <= 10; k++)
				{
					oFileOut << " " << aiDevicers[k - 2];
				}

				oFileOut << "\n";

				++iFoundCount;

				if (iFoundCount >= iJ)
					break;

			}

		}

	}

	oFileIn.close();
	oFileOut.close();

	return 0;
}

