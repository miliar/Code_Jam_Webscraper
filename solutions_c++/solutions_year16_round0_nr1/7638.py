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
        unsigned int N;
        inStream >> N;

        if (N == 0) {
            outStream << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }

        unsigned int n;
        bool seen[10] = {false};
        for (n = N ; true ; n += N) {
            unsigned int i = n;
            while (i > 0) {
                seen[i % 10] = true;
                i /= 10;
            }

            for (i = 0 ; i < 10 ; i++) {
                if (!seen[i]) {
                    break;
                }
            }
            if (i == 10) {
                break;
            }
        }

        // Output the test case result
        outStream << "Case #" << t << ": " << n << endl;
    }

    // Close input and output files and leave
    outStream.close();
    inStream.close();
    return 0;
}
