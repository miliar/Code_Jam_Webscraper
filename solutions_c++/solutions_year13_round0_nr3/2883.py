#include <fstream>
#include <string>

using namespace std;

int main( int argc, char *argv[] )
{
	ifstream inFile(argv[1]);
	ofstream outFile("result.out");
	const unsigned long table[21] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321,
		4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404};
	unsigned caseNum;
	inFile >> caseNum;
	for( unsigned i = 0; i != caseNum; ++i ) {
		unsigned long A, B;
		inFile >> A >> B;
		unsigned result(0);
		for( unsigned j = 0; j != 21; ++j ) {
			if( A <= table[j] && B >= table[j] ) {
				++result;
			}
		}
		outFile << "Case #" << i+1 << ": " << result << endl;
	}

	inFile.close();
	outFile.close();
}