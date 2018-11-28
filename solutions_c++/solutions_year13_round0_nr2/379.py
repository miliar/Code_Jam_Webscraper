#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

void getInputFile(int argc, char* argv[], ifstream &inputFile)
{
	if (argc != 2) {
		cerr << "Require one argument (input file); exiting ...\n";
		exit(1);
	}
	string filename = argv[1];
	inputFile.exceptions(ifstream::failbit);
	inputFile.open(filename.c_str());
}

void getOutputFile(int argc, char* argv[], ofstream &outputFile)
{
	string filename = argv[1];
	unsigned dotIndex = filename.find_last_of('.');
	if (dotIndex != string::npos)
		filename.erase(dotIndex);
	filename += ".out";
	outputFile.exceptions(ofstream::failbit);
	outputFile.open(filename.c_str());
}

void processCase(istream& inputFile, ostream& outputFile)
{
	int numRows, numCols;
	inputFile >> numRows >> numCols;
	vector<int> height(numRows * numCols);
	for (int i=0; i<numRows * numCols; ++i)
		inputFile >> height[i];

	vector<int> maxInRow(numRows, 0), maxInCol(numCols, 0);
	for (int row=0; row<numRows; ++row)
		for (int col=0; col<numCols; ++col) {
			maxInRow[row] = max(maxInRow[row], height[row * numCols + col]);
			maxInCol[col] = max(maxInCol[col], height[row * numCols + col]);
		}

	for (int row=0; row<numRows; ++row)
		for (int col=0; col<numCols; ++col) {
			int h = height[row * numCols + col];
			if ((h != maxInRow[row]) && (h != maxInCol[col]))
			{
				outputFile << "NO";
				return;
			}
		}

	outputFile << "YES";
}

int main(int argc, char *argv[])
{
	ifstream inputFile;
	getInputFile(argc, argv, inputFile);
	ofstream outputFile;
	getOutputFile(argc, argv, outputFile);

	int numCases;
	inputFile >> numCases >> ws;
	for (int caseIndex = 0; caseIndex < numCases; ++caseIndex) {
		outputFile << "Case #" << caseIndex+1 << ": ";
		cout << "Case #" << caseIndex+1 << "\n";
		processCase(inputFile, outputFile);
		outputFile << "\n";
	}
}


