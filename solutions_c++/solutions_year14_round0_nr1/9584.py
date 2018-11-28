//#include "stdafx.h"
#include <iostream>
#include <fstream>
//#include <ofstream>
//#include <ifstream>
using namespace std;

class FileIO
{
private:
	ifstream m_inputFile;
	ofstream m_outputFile;
public:
	bool openInputFile(const char* inputFileName);
	bool openOutputFile(const char* outputFileName);
	void getNumOfTestCases(int* numTestCase);
	void getCardRow(int* row);
	void initGrid(int grid[4][4]);
	void outputToFile(const char *outputString);
	void outputToFile(int value);

	
};