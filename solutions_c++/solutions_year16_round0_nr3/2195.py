//	main: load input, run tasks, write output

#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <assert.h>

#include "QC.h"

using namespace std;

///////////////////////////////////////////////////////////

class CInParser {
public:
	explicit CInParser( const std::string& fileName );

	int ReadLineAsInt();
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
//const string inFileName = "./../in/C-small-attempt0.in";
//const string outFileName = "./../out/C-small-attempt0.out";
const string inFileName = "./../in/C-large.in";
const string outFileName = "./../out/C-large.out";


///////////////////////////////////////////////////////////

CInParser::CInParser( const string& fileName )
{
	inFile.open( fileName.c_str() );
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

void parseInFile( CInParser& parser, int& N, int& J )
{
	vector<int> ints;
	parser.ReadLineAsIntsVector( ints );
	N = ints[0];
	J = ints[1];
	assert( N > 0 && J > 0 );
}

void writeOutput( std::ofstream& outFile, const std::string& jamcoin, const vector<int>& divisors )
{
	assert( divisors.size() == 9 );
	outFile << jamcoin;
	for( int i = 0; i < (int)divisors.size(); i++ ) {
		outFile << " ";
		outFile << divisors[i];
	}
	outFile << "\n";
}


int main(int argc, char* argv[])
{
	//	parse input
	CInParser parser( inFileName );
	const int numberOfSets = parser.ReadLineAsInt();
	assert( numberOfSets > 0 );

	std::ofstream outFile( outFileName.c_str() );

	CQCTaskProcessor taskProcessor;

	for( int setN = 1; setN <= numberOfSets; setN++ ) {
		cout << "Processing set #" << setN <<"...\n";

		//	parse in file
		int N = 0;
		int J = 0;
		parseInFile( parser, N, J );

		//	process
		outFile << "Case #" << setN << ":\n";
		vector<int> divisors;
		std::string jamcoin;
		std::set<string> foundCoins;
		for( int j = 0; j < J; j++ ) {
			jamcoin = taskProcessor.findJamcoin( N, foundCoins, divisors );
			foundCoins.insert( jamcoin );
			//	output
			writeOutput( outFile, jamcoin, divisors );
		}
	}

	return 0;
}

