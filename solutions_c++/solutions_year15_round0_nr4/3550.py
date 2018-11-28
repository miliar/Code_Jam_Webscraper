// CPP file
// Created in Microsoft VS2013 Community 

#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

int main()
{
	unsigned int uiT = 0; // test cases
	vector<unsigned int> conXes;
	vector<unsigned int > conRes;
	vector<unsigned int> conCes;

	vector<bool> conRichardWins; // true if Richard wins, false if Gabriel

	string sFileName = "D-small-attempt1";

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s(stream, "%d", &uiT);

		for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
		{
			// reading data for each test case

			unsigned int uiX = 0;
			fscanf_s(stream, "%d", &uiX);
			conXes.push_back(uiX);
			unsigned int uiR = 0;
			fscanf_s(stream, "%d", &uiR);
			conRes.push_back(uiR);
			unsigned int uiC = 0;
			fscanf_s(stream, "%d", &uiC);
			conCes.push_back(uiC);
		}

		// closing file
		fclose(stream);
	}
	//--------------------- end - reading from file -----------------------


	//--------------------- begin - algorithm ---------------------
	// FOR SMALL INPUT ONLY
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		if (conXes[uiIdx] == 1)
		{
			// Gabriel wins
			conRichardWins.push_back(false);
		}
		if (conXes[uiIdx] == 2 )
		{
			if (((conRes[uiIdx] * conCes[uiIdx]) % 2 == 0))
			{ 
				// Gabriel wins
				conRichardWins.push_back(false);
			}
			else
			{
				// Richard wins
				conRichardWins.push_back(true);
			}
		} // end if X == 2
		if ( conXes[uiIdx] == 3 )
		{
			if (((conRes[uiIdx] * conCes[uiIdx]) % 3 == 0))
			{
				if ((conRes[uiIdx] * conCes[uiIdx]) >= 6)
				{
					// Gabriel wins
					conRichardWins.push_back(false);
				}
				else
				{
					// Richard wins
					conRichardWins.push_back(true);
				}
			}
			else
			{
				// Richard wins
				conRichardWins.push_back(true);
			}
		} // end if X == 3
		if ( conXes[uiIdx] == 4 )
		{ 
			if (((conRes[uiIdx] * conCes[uiIdx]) % 4 == 0))
			{
				if ((conRes[uiIdx] * conCes[uiIdx]) == 4)
				{
					// Richard
					conRichardWins.push_back(true);
				}
				else if ((conRes[uiIdx] * conCes[uiIdx]) == 8)
				{
					// Richard
					conRichardWins.push_back(true);
				}
				else if ((conRes[uiIdx] * conCes[uiIdx]) == 12)
				{
					// Gabriel
					conRichardWins.push_back(false);
				}
				else if ((conRes[uiIdx] * conCes[uiIdx]) == 16)
				{
					// Gabriel
					conRichardWins.push_back(false);
				}
				else
				{
					assert(!"Wrong!");
					conRichardWins.push_back(false); // wrong
				}
			}
			else
			{
				// Richard
				conRichardWins.push_back(true);
			}
		} // end if X == 4
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		string sWinner = conRichardWins[uiIdx] ? "RICHARD" : "GABRIEL";
		out << "Case #" << uiIdx + 1 << ": " << sWinner << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

