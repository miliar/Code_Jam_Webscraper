#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;

    for(int idx = 0 ; nTest > idx ; idx++){
	string cu;
	int result = 0;

	inFile >> cu;

	char tok    = cu[0];

	for(int ci = 1 ; cu.size() > ci ; ci++){
	    if(tok != cu[ci]){
		tok = cu[ci];
		result++;
	    }

	}

	if('-' == cu[cu.size()-1]){
	    result++;
	}

	outFile << "Case #" << idx+1 << ": " << result << endl;

	cu.clear();
    }
}
