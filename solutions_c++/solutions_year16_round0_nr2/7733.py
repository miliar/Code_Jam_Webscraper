#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
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
        int l = S.length();

        int c = 0;
        while (true) {
            int i;
            for (i = l - 1 ; i >= 0 ; i--) {
                if (S[i] == '-') {
                    break;
                }
            }
            l = i + 1;
            if (l <= 0) {
                break;
            }

            int nbTurn;
            for (nbTurn = 0 ; nbTurn < l ; nbTurn++) {
                if (S[nbTurn] == '-') {
                    if (nbTurn == 0) {
                        nbTurn = l;
                    }
                    break;
                }
            }

            string S2 = S;
            for (i = 0 ; i < nbTurn ; i++) {
                S[i] = (S2[nbTurn-1-i] == '-' ? '+' : '-');
            }

            c++;
        }

        // Output the test case result
        outStream << "Case #" << t << ": " << c << endl;
    }

    // Close input and output files and leave
    outStream.close();
    inStream.close();
    return 0;
}
