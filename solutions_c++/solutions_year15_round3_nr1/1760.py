//	main: load input, run tasks, write output

#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <assert.h>

#include "R1C_A.h"

using namespace std;

///////////////////////////////////////////////////////////

class CInParser {
public:
	explicit CInParser( const std::string& fileName );

	int ReadLineAsInt();
	__int64 ReadLineAsInt64();
	std::string ReadLineAsString();
	void ReadLineAsIntsVector( std::vector<int>& ints );
	void ReadLineAsIntsVector( std::vector<__int64>& ints );
	void ReadLineAsIntAndString(int& n, std::string& str);

private:
	std::ifstream inFile;
};

///////////////////////////////////////////////////////////

//const string inFileName = "./../in/test.txt";
//const string outFileName = "./../out/test.txt";
const string inFileName = "./../in/A-small-attempt0.in";
const string outFileName = "./../out/A-small-attempt0.out";
//const string inFileName = "./../in/A-large.in";
//const string outFileName = "./../out/A-large.out";

void writeOutput( std::ofstream& outFile, int setN, int result )
{
	outFile << "Case #" << setN << ": " << result << "\n";
}

///////////////////////////////////////////////////////////

CInParser::CInParser( const string& fileName )
{
	inFile.open( fileName.c_str() );
}

__int64 CInParser::ReadLineAsInt64()
{
	std::string line;
	std::getline(inFile, line);
	std::istringstream iss(line);
	__int64 result = 0;
	iss >> result;
	return result;
}

int CInParser::ReadLineAsInt()
{
	std::string line;
	std::getline(inFile, line);
	std::istringstream iss(line);
	int result = 0;
	iss >> result;
	return result;
}

//	N "str"
void CInParser::ReadLineAsIntAndString(int& n, std::string& str)
{
	std::string line;
	std::getline(inFile, line);
	std::istringstream iss(line);
	iss >> n;
	iss >> str;
}

std::string CInParser::ReadLineAsString()
{
	std::string line;
	std::getline(inFile, line);
	return line;
}

void CInParser::ReadLineAsIntsVector( std::vector<int>& ints )
{
	std::string line;
	std::getline(inFile, line);
	std::istringstream iss(line);
	ints.clear();
	int n = 0;
	while(iss >> n) {
		ints.push_back(n);
	}
}

void CInParser::ReadLineAsIntsVector( std::vector<__int64>& ints )
{
	std::string line;
	std::getline(inFile, line);
	std::istringstream iss(line);
	ints.clear();
	__int64 n = 0;
	while(iss >> n) {
		ints.push_back(n);
	}
}

///////////////////////////////////////////////////////////

void parseInFile( CInParser& parser, int& R, int& C, int& W )
{
	std::vector<int> ints;
	parser.ReadLineAsIntsVector( ints );
	assert( ints.size() == 3 );
	R = ints[0];
	C = ints[1];
	W = ints[2];
}

int main(int argc, char* argv[])
{
	//	parse input
	CInParser parser( inFileName );
	const int numberOfSets = parser.ReadLineAsInt();
	assert( numberOfSets > 0 );

	std::ofstream outFile( outFileName.c_str() );

	CR1C_ATaskProcessor taskProcessor;

	for( int setN = 1; setN <= numberOfSets; setN++ ) {
		cout << "Processing set #" << setN <<"...\n";

		//	parse in file
		int R = 0;
		int C = 0;
		int W = 0;
		parseInFile( parser, R, C, W );

		//	process		
		const int result = taskProcessor.findMinimumScore( R, C, W );

		//	output
		writeOutput( outFile, setN, result );
	}

	return 0;
}

