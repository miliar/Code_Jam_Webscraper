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

	unsigned int uiN = 0; // digits

	unsigned int uiJ = 0; // different results

	vector<string> vecNumber;
	vector<vector<unsigned int>> vecDividers;

	string sFileName = "C-small-attempt0";

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s( stream, "%d", &uiT );

		for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
		{
			// reading data for each test case

			// ONLY FOR uiT = 1
			fscanf_s(stream, "%d", &uiN);

			fscanf_s(stream, "%d", &uiJ);
		}

		// closing file
		fclose( stream );
	}
	//--------------------- end - reading from file -----------------------
	

	//--------------------- begin - algorithm ---------------------
	for (unsigned int uiIdx = 0; uiIdx < uiJ; ++uiIdx)
	{
		// creating a number
		string sNumber = "1";
		unsigned int uiDivRes = uiIdx;
		for (unsigned int uii = 1; uii < (uiN / 2) - 1; ++uii)
		{
			if(uiDivRes % 2 == 0)
			{ 
				sNumber += "0";
			}
			else
			{
				sNumber += "1";
			}	
			uiDivRes = uiDivRes / 2;
		}
		sNumber += "1";

		vecNumber.push_back(sNumber);

		// base-2
		unsigned int uiB2 = stoi(sNumber, nullptr, 2);;

		vector<unsigned int> vecTemp;
		for (unsigned int uik = 2; uik <= 10; ++uik)
		{
			vecTemp.push_back(stoi(sNumber, nullptr, uik));
		}
		vecDividers.push_back(vecTemp);
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ":" << endl;
		for (unsigned int uiIdx_2 = 0; uiIdx_2 < uiJ; ++ uiIdx_2)
		{
			out << vecNumber[uiIdx_2] << vecNumber[uiIdx_2]  << " ";
			for (unsigned int uiIdx_3 = 0; uiIdx_3 < 9; ++uiIdx_3)
			{
				out << vecDividers[uiIdx_2][uiIdx_3] << " ";
			}
			out << endl;
		}
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

