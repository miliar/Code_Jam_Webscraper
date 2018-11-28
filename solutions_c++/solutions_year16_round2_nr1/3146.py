
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <math.h>

using namespace std;


map<char, int> mapInput;
list<int> lstOut;

const char* num[] = {
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX",
	"SEVEN",
	"EIGHT",
	"NINE" };


void numberFound(int iNum)
{
	int iLen = strlen(num[iNum]);

	for (int k = 0; k < iLen; ++k)
	{
		mapInput[num[iNum][k]]--;

		if (mapInput[num[iNum][k]] < 0)
			break;


	}

	lstOut.push_back(iNum);
}
int main()
{
	ifstream oFileIn("aa.in");
	ofstream oFileOut("bb.out");

	int iT = 0;
	oFileIn >> iT;


	
	
	for (int i = 1; i <= iT; ++i)
	{
		

		mapInput.clear();
		lstOut.clear();

		oFileOut << "Case #" << i << ": ";

		string s;
		oFileIn >> s;

		

		int iStrLen = s.size();
		
		for (int j = 0; j < iStrLen; ++j)
		{
			mapInput[s[j]]++;
		}

		
		while (true)
		{
			bool bFound = false;

			if (mapInput['Z'] > 0)
			{
				bFound = true;
				numberFound(0);
			}
			if (mapInput['W'] > 0)
			{
				bFound = true;
				numberFound(2);
			}
			if (mapInput['U'] > 0)
			{
				bFound = true;
				numberFound(4);
			}
			if (mapInput['X'] > 0)
			{
				bFound = true;
				numberFound(6);
			}
			if (mapInput['G'] > 0)
			{
				bFound = true;
				numberFound(8);
			}

			if (bFound == false)
				break;
		}

		while (true)
		{
			bool bFound = false;

			if (mapInput['O'] > 0)
			{
				bFound = true;
				numberFound(1);
			}
			if (mapInput['T'] > 0)
			{
				bFound = true;
				numberFound(3);
			}
			if (mapInput['F'] > 0)
			{
				bFound = true;
				numberFound(5);
			}
			if (mapInput['S'] > 0)
			{
				bFound = true;
				numberFound(7);
			}
			

			if (bFound == false)
				break;
		}

		while (true)
		{
			bool bFound = false;

			if (mapInput['N'] > 0)
			{
				bFound = true;
				numberFound(9);
			}
		
			if (bFound == false)
				break;
		}

		lstOut.sort();

		auto ite = lstOut.begin();
		auto iteEnd = lstOut.end();

		while (ite != iteEnd)
		{
			oFileOut << *ite;
			++ite;
		}

		oFileOut << "\n";

	}

	oFileIn.close();
	oFileOut.close();

	return 0;
}

