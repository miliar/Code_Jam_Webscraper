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
#include <iterator> 

using namespace std;

int main()
{
	unsigned int uiT = 0; // test cases

	string sFileName = "A-large";

	vector <unsigned int > col_uiN; // Ns
	vector<vector<unsigned int >> col_senators;

	vector<vector<string>> col_results;


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

			unsigned int uiNumber = 0;
			fscanf_s(stream, "%d", &uiNumber);
			col_uiN.push_back(uiNumber);

			vector<unsigned int> vec_temp;
			for (unsigned int i = 0; i < uiNumber; ++i)
			{
				unsigned int uisen = 0;
				fscanf_s(stream, "%d", &uisen);
				vec_temp.push_back(uisen);
			}
			col_senators.push_back(vec_temp);
		}

		// closing file
		fclose( stream );
	}
	//--------------------- end - reading from file -----------------------
	
	string sAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
	//--------------------- begin - algorithm ---------------------
	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		unsigned int uiMax = *max_element(col_senators[uiIdx].begin(), col_senators[uiIdx].end());
		vector<string> col_lettersTEMP;
		while (uiMax != 0)
		{ 
			vector<unsigned int>::const_iterator it;
			it = max_element(col_senators[uiIdx].begin(), col_senators[uiIdx].end());
			uiMax = *it;
			unsigned int uiIndex = it - col_senators[uiIdx].begin();

			if (col_uiN[uiIdx] > 2 && uiMax > 1)
			{
				--col_senators[uiIdx][uiIndex];
				char letter = sAlphabet.at(uiIndex % sAlphabet.size());
				string sstrings(1, letter);
				col_lettersTEMP.push_back(sstrings);
			}
			if (col_uiN[uiIdx] == 2 && uiMax > 1)
			{
				if (col_senators[uiIdx][0] != col_senators[uiIdx][1])
				{
					--col_senators[uiIdx][uiIndex];
					char letter = sAlphabet.at(uiIndex % sAlphabet.size());
					string sstrings(1, letter);
					col_lettersTEMP.push_back(sstrings);
				}
				else
				{
					// pairs
					--col_senators[uiIdx][0];
					--col_senators[uiIdx][1];
					char letter = sAlphabet.at(0 % sAlphabet.size());
					string sstrings(1, letter);

					char letter2 = sAlphabet.at(1 % sAlphabet.size());
					string sstrings2(1, letter2);
					sstrings.append(sstrings2);
					col_lettersTEMP.push_back(sstrings);
				}
			}
			if (uiMax == 1)
			{
				unsigned int uiMoreThanZero = 0;
				for(unsigned int uiii = 0; uiii < col_senators[uiIdx].size();++uiii)
				{
					if(col_senators[uiIdx][uiii] > 0)
					{
						++uiMoreThanZero;
					}
				}
				if (uiMoreThanZero % 2 == 0)
				{
					//pairs
					--col_senators[uiIdx][uiIndex];

					vector<unsigned int>::const_iterator it2;
					it2 = max_element(col_senators[uiIdx].begin(), col_senators[uiIdx].end());
					unsigned int uiIndex2 = it2 - col_senators[uiIdx].begin();

					--col_senators[uiIdx][uiIndex2];
					char letter = sAlphabet.at(uiIndex % sAlphabet.size());
					string sstrings(1, letter);

					char letter2 = sAlphabet.at(uiIndex2 % sAlphabet.size());
					string sstrings2(1, letter2);
					sstrings.append(sstrings2);
					col_lettersTEMP.push_back(sstrings);
				}
				else
				{
					--col_senators[uiIdx][uiIndex];
					char letter = sAlphabet.at(uiIndex % sAlphabet.size());
					string sstrings(1, letter);
					col_lettersTEMP.push_back(sstrings);
				}
			}
		}
		col_results.push_back(col_lettersTEMP);
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": ";
		for (unsigned int uiidx2 = 0; uiidx2 < col_results[uiIdx].size(); ++uiidx2)
		{
			out << " " << col_results[uiIdx][uiidx2];
		}
		out << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

