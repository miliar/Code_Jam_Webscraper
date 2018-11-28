// DeceitfulWar.cpp
//

#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <time.h>

using namespace std;

int main()
{
	string sFileName = "D-large";

	ifstream in(sFileName + ".in");

	int i = 0;
	string sLine;

	unsigned int uiT = 0; // test cases

	unsigned int uiN = 0; // N- blocks for each player

	unsigned int uiDigits = 1000000; // 6 digits as 5 digits are maximum in test cases

	vector< vector< unsigned int > > colNaomisBlocksCases;
	vector< vector< unsigned int > > colKensBlocksCases;

	vector< unsigned int > colNumberofBloksForCases;
	
	while (getline(in, sLine))
	{
		if (i == 0)
		{
			// T
			uiT = stoi(sLine);
		}
		else
		{
			if (i % 3 == 1)
			{
				uiN = stoi(sLine);
				colNumberofBloksForCases.push_back( uiN );
			}
			if (i % 3 == 2)
			{
				// Naomi's blocks
				vector< unsigned int > colNaomisBlocks;
				for (unsigned int uiIdx = 0; uiIdx < uiN; ++uiIdx)
				{
					int iPos = sLine.find(" ");
					string s = sLine.substr( 0, iPos );
					sLine.erase(0, iPos + 1);

					unsigned int uiBlockWeight = ( unsigned int )( uiDigits * stold( s ) );

					colNaomisBlocks.push_back( uiBlockWeight );
				}
				sort( colNaomisBlocks.begin(), colNaomisBlocks.end() );
				colNaomisBlocksCases.push_back(colNaomisBlocks);
				colNaomisBlocks.clear();
			}
			if (i % 3 == 0)
			{
				// Ken's blocks
				vector< unsigned int > colKensBlocks;
				for (unsigned int uiIdx = 0; uiIdx < uiN; ++uiIdx)
				{
					int iPos = sLine.find(" ");
					string s = sLine.substr(0, iPos);
					sLine.erase(0, iPos + 1);

					unsigned int uiBlockWeight = (unsigned int)( uiDigits * stold( s ) );

					colKensBlocks.push_back( uiBlockWeight );
				}
				sort( colKensBlocks.begin(), colKensBlocks.end() );
				colKensBlocksCases.push_back(colKensBlocks);
				colKensBlocks.clear();
			}
		}
		++i;
	}

	vector< unsigned int > colNamoisWinDECEITFULWAR;
	vector< unsigned int > colNaomisWinWAR;

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		colNaomisWinWAR.push_back( 0 );
		colNamoisWinDECEITFULWAR.push_back(0);
	}

	vector< vector< unsigned int > > colNaomisBlocksCasesForDeceitFulWar = colNaomisBlocksCases;
	vector< vector< unsigned int > > colKensBlocksCasesForDeceitFulWar = colKensBlocksCases;

	// WAR
	for (unsigned int uiCasesIdx = 0; uiCasesIdx < uiT; ++uiCasesIdx)
	{
		for (unsigned int uiNIdx = 0; uiNIdx < colNumberofBloksForCases[uiCasesIdx]; ++uiNIdx)
		{
			// Naomi always plays lowest block
			unsigned int uiNaomiBlock = colNaomisBlocksCases[ uiCasesIdx ][ 0 ];
			colNaomisBlocksCases[uiCasesIdx].erase(colNaomisBlocksCases[uiCasesIdx].begin());

			bool bKenWon = false;
			for (unsigned int uiVecIdx = 0; uiVecIdx < colKensBlocksCases[uiCasesIdx].size(); ++uiVecIdx)
			{
				if ( uiNaomiBlock < colKensBlocksCases[uiCasesIdx][uiVecIdx] )
				{
					colKensBlocksCases[uiCasesIdx].erase(colKensBlocksCases[uiCasesIdx].begin() + uiVecIdx);
					bKenWon = true;
					break;
				}
			}
			if ( !bKenWon )
			{
				++colNaomisWinWAR[uiCasesIdx];
			}
		}
	}

	// DECEITFUL WAR
	for (unsigned int uiCasesIdx = 0; uiCasesIdx < uiT; ++uiCasesIdx)
	{
		for (unsigned int uiNIdx = 0; uiNIdx < colNumberofBloksForCases[uiCasesIdx]; ++uiNIdx)
		{
			// if Naomi has the lowest block - plays it and says it is a little bit smaller than Ken's highest block
			// ( in that case Ken's removing his highest block ) - Ken wins anyway
			// if Ken has the lowest block - Naomi plays her lowest block and says that it is a little bit higher than Ken's highest card
			// Ken thinking he'll lose anyway plays his lowest block - Naomi wins
			if (colNaomisBlocksCasesForDeceitFulWar[uiCasesIdx][0] < colKensBlocksCasesForDeceitFulWar[uiCasesIdx][0])
			{
				// Ken wins anyway
				colNaomisBlocksCasesForDeceitFulWar[uiCasesIdx].erase(colNaomisBlocksCasesForDeceitFulWar[uiCasesIdx].begin());
				colKensBlocksCasesForDeceitFulWar[uiCasesIdx].erase(colKensBlocksCasesForDeceitFulWar[uiCasesIdx].begin() + colKensBlocksCasesForDeceitFulWar[uiCasesIdx].size() - 1);
			}
			else
			{
				// Naomi wins
				colNaomisBlocksCasesForDeceitFulWar[uiCasesIdx].erase(colNaomisBlocksCasesForDeceitFulWar[uiCasesIdx].begin());
				colKensBlocksCasesForDeceitFulWar[uiCasesIdx].erase(colKensBlocksCasesForDeceitFulWar[uiCasesIdx].begin());
				++colNamoisWinDECEITFULWAR[ uiCasesIdx ];

			}
		}
	}

	// printing to file
	ofstream out;
	out.open(sFileName + ".txt");

	for (unsigned int uiIdx = 0; uiIdx < uiT; ++uiIdx)
	{
		out << "Case #" << uiIdx + 1 << ": " << colNamoisWinDECEITFULWAR[uiIdx] << " " << colNaomisWinWAR[uiIdx] << endl;
	}

	out.close();

	return 0;
}

