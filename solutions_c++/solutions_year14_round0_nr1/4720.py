#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//!
//! \brief The main function
//!
int main(int argc, char* argv[])
{
    // Check if valid number of program arguments
    if(argc != 2)
    {
        cerr << "Need only one argument : the input file name" << endl;
        return 0;
    }

    // Compute test name from input inStream name
    string testName = argv[1];
    testName = testName.substr(0, testName.find(".in"));

    // Open (and check) input inStream
    ifstream inStream(testName + ".in");
    if(!inStream.is_open())
    {
        cerr << "The input file \"" << testName << ".in\" does not exist" << endl;
        return 0;
    }

    // Get the number of test cases to process
    unsigned int T = 0;
    inStream >> T;

    // Create a string to get lines and ignore the previous already read one
    string line;
    getline(inStream, line);

    // Open the output file
    ofstream outStream(testName + ".out");

    // Process each test case one by one
    for(unsigned int t = 1 ; t <= T ; t++)
    {
        unsigned int answers[2];
        unsigned int tables[2][4][4];

        // Read test case
        for(unsigned int k = 0 ; k < 2 ; k++)
        {
            inStream >> answers[k];
            for(unsigned int i = 0 ; i < 4 ; i++) {
                for(unsigned int j = 0 ; j < 4 ; j++) {
                    inStream >> tables[k][i][j];
                }
            }
        }

        // Solve
        unsigned int nbMatch = 0, card = 0;
        for(unsigned int i = 0 ; i < 4 ; i++) {
            for(unsigned int j = 0 ; j < 4 ; j++) {
                if(tables[0][answers[0]-1][i] == tables[1][answers[1]-1][j])
                {
                    nbMatch++;
                    card = tables[0][answers[0]-1][i];
                    break;
                }
            }
        }

        // Output the test case result
        outStream << "Case #" << t << ": ";

        switch(nbMatch)
        {
            case 0:
                outStream << "Volunteer cheated!";
                break;

            case 1:
                outStream << card;
                break;

            default:
                outStream << "Bad magician!";
        }

        if(t != T)
            outStream << endl;
    }

    // Close input and output files
    outStream.close();
    inStream.close();

    // Exit the program
    return 0;
}
