#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double ifIListen(int farmsNumber, double F, double X)
{
    double timeToReachX;
    timeToReachX = X/(2+farmsNumber*F);
    return timeToReachX;
}

double ifIBuyAnOtherFarm(int farmsNumber, double C, double F, double X)
{
    double timeToReach_C, timeToReach_X, totalTime;
    timeToReach_C = C/(2+farmsNumber*F);
    timeToReach_X = X/(2+(farmsNumber+1)*F);
    totalTime = timeToReach_C + timeToReach_X;

    return totalTime;
}

double timeToReachC(int farmsNumber, double C, double F)
{
    double timeToReach_C;
    timeToReach_C = C/(2+farmsNumber*F);

    return timeToReach_C;
}

int main()
{
    int T;
    string inFileNP("B_l.in"), outFileNP("B_l.out");

    ifstream inFile(inFileNP.c_str());
    ofstream outFile(outFileNP.c_str());

    if(inFile)
    {
        if(outFile)
        {
            // Processing part :D
            inFile >> T;

            for(int caseNum(1); caseNum<=T; caseNum++)
            {
                double C, F, X;
                inFile >> C >> F >> X;

                double timeSpend(0);
                int farmsNumber(0);
                bool xReached(false);

                while(!xReached)
                {
                    double timeListen=ifIListen(farmsNumber,F,X);
                    double timeFarm=ifIBuyAnOtherFarm(farmsNumber,C,F,X);

                    if(timeFarm<timeListen)
                    {
                        timeSpend+=timeToReachC(farmsNumber, C, F);
                        farmsNumber++;
                    }
                    else
                    {
                        timeSpend+=timeListen;
                        xReached=true;
                    }
                }

                //write out put file
                outFile << std::fixed;
                outFile << "Case #" << caseNum << ": " << std::setprecision(7) << timeSpend << endl;
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
