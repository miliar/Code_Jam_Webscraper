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

	string sFileName = "D-small-attempt1";

	vector<unsigned int> vecK; // K - string length
	vector<unsigned int> vecC; // C - complexity
	vector<unsigned int> vecS; // S - students
	vector<vector<unsigned int>> vecTILES; // which tiles should be searched


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

			unsigned int uiK = 0;
			fscanf_s(stream, "%d", &uiK);
			vecK.push_back(uiK);

			unsigned int uiC = 0;
			fscanf_s(stream, "%d", &uiC);
			vecC.push_back(uiC);

			unsigned int uiS = 0;
			fscanf_s(stream, "%d", &uiS);
			vecS.push_back(uiS);
			
		}

		// closing file
		fclose( stream );
	}
	//--------------------- end - reading from file -----------------------
	

	//--------------------- begin - algorithm --------------------- 
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		vector<unsigned int> vecTempTiles;
		unsigned int uiTileNumber = 0;
		if (vecC[uiIdx] == 1 )
		{
			if (vecS[uiIdx] >= vecK[uiIdx])
			{
				for (unsigned int uiii = 0; uiii < vecK[uiIdx]; ++uiii)
				{
					vecTempTiles.push_back(uiii+1);
				}
			}
		}

		if (vecC[uiIdx] >= 2 && vecK[uiIdx] < 4)
		{
			unsigned int uiTempK = vecK[uiIdx] - 1;
			if ( uiTempK == 0 )
			{
				uiTileNumber = 1;
				vecTempTiles.push_back(uiTileNumber);
			}
			while (uiTempK != 0)
			{
				uiTileNumber += vecK[uiIdx];
				vecTempTiles.push_back(uiTileNumber);
				uiTempK--;
			}
		}

		if (vecC[uiIdx] >= 2 && vecK[uiIdx] >= 4)
		{
			unsigned int uiTempK = vecK[uiIdx] - 1;
			while (uiTempK > 2)
			{
				uiTileNumber += vecK[uiIdx];
				vecTempTiles.push_back(uiTileNumber);
				uiTempK--;
			}
			if (uiTempK == 2)
			{
				uiTileNumber += vecK[uiIdx] - 1;
				vecTempTiles.push_back(uiTileNumber);
			}
		}
		if (vecTempTiles.size() > vecS[uiIdx])
		{
			vecTempTiles.clear();
		}
		vecTILES.push_back( vecTempTiles );
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		if(vecTILES[uiIdx].empty())
		{
			out << "Case #" << uiIdx + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			out << "Case #" << uiIdx + 1 << ": ";
			for (unsigned int uiI = 0; uiI < vecTILES[uiIdx].size(); uiI++ )
			{
				out << vecTILES[uiIdx][uiI] << " ";
			}
			out << endl;
		}

	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

