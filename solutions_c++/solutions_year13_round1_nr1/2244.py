#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(int argc, char ** argv){

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    long long r;
    long long t;
    long long temp;
    long long now;

    int numberOfTest;

    unsigned long long count;
    unsigned long long count2;
    unsigned long long count3;

    inFile >> numberOfTest;

    for(count = 0 ; numberOfTest > count ; count++){
	inFile >> r;
	inFile >> t;

	temp = t;

	now = r + r + 1;

	temp	= t - now;
	for(count2 = 0 ; 0 <= temp ; count2++){

	    now += 4;
	    temp -= now;
	}


	outFile << "Case #" << count + 1 << ": " << count2 << endl;
    }

    inFile.close();
    outFile.close();

    return EXIT_SUCCESS ;
}
