// CookieClickerAlpha.cpp
//

#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

int main()
{
	string sFileName = "B-large";

	ifstream in(sFileName + ".in");

	int i = 0;
	string sLine;

	vector< vector< long double> > colTestCases;

	unsigned int uiT = 0;

	while (getline(in, sLine))
	{
		if (i == 0)
		{
			// T
			uiT = stoi(sLine);
		}
		else
		{
			int iPos0 = sLine.find(" ");
			string s0 = sLine.substr(0, iPos0);
			sLine.erase(0, iPos0 + 1);
			int iPos1 = sLine.find(" ");
			string s1 = sLine.substr(0, iPos1);
			sLine.erase(0, iPos1 + 1);
			string s2 = sLine.substr(0, sLine.find(" "));

			vector<long double> colEachTestCase;

			colEachTestCase.push_back(stold(s0)); // C
			colEachTestCase.push_back(stold(s1)); // F
			colEachTestCase.push_back(stold(s2)); // X

			colTestCases.push_back( colEachTestCase );
		}
		++i;
	}

	assert( colTestCases.size() == uiT ); // something's seriously wrong

	vector< long double > colSecondsToWin; // seconds to win for each test case

	for (unsigned int uiTestCaseIdx = 0; uiTestCaseIdx < uiT; ++uiTestCaseIdx)
	{
		bool bFinished = false;
		long double ldCookiesPerSec = 2.0; // value of cookies/sec - initial value: 2/sec
		long double ldSeconds = 0.0; // min value of seconds needed to win this game
		long double ldCurrentCookies = 0.0; // current number of cookies

		long double ldC = colTestCases[uiTestCaseIdx][ 0 ];
		long double ldF = colTestCases[uiTestCaseIdx][ 1 ];
		long double ldX = colTestCases[uiTestCaseIdx][ 2 ];

		while (!bFinished)
		{
			if ( ( ( ldC / ldCookiesPerSec ) + ( ldX / ( ldCookiesPerSec + ldF ) ) ) < ( ldX / ldCookiesPerSec ) )
			{
				// it is better to buy a farm
				ldSeconds += ( ldC / ldCookiesPerSec );
				ldCurrentCookies = 0.0;
				ldCookiesPerSec += ldF;
			}
			else
			{
				// it is better to wait for X cookies than buy a farm
				ldSeconds += ( ldX / ldCookiesPerSec );
				colSecondsToWin.push_back( ldSeconds );
				bFinished = true;
			}
		}
	}

	// printing to file
	ofstream out;
	out.open(sFileName + ".txt");
	out.precision(7);
	out.setf(std::ios::fixed, std::ios::floatfield);
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << colSecondsToWin[uiIdx] << endl;
	}

	out.close();

	return 0;
}

