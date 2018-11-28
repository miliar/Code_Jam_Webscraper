#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>

using namespace std;

//#define TRY
#define SMALL
//#define LARGE

unsigned long compute(unsigned long A, unsigned long B, unsigned long K) {

    unsigned long result = 0;

    for (unsigned long iA = 0; iA < A; ++iA) {
        for (unsigned long iB = 0; iB < B; ++iB) {

            unsigned long val = iA & iB;
            if (val >= 0 && val < K) {
                ++result;
            }
        }
    }

    return result;
}

int main() {

#ifdef TRY
    const char* inFilename = "try.in";
    const char* outFilename = "try.out";
#endif
#ifdef SMALL
    const char* inFilename = "B-small-attempt0.in";
    const char* outFilename = "B-small-attempt.out";
#else
    #ifdef LARGE
        const char* inFilename = "A-large.in";
        const char* outFilename = "A-large.out";
    #endif
#endif

    ifstream inFileStream;
    inFileStream.open(inFilename, ios::in);
    if( !inFileStream.is_open() ) {
        cout << "Unable to open input file" << endl;
        return 1;
    }

    ofstream outFileStream;
    outFileStream.open(outFilename, ios::out);
    if( !outFileStream.is_open() ) {
        cout << "Unable to open output file" << endl;
        inFileStream.close();
        return 1;
    }


    int numTestCases;
    inFileStream >> numTestCases;
  
    for (int iTestCase = 1; iTestCase <= numTestCases; ++iTestCase) {

        unsigned long A, B, K;
        inFileStream >> A >> B >> K;

        outFileStream << "Case #" << iTestCase << ": " << compute(A, B, K) << endl;
    }

    inFileStream.close();
    outFileStream.close();

	return 0;
}
