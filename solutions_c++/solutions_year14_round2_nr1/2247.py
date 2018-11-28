#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
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
        unsigned int N;
        inStream >> N;

        vector<string> strings;
        for(unsigned int i = 0 ; i < N ; i++)
        {
            inStream >> line;
            strings.push_back(line);
        }

        unsigned int result = 0;
        bool impossible = false;
        while(true)
        {
            if(strings.at(0).size() == 0)
            {
                for(unsigned int i = 1 ; i < N ; i++)
                {
                    if(strings.at(i).size() != 0)
                    {
                        impossible = true;
                        break;
                    }
                }

                break;
            }

            char currentLetter = strings.at(0).at(0);
            unsigned int totalRepeat = 0, nbRepeat = 0;
            for(unsigned int i = 0 ; i < N ; i++)
            {
                nbRepeat = 0;
                for(unsigned int j = 0 ; j < strings.at(i).size() ; j++)
                {
                    if(strings.at(i).at(j) == currentLetter)
                        nbRepeat++;
                    else
                        break;
                }

                if(nbRepeat == 0)
                {
                    impossible = true;
                    break;
                }

                totalRepeat += nbRepeat;
            }

            if(impossible)
                break;

            double meanRepeat = static_cast<double>(totalRepeat)/N;
            unsigned int chosenRepeat = floor(meanRepeat+0.5);

            for(unsigned int i = 0 ; i < N ; i++)
            {
                nbRepeat = 0;
                for(unsigned int j = 0 ; j < strings.at(i).size() ; j++)
                {
                    if(strings.at(i).at(j) == currentLetter)
                        nbRepeat++;
                    else
                        break;
                }

                strings.at(i) = strings.at(i).substr(nbRepeat);
                result += abs(static_cast<int>(chosenRepeat) - static_cast<int>(nbRepeat));
            }
        }

        // Output the test case result
        outStream << "Case #" << t << ": ";
        if(impossible)
            outStream << "Fegla Won";
        else
            outStream << result;

        if(t != T)
            outStream << endl;
    }

    // Close input and output files
    outStream.close();
    inStream.close();

    // Exit the program
    return 0;
}
