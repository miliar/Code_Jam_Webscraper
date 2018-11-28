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

	string sFileName = "B-large";

	vector<vector<bool>> vecPancakes;
	vector<unsigned int> vecResults;

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

			char sKeys[105];
			fscanf_s(stream, "%s", sKeys, _countof(sKeys));
			string s1 = string(sKeys);
			vector<bool> vecTemp;
			for (unsigned int uii = 0; uii < s1.size(); ++uii)
			{
				if (s1[uii] == '+' )
				{
					vecTemp.push_back(true);
				}
				else
				{
					vecTemp.push_back(false);
				}
			}
			vecPancakes.push_back(vecTemp);
		}

		// closing file
		fclose( stream );
	}
	//--------------------- end - reading from file -----------------------
	

	//--------------------- begin - algorithm ---------------------
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		unsigned int uiFlip = 0;
		for ( int ii = vecPancakes[uiIdx].size() - 1; ii >= 0; --ii)
		{
			if (!vecPancakes[uiIdx][ii] && !vecPancakes[uiIdx][0] )
			{
				uiFlip++;
				vector<bool> vecTemp_1;
				for ( int ij = ii; ij >= 0; --ij )
				{
					vecTemp_1.push_back( !vecPancakes[uiIdx][ij] );
				}
				for ( unsigned int uik = 0; uik < vecTemp_1.size(); ++uik )
				{
					vecPancakes[uiIdx][uik] = vecTemp_1[uik];
				}
			}
			else if ( !vecPancakes[uiIdx][ii] && vecPancakes[uiIdx][0] )
			{
				for ( int il = ii; il >= 0; --il )
				{	
					vector<bool> vecTemp_2;
					if (vecPancakes[uiIdx][il])
					{
						uiFlip++;
						for ( int im = il; im >= 0; --im)
						{
							vecTemp_2.push_back( !vecPancakes[uiIdx][im]);
						}
						for (unsigned int uik = 0; uik < vecTemp_2.size(); ++uik)
						{
							vecPancakes[uiIdx][uik] = vecTemp_2[uik];
						}
						break;
					}
				}
				ii++; // repeat for ii, now vecPancakes[uiIdx][0] wil be false
			}
		}
		vecResults.push_back(uiFlip);
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << vecResults[ uiIdx ] << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

