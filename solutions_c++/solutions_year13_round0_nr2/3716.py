#include <iostream>
#include <fstream>
#define M 105

using namespace std;

int nums, dat[M][M];

int main(int argc, char **argv) {
	ifstream inFile;
	ofstream outFile;
	
	inFile.open("input.in");
	outFile.open("output.out");

	inFile >> nums;
	for( int i = 1 ; i <= nums ; ++i ) {
		int he, wi;
		
		inFile >> he >> wi;
		for ( int j = 0 ; j < he ; ++j) {
			for ( int k = 0 ; k < wi ; ++k) {
				inFile >> dat[j][k];
			}
		}

		for( int j = 0 ; j < he ; ++j ) {
			for ( int k = 0 ; k < wi ; ++k ) {
				int l, nn = dat[j][k];

				for ( l = 0 ; l < he ; ++l) {
					if ( nn < dat[l][k] ) break;
				}
				if ( l == he ) continue;
				
				for ( l = 0 ; l < wi ; ++l) {
					if ( nn < dat[j][l] ) break;
				}
				if ( l == wi ) continue;

				goto FAIL;
			}
		}
		outFile << "Case #" << i << ": YES" << endl;
		continue;
FAIL:
		outFile << "Case #" << i << ": NO" << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}