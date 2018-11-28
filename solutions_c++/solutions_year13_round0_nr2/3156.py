#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream inFile(argv[1]);
	ofstream outFile("result.out");
	unsigned caseNum(0);
	inFile >> caseNum;
	for( unsigned i = 0; i != caseNum; ++i ) {
		// get one case
		unsigned N, M;
		inFile >> N >> M;
		vector<vector<unsigned>> lawn;
		vector<unsigned> lawnRow(M, 0);
		lawn.resize(N, lawnRow);
		vector<vector<unsigned>> isLMax(lawn);

		// get row max
		for( unsigned j = 0; j != N; ++j ) {
			for( unsigned k = 0; k != M; ++k ) {
				inFile >> lawn[j][k];
			}
		}
		for( unsigned j = 0; j != N; ++j ) {
			unsigned rowMax(0);
			for( unsigned k = 0; k != M; ++k ) {
				if( lawn[j][k] > rowMax ) {
					rowMax = lawn[j][k];
				}
			}
			for( unsigned k = 0; k != M; ++k ) {
				if( lawn[j][k] == rowMax ) {
					isLMax[j][k] |= 1;
				}
			}
		}
		// get column max
		for( unsigned k = 0; k != M; ++k ) {
			unsigned colMax(0);
			for( unsigned j = 0; j != N; ++j ) {
				if( lawn[j][k] > colMax ) {
					colMax = lawn[j][k];
				}
			}
			for( unsigned j = 0; j != N; ++j ) {
				if( lawn[j][k] == colMax ) {
					isLMax[j][k] |= 1;
				}
			}
		}
		// get result
		unsigned result = 1;
		for( unsigned j = 0; result == 1 && j != N; ++j ) {
			for( unsigned k = 0; result == 1 && k != M; ++k ) {
				result &= isLMax[j][k];
			}
		}
		// output
		outFile << "Case #" << i+1 << ": ";
		if( result == 1 ) {
			outFile << "YES";
		} else {
			outFile << "NO";
		}
		outFile << endl;
	}
	
	inFile.close();
	outFile.close();
}