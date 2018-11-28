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

class matrix {
public:
	int nRows, nCols;
	int **ppRows;
	matrix(int rows = 0, int cols = 0) {
		nRows = 0;
		nCols = 0;
		ppRows = NULL;
	}
	void set(int rows, int cols) {
		nRows = rows;
		nCols = cols;
		ppRows = new int* [nRows];
		for (int i = 0; i < nRows; i++) {
			ppRows[i] = new int [nCols];
		}
		for (int i = 0; i < nRows; i++) {
			for (int j = 0; j < nCols; j++) {
				ppRows[i][j] = 0;
			}
		}
	}
	int getVal(int row, int col) {
		return ppRows[row][col];
	}
	void setVal(int row, int col, int val) {
		ppRows[row][col] = val;
	}
	~matrix() {
		if (ppRows != NULL) {
			for (int i = 0; i < nRows; i++) {
				delete [] ppRows[i];
			}
			delete [] ppRows;
		}
	}
};

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
	matrix* pMatrix = new matrix[nCases];
	string* pstrOutput = new string [nCases];

	// Read input
	string sRows, sCols;
	int nRows, nCols;
	int strlen;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		sLine = "";

		if (fInput.good()) { getline(fInput, sLine); }

		if (sLine == "") { continue; }

		strlen = sLine.length();

		nRows = 0;
		nCols = 0;
		sRows = "";
		sCols = "";

		for (int i = 0; i < strlen; i++) {
			if (nRows == 0) {
				if (sLine[i] != ' ') {
					sRows += sLine[i];
				}
				else {
					nRows = atoi(sRows.c_str());
				}
			}
			else {
				sCols += sLine[i];
			}
		}
		nCols = atoi(sCols.c_str());

		pMatrix[nCase-1].set(nRows, nCols);

		for (int i = 0; i < nRows; i++) {
			getline(fInput, sLine);

			string* pstrLine = new string [nCols];
			string strWord;
			int nCol = 0;
			strlen = sLine.length();

			for (int j = 0; j < strlen; j++) {
				if (sLine[j] == ' ') {
					pstrLine[nCol++] = strWord;
					strWord = "";
				}
				else {
					strWord += sLine[j];
				}
			}
			pstrLine[nCol++] = strWord;

			for (int c = 0; c < nCols; c++) {
				pMatrix[nCase-1].setVal(i, c, atoi(pstrLine[c].c_str()));
			}

			delete [] pstrLine;
		}
	}
	//////////////////////////////////////////////////////////////////////////

	// Solve problem
	bool bPossible = true;
	for (int nCase = 1; nCase <= nCases; nCase++) {
		bPossible = true;
		// Check rows
		int nMinHeight = -1;
		int nMinHeightCol = 0;
		for (int i = 0; i < pMatrix[nCase-1].nRows; i++) {
			bPossible = true;
			nMinHeight = -1;
			nMinHeightCol = 0;
			for (int j = 0; j < pMatrix[nCase-1].nCols; j++) {
				if (nMinHeight == -1) {
					nMinHeight = pMatrix[nCase-1].getVal(i, j);
					nMinHeightCol = j;
				}
				else if (pMatrix[nCase-1].getVal(i, j) < nMinHeight) {
					nMinHeight = pMatrix[nCase-1].getVal(i, j);
					nMinHeightCol = j;
				}
			}
			bool bRowOK = true;
			bool bColumnOK = true;
			// Either Row has all min height values
			for (int j = 0; j < pMatrix[nCase-1].nCols; j++) {
				if (pMatrix[nCase-1].getVal(i, j) != nMinHeight) {
					bRowOK = false;
					break;
				}
			}
			// or all columns having the min height values must be checked
			for (int j = 0; j < pMatrix[nCase-1].nCols; j++) {
				if (pMatrix[nCase-1].getVal(i, j) == nMinHeight) {
					for (int x = 0; x < pMatrix[nCase-1].nRows; x++) {
						if (pMatrix[nCase-1].getVal(x, j) != nMinHeight) {
							bColumnOK = false;
							break;
						}
					}
				}
			}
			// Final check
			if (bRowOK || bColumnOK) {
				continue;
			}
			else {
				bPossible = false;
				break;
			}
		}

		if (bPossible == true) {
			pstrOutput[nCase-1] = "YES";
		}
		else {
			pstrOutput[nCase-1] = "NO";
		}
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
	delete [] pMatrix;
	//////////////////////////////////////////////////////////////////////////

	return 0;
}