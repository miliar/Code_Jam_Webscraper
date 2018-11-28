#include <iostream>
#include <fstream>
#include <string>
#include <set>
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
        // Read input
        unsigned int N;
        inStream >> N;

        set<double> naomi, ken;
        set<double> naomiCopy, kenCopy;
        double tmp;
        for(unsigned int i = 0 ; i < N ; i++)
        {
            inStream >> tmp;
            naomiCopy.insert(tmp);
        }
        for(unsigned int i = 0 ; i < N ; i++)
        {
            inStream >> tmp;
            kenCopy.insert(tmp);
        }

        // Solve with cheat
        naomi = naomiCopy;
        ken = kenCopy;
        unsigned int cheattedScore = 0;

        // Two choice : burn our smallest with its best or burn our smallest with its smallest
        set<double>::iterator chosenNaomi1 = naomi.begin();
        while(chosenNaomi1 != naomi.end())
        {
            if(*chosenNaomi1 > *(ken.begin()))
            {   // Choice 2
                cheattedScore++;
                ken.erase(ken.begin());
            }
            else
            {   // Choice 1
                ken.erase(*(ken.rbegin()));
            }

            naomi.erase(chosenNaomi1);
            chosenNaomi1 = naomi.begin();
        }

        // Solve without cheat
        naomi = naomiCopy;
        ken = kenCopy;
        unsigned int realScore = 0;
        for(set<double>::iterator chosenNaomi2 = naomi.begin()
             ; chosenNaomi2 != naomi.end() ; chosenNaomi2++)
        {
            realScore++;

            bool erased = false;
            for(set<double>::iterator chosenKen2 = ken.begin()
                 ; chosenKen2 != ken.end() ; chosenKen2++)
            {
                if(*chosenKen2 > *chosenNaomi2)
                {
                    ken.erase(chosenKen2);
                    erased = true;
                    realScore--;
                    break;
                }
            }

            if(!erased)
                ken.erase(ken.begin());
        }

        // Output the test case result
        outStream << "Case #" << t << ": " << cheattedScore << " " << realScore;
        if(t != T)
            outStream << endl;
    }

    // Close input and output files
    outStream.close();
    inStream.close();

    // Exit the program
    return 0;
}
