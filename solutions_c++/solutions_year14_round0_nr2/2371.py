#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>

using namespace std;

//#define TRY
//#define SMALL
#define LARGE

int main() {

#ifdef TRY
    const char* inFilename = "try.in";
    const char* outFilename = "try.out";
#endif
#ifdef SMALL
    const char* inFilename = "B-small-attempt0.in";
    const char* outFilename = "B-small-attempt0.out";
#else
    #ifdef LARGE
        const char* inFilename = "B-large.in";
        const char* outFilename = "B-large.out";
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

        double C, F, X;

        inFileStream >> C >> F >> X;
        double minTime = X / 2;
        double farmTime = 0.0;
        int i = 0;

        while (1) {

            farmTime += C / (2 + i * F);
            double newTime = X / (2 + (i+1) * F);
            if (minTime > (farmTime + newTime)) {
                minTime = farmTime + newTime;
                ++i;
            } else {
                break;
            }
        }

        outFileStream.setf( std::ios::fixed, std:: ios::floatfield );
        outFileStream << "Case #" << iTestCase << ": " << setprecision(7) << minTime << endl;
    }

    inFileStream.close();
    outFileStream.close();

	return 0;
}
