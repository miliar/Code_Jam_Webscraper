// CPP file
// Created in Microsoft VS2015 Community 

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

	string sFileName = "A-large";

	vector<string> vecWords;
	vector<string> vecResults;

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s( stream, "%d", &uiT ); // "%ld"   "%f"   "%c"

		for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
		{
			// reading data for each test case

			//unsigned int uiNumber = 0;

			char sWords[1005];
			fscanf_s(stream, "%s", sWords, _countof(sWords));
			string s1 = string(sWords);

			string s2 = "";

			vecWords.push_back(sWords);

		}

		// closing file
		fclose( stream );
	}
	//--------------------- end - reading from file -----------------------
	

	//--------------------- begin - algorithm ---------------------
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		string sResult;
			for (unsigned int uij = 0; uij < vecWords[uiIdx].length(); ++uij)
			{
				if (uij == 0)
				{
					sResult = vecWords[uiIdx][0];
				}
				else
				{
					if (vecWords[uiIdx][uij] >= sResult[0])
					{
						sResult.insert(sResult.begin(), vecWords[uiIdx][uij]);
					}
					else
					{
						sResult.insert(sResult.end(), vecWords[uiIdx][uij]);
					}
				}

			}
		vecResults.push_back(sResult);
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << vecResults[uiIdx] << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

