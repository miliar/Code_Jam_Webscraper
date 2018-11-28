#include <iostream>
#include <fstream>
#include <string>
#include <limits>
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
        double C, F, X;
        inStream >> C;
        inStream >> F;
        inStream >> X;

        unsigned int f = 0;
        double s = -1;
        while(true)
        {
            double newS = X / (2 + f*F);
            for(unsigned int i = 0 ; i < f ; i++)
                newS += C / (2 + i*F);

            if(s != -1 && newS > s)
                break;

            s = newS;
            f++;
        }

        // Output the test case result
        outStream.precision(numeric_limits<double>::digits10);
        outStream << "Case #" << t << ": " << fixed << s;
        if(t != T)
            outStream << endl;
    }

    // Close input and output files
    outStream.close();
    inStream.close();

    // Exit the program
    return 0;
}
