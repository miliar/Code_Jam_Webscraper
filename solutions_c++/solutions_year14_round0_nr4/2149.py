#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

//#define TRY
//#define SMALL
#define LARGE

int myCompare(const void* x, const void* y);

int main() {

#ifdef TRY
    const char* inFilename = "try.in";
    const char* outFilename = "try.out";
#endif
#ifdef SMALL
    const char* inFilename = "D-small-attempt0.in";
    const char* outFilename = "D-small-attempt0.out";
#else
    #ifdef LARGE
        const char* inFilename = "D-large.in";
        const char* outFilename = "D-large.out";
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

        int N;
        inFileStream >> N;

        double* naomiBlocks = new double[N];
        double* kenBlocks = new double[N];

        for (int iCtr = 0; iCtr < N; ++iCtr) {
            inFileStream >> naomiBlocks[iCtr];
        }

        for (int iCtr = 0; iCtr < N; ++iCtr) {
            inFileStream >> kenBlocks[iCtr];
        }

        int numWin4Naomi = 0;
        int numDeceitWarWin4Naomi = 0;

        // Fair war win for naomi calculation
        qsort(naomiBlocks, N, sizeof(double), &myCompare);
        qsort(kenBlocks, N, sizeof(double), &myCompare);

        int startIndex = 0;
        int endIndex = N - 1;
        for (int iCtr = 0; iCtr < N; ++iCtr) {
            if (naomiBlocks[iCtr] > kenBlocks[startIndex]) {
                --endIndex;
                ++numWin4Naomi;
            } else {
                ++startIndex;
            }
        }

        // Deceit War win for naomi calculations
        startIndex = N - 1;
        endIndex = 0;
        for (int iCtr = N - 1; iCtr >= 0; --iCtr) {
            if (naomiBlocks[iCtr] > kenBlocks[startIndex]) {
                --startIndex;
                ++numDeceitWarWin4Naomi;
            } else {
                ++endIndex;
            }
        }

        outFileStream << "Case #" << iTestCase << ": " << numDeceitWarWin4Naomi << " " << numWin4Naomi << endl;

        delete[] naomiBlocks;
        delete[] kenBlocks;
    }

    inFileStream.close();
    outFileStream.close();

	return 0;
}

int myCompare(const void* x, const void* y) {

    if (*(double*)x > *(double*)y) {
        return -1;
    } else if (*(double*)x < *(double*)y) {
        return 1;
    } else {
        return 0;
    }
}
