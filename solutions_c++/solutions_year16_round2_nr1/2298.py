#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>
using namespace std;

int main(int argc, char* argv[])
{
    if (argc != 2) { // Check if valid number of program arguments
        cerr << "Need only one argument : the input file name" << endl;
        return 0;
    }
    string testFilename(argv[1]);

    // Open (and check) input inStream
    ifstream inStream(testFilename);
    if (!inStream.is_open()) {
        cerr << "The input file \"" << testFilename << "\" does not exist" << endl;
        return 0;
    }

    // Get the number of test cases to process
    unsigned int T = 0;
    inStream >> T;

    // If needed : create a string to get lines and ignore the previous already read one
    // string line;
    // getline(inStream, line);

    // Open the output file
    ofstream outStream(testFilename.substr(0, testFilename.find(".in")) + ".out");

    // Process each test case one by one
    for (unsigned int t = 1 ; t <= T ; t++) {
        // Read input file & Find solution
        string S;
        inStream >> S;

        map<char, int> mapS;
        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        for (unsigned int i = 0 ; i < alphabet.length() ; i++) {
            mapS[alphabet[i]] = 0;
        }
        for (unsigned int i = 0 ; i < S.length() ; i++) {
            mapS[S[i]]++;
        }

        int numbers[10] = {0};
        string numberTexts[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
        char uIds[3][10] = {
            {'Z', '0', 'W', '0', 'U', '0', 'X', '0', 'G', '0'},
            {'0', 'O', '0', 'H', '0', 'F', '0', 'S', '0', '0'},
            {'0', '0', '0', '0', '0', '0', '0', '0', '0', 'N'}
        };

        // First pass
        for (int p = 0 ; p < 3 ; p++) {
            for (int i = 0 ; i < 10 ; i++) {
                if (uIds[p][i] == '0') {
                    continue;
                }
                while (mapS[uIds[p][i]] != 0) {
                    numbers[i]++;
                    for (unsigned int j = 0 ; j < numberTexts[i].length() ; j++) {
                        mapS[numberTexts[i][j]]--;
                    }
                }
            }
        }

        // Output the test case result
        outStream << "Case #" << t << ": ";
        for (int i = 0 ; i < 10 ; i++) {
            for (int j = 0 ; j < numbers[i] ; j++) {
                outStream << i;
            }
        }
        outStream << endl;
    }

    // Close input and output files and leave
    outStream.close();
    inStream.close();
    return 0;
}
