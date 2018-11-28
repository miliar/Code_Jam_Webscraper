// MagicTrick.cpp
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
	string sFileName = "A-small-attempt0";

	ifstream in(sFileName + ".in");

	int i = 0;
	unsigned int uiT = 0;
	string sLine;

	vector<string> colSingleCase;
	vector<vector<string>> colCases;

	while (getline(in, sLine))
	{
		if (i == 0)
		{
			uiT = stoi(sLine);
		}
		else
		{
			colSingleCase.push_back(sLine);
			if (i % 10 == 0)
			{
				colCases.push_back(colSingleCase);
				colSingleCase.clear();
			}
		}
		++i;
	}

	assert(colCases.size() == uiT); // something's seriously wrong

	vector<string> colOutputCases;
	string sBadMagician = "Bad magician!";
	string sVolunteerCheated = "Volunteer cheated!";

	for (unsigned int uiTestCaseIDx = 0; uiTestCaseIDx < uiT; ++uiTestCaseIDx)
	{
		unsigned int uiFirstRow = stoi( colCases[uiTestCaseIDx][0] );
		unsigned int uiSecondRow = stoi( colCases[uiTestCaseIDx][5] );

		string sFirstRow = colCases[uiTestCaseIDx][uiFirstRow];
		string sSecondRow = colCases[uiTestCaseIDx][uiSecondRow + 5];

		vector<unsigned int> colFirstRow;
		vector<unsigned int> colSecondRow;

		int iPos0 = sFirstRow.find(" ");
		string s0 = sFirstRow.substr(0, iPos0);
		sFirstRow.erase(0, iPos0 + 1);
		int iPos1 = sFirstRow.find(" ");
		string s1 = sFirstRow.substr(0, iPos1);
		sFirstRow.erase(0, iPos1 + 1);
		int iPos2 = sFirstRow.find(" ");
		string s2 = sFirstRow.substr(0, iPos2);
		sFirstRow.erase(0, iPos2 + 1);
		string s3 = sFirstRow.substr(0, sLine.find(" "));

		colFirstRow.push_back(stoi(s0));
		colFirstRow.push_back(stoi(s1));
		colFirstRow.push_back(stoi(s2));
		colFirstRow.push_back(stoi(s3));

		iPos0 = sSecondRow.find(" ");
		s0 = sSecondRow.substr(0, iPos0);
		sSecondRow.erase(0, iPos0 + 1);
		iPos1 = sSecondRow.find(" ");
		s1 = sSecondRow.substr(0, iPos1);
		sSecondRow.erase(0, iPos1 + 1);
		iPos2 = sSecondRow.find(" ");
		s2 = sSecondRow.substr(0, iPos2);
		sSecondRow.erase(0, iPos2 + 1);
		s3 = sSecondRow.substr(0, sLine.find(" "));

		colSecondRow.push_back(stoi(s0));
		colSecondRow.push_back(stoi(s1));
		colSecondRow.push_back(stoi(s2));
		colSecondRow.push_back(stoi(s3));

		bool bFound = false;
		assert( colFirstRow.size() == 4 );
		assert( colSecondRow.size() == 4 );
		string sChosenCard = "";
		for (unsigned int uiIdx = 0; uiIdx < 4; ++uiIdx)
		{
			if (std::find(std::begin(colSecondRow), std::end(colSecondRow), colFirstRow[uiIdx]) != std::end(colSecondRow))
			{
				if (!bFound)
				{
					bFound = true;
					sChosenCard = to_string(colFirstRow[uiIdx]);
				}
				else
				{
					sChosenCard = sBadMagician;
					break;
				}
			}
		}
		if ( sChosenCard.empty() )
		{
			sChosenCard = sVolunteerCheated;
		}
		colOutputCases.push_back(sChosenCard);	
	}

	// printing to file
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << colOutputCases[uiIdx] << endl;
	}

	out.close();

	return 0;
}

