#include <iostream>
#include <fstream>
#include <Vector>
#include <string>

using namespace std;

int main()
{
    int T;
    string inFileNP("A_s.in"), outFileNP("A_s.out");

    ifstream inFile(inFileNP.c_str());
    ofstream outFile(outFileNP.c_str());

    if(inFile)
    {
        if(outFile)
        {
            // Processing part :D
            inFile >> T;

            for(int theCase(1); theCase<=T; theCase++)
            {
                int firstAnswer;
                inFile >> firstAnswer;

                //Store cards numbers
                int fourPossibilities[4];

                for(int i(1); i<=4; i++)
                {
                    for(int j(0); j<4; j++)
                    {
                        int cardVal1;
                        inFile >> cardVal1;
                        if(i==firstAnswer)
                        {
                            fourPossibilities[j]=cardVal1;
                        }
                    }
                }

                //read second answer
                int secondAnswer;
                inFile >> secondAnswer;

                //
                vector< vector<int> > cardRow(4);

                for(int i(0); i<4; i++)
                    for(int j(0); j<4; j++)
                    {
                        int cardVal;
                        inFile >> cardVal;

                        for(int k(0); k<4; k++)
                        {
                            if(cardVal==fourPossibilities[k])
                            {
                                cardRow[i].push_back(fourPossibilities[k]);
                                break;
                            }
                        }
                    }

                //print cardRow
                cout << "\ncase: " << theCase << "(" << fourPossibilities[0] << "," << fourPossibilities[1] << "," << fourPossibilities[2] << "," << fourPossibilities[3] << ")" << endl;

                for(int i(0); i<4; i++)
                {
                    for(int j(0); j<cardRow[i].size(); j++)
                    {
                        cout << cardRow[i][j] << " ";
                    }
                    cout << endl;
                }

                //out put
                if(cardRow[secondAnswer-1].size()>=2)
                {
                    outFile << "Case #" << theCase <<": Bad magician!" << endl;
                }
                else
                    if(cardRow[secondAnswer-1].size()<=0)
                    {
                        outFile << "Case #" << theCase <<": Volunteer cheated!" << endl;
                    }
                    else
                    {
                        outFile << "Case #" << theCase <<": " << cardRow[secondAnswer-1][0] << endl;
                    }
            }

            // Closing files
            inFile.close();
            outFile.close();
            // End Processing :) .
        }
        else
        {
            cout << "ERROR: Can not open the outFile: " << outFileNP << endl;
        }
    }
    else
    {
        cout << "Error, The inFile " << inFileNP << " is not found!!" << endl;
    }
}
