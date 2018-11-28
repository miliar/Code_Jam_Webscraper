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
	void getNumOfTestCases(long long *numTestCase);
	void getInputNumber(long long &inputNum);
	void outputToFile(const char *outputString);
	void outputToFile(unsigned long long value);
	void closeInputFile();
	void closeOutputFile();

	
};