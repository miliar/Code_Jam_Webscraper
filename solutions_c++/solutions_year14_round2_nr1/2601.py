#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string.h>
using namespace std;

//#define DEBUG

#ifdef DEBUG
#define DEBUG_PRINT(...) fprintf (stderr, __VA_ARGS__)
#else
#define DEBUG_PRINT(...)
#endif

int countChars(string& str, int start) {
	
	const char myChar = str[start];
	
	for(int pos = start; pos < str.length(); pos++) {
		if (myChar != str[pos]) {
			return pos - start;
		}		
	}
	
	return str.length() - start;	
}


int main(int argc, char **argv)
{
	DEBUG_PRINT("Open file %s\n", argv[1]);
	
	ifstream InputFile (argv[1]);
	
	int NbTestCases = 0;
	
	if (!InputFile.is_open()) {
		cerr << "Could not open " << argv[1] << endl;
		return 1;
	}
	
	InputFile >> NbTestCases;
	
	DEBUG_PRINT("NbTestCases = %d\n", NbTestCases);
	
	for (int CurTestCase = 0; CurTestCase < NbTestCases; CurTestCase++) {
		
		int strIdx = 0;
		int pos = 0;
		int NbStrings = 0;
		
		int NbMoves = 0;
		
		
		InputFile >> NbStrings;			
		
		DEBUG_PRINT("\n\nTest Case %d\n", CurTestCase+1);

		string *pStrings = NULL;
		
		pStrings = new string[NbStrings];
		
		for (strIdx = 0; strIdx< NbStrings; strIdx++) {
			
			InputFile >> pStrings[strIdx];
			
			DEBUG_PRINT("str[%d] = %s\n", strIdx, pStrings[strIdx].c_str());
		}
	

		int curPos[NbStrings];
		memset(curPos, 0, sizeof(int) * NbStrings);

		while(true) {
			
			int curCountTotal = 0;			
			int curCounts[NbStrings];
						
			int curMean = 0;
			char curChar = pStrings[0][curPos[0]];
			bool Impossible = false;
			
			// check if we should stop
			
			if (curPos[0] == (pStrings[0]).length()) {
				
				for (strIdx = 0; strIdx < NbStrings; strIdx++) {
					if (curPos[strIdx] != pStrings[strIdx].length()) {
						break;
					}
				}
				
				if (strIdx < NbStrings) {
					cout << "Case #" << CurTestCase+1 << ": Fegla Won" << endl;					
				} else {
					cout << "Case #" << CurTestCase+1 << ": " << NbMoves << endl;
				
				}
				break;				
			}
			
			// get next characters
			
			for (strIdx = 0; strIdx < NbStrings; strIdx++) {		
				
				if (pStrings[strIdx][curPos[strIdx]] != curChar) {
					Impossible = true;
					break;
				}
			
				curCounts[strIdx] = countChars(pStrings[strIdx], curPos[strIdx]);
				curCountTotal += curCounts[strIdx];
				
				curPos[strIdx] += curCounts[strIdx];
				
				DEBUG_PRINT("str[%d][%d] = %d\n", strIdx, curPos[strIdx], curCounts[strIdx]);				
			}
			
			if (Impossible) {
				cout << "Case #" << CurTestCase+1 << ": Fegla Won" << endl;
				break;
			}
			
			curMean = round( (double) curCountTotal / (double) NbStrings);
			
			DEBUG_PRINT("curMean = %d\n", curMean);
			
			for (strIdx = 0; strIdx < NbStrings; strIdx++) {		
				
				if (curCounts[strIdx] > curMean) {
					NbMoves += (curCounts[strIdx] - curMean);
					DEBUG_PRINT("str[%d][%d] -> moves = %d\n", strIdx, curPos[strIdx], curCounts[strIdx] - curMean);								
				} else if (curCounts[strIdx] < curMean) {
					NbMoves += (curMean - curCounts[strIdx]);
					DEBUG_PRINT("str[%d][%d] -> moves = %d\n", strIdx, curPos[strIdx], curMean - curCounts[strIdx]);													
				}
			}
			
		}
		

	}
	
	return 0;
}

