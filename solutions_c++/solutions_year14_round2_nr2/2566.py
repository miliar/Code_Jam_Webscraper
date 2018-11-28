#include <fstream>
#include <iostream>

using namespace std;


int main()
{
    ifstream inFile ("B-small-attempt0.in");
    ofstream outFile("B-small-attempt0.out");

    int      cases;
    int      oldLim;
    int      newLim;
    int      selLim;
    int      winningNums;

    if (inFile.is_open() && outFile.is_open())
    {
        inFile >> cases;

        for (int c = 0; c < cases; c++)
        {
            inFile >> oldLim;
            inFile >> newLim;
            inFile >> selLim;

            winningNums = 0;

            for (int o = 0; o < oldLim; o++)
            {
                for (int n = 0; n < newLim; n++)
                {
                    int onBitwise = o & n;

                    if (onBitwise < selLim)
                        winningNums++;
                }
            }

            outFile << "Case #" << c + 1 << ": " << winningNums << endl;
        }
    }
    else
        cerr << "Cannot open files." << endl;

    inFile.close();
    outFile.close();

    return 0;
}

