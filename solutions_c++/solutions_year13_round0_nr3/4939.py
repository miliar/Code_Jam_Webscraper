// GoogleTest.cpp : Defines the entry point for the console application.
//

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

class FairAndSquare {
public:
	int nLowerLimit;
	int nUpperLimit;
};

bool isFair(int nVal)
{
	stringstream out;
	out << nVal;
	string sVal = out.str();
	int nLen = sVal.length();
	if (nLen == 1) { return true; }
	int nHalfLen = nLen/2;
	for (int i = 0; i < nHalfLen; i++) {
		if (sVal[i] != sVal[nLen-i-1]) {
			return false;
		}
	}
	return true;
}

bool isSquare(int nVal)
{
	if (nVal <= 0) { return false; }
	int sq = (int) sqrt((double) nVal);
	return (nVal == sq * sq);
}

bool isSquareAndFair(int nVal)
{
	if (nVal <= 0) { return false; }
	int sq = (int) sqrt((double) nVal);
	if (nVal != sq * sq) { return false; }
	if (isFair(nVal) == false) { return false; }
	if (isFair(sq) == false) { return false; }
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//////////////////////////////////////////////////////////////////////////
	// Check input
	if (argc <= 1) { return 1; }

	// Get input file path
	string sPath = argv[1];

	// Variable to store number of cases
	int nCases = 0;

	// Read file
	string sLine;
	ifstream fInput(sPath);

	// Validate file
	if (!fInput.is_open()) { return 1; }

	// Read number of cases
	if (fInput.good()) {
		getline(fInput, sLine);
		stringstream(sLine) >> nCases;
	}

	// Validate input before dynamic allocation
	if (nCases < 1) { return 1; }

	// Declare array for input and output
	FairAndSquare* pFairAndSquareArr = new FairAndSquare[nCases];
	string* pstrOutput = new string [nCases];

	// Read input
	int nLowerLimit, nUpperLimit;
	string sTmp;
	int strlen;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		sLine = "";

		if (fInput.good()) { getline(fInput, sLine); }

		if (sLine == "") { continue; }

		strlen = sLine.length();

		nLowerLimit = -1;
		nUpperLimit = -1;
		sTmp = "";

		for (int i = 0; i < strlen; i++) {
			if (nLowerLimit == -1) {
				if (sLine[i] != ' ') {
					sTmp += sLine[i];
				}
				else {
					nLowerLimit = atoi(sTmp.c_str());
					sTmp = "";
				}
			}
			else {
				sTmp += sLine[i];
			}
		}
		nUpperLimit = atoi(sTmp.c_str());

		pFairAndSquareArr[nCase-1].nLowerLimit = nLowerLimit;
		pFairAndSquareArr[nCase-1].nUpperLimit = nUpperLimit;
	}
	//////////////////////////////////////////////////////////////////////////

	// Solve problem
	int nCounter = 0;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		nCounter = 0;
		nLowerLimit = pFairAndSquareArr[nCase-1].nLowerLimit;
		nUpperLimit = pFairAndSquareArr[nCase-1].nUpperLimit;
		for (int nVal = nLowerLimit; nVal <= nUpperLimit; nVal++) {
			if (isSquareAndFair(nVal) == true) {
				nCounter++;
			}
		}
		stringstream out;
		out << nCounter;
		pstrOutput[nCase-1] = out.str();
	}

	//for (int nCase = 1; nCase <= nCases; nCase++) {
	//	stringstream outRows, outCols;
	//	outRows << pMatrix[nCase-1].nRows;
	//	pstrOutput[nCase-1] += outRows.str() + " ";
	//	outCols << pMatrix[nCase-1].nCols;
	//	pstrOutput[nCase-1] += outCols.str() + "\n";
	//	for (int i = 0; i < pMatrix[nCase-1].nRows; i++) {
	//		for (int j = 0; j < pMatrix[nCase-1].nCols; j++) {
	//			stringstream out;
	//			out << pMatrix[nCase-1].ppRows[i][j];
	//			pstrOutput[nCase-1] += out.str() + " ";
	//		}
	//		pstrOutput[nCase-1] += "\n";
	//	}
	//}

	//////////////////////////////////////////////////////////////////////////
	// File output
	ofstream fOutput;
	fOutput.open(sPath+".out", ios::out|ios::trunc);
	for (int nCase = 1; nCase <= nCases; nCase++) {
		fOutput << "Case #" << nCase << ": " << pstrOutput[nCase-1] << "\n";
	}
	fOutput.close();

	// Release memory
	delete [] pFairAndSquareArr;
	//////////////////////////////////////////////////////////////////////////

	return 0;
}