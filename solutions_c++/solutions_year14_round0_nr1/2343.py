#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

//#define TRY
#define SMALL
//#define LARGE

int main() {

#ifdef TRY
    const char* inFilename = "try.in";
    const char* outFilename = "try.out";
#endif
#ifdef SMALL
    const char* inFilename = "A-small-attempt0.in";
    const char* outFilename = "A-small-attempt0.out";
#else
    #ifdef LARGE
        const char* inFilename = "large.in";
        const char* outFilename = "large.out";
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

        int firstAnswer;
        inFileStream >> firstAnswer;

        int arr[4][4];

        for (int iRow = 0; iRow < 4; ++iRow) {

            for (int iCol = 0; iCol < 4; ++iCol) {

                inFileStream >> arr[iRow][iCol];
            }
        }

        int secondAnswer;
        inFileStream >> secondAnswer;

        int arr2[4][4];

        for (int iRow = 0; iRow < 4; ++iRow) {

            for (int iCol = 0; iCol < 4; ++iCol) {

                inFileStream >> arr2[iRow][iCol];
            }
        }

        int occurrence = 0;
        int value;
        for (int iFirstArrIndex = 0; iFirstArrIndex < 4; ++iFirstArrIndex) {

            for (int iSecondArrIndex = 0; iSecondArrIndex < 4; ++iSecondArrIndex) {

                if (arr[firstAnswer - 1][iFirstArrIndex] == arr2[secondAnswer - 1][iSecondArrIndex]) {
                    ++occurrence;
                    value = arr[firstAnswer - 1][iFirstArrIndex];
                    break;
                }
            }
        }

        outFileStream << "Case #" << iTestCase << ": ";
        if (occurrence == 0) {
            outFileStream << "Volunteer cheated!" << endl;
        } else if (occurrence > 1) {
            outFileStream << "Bad magician!" << endl;
        } else {
            outFileStream << value << endl;
        }
    }

    inFileStream.close();
    outFileStream.close();

	return 0;
}
