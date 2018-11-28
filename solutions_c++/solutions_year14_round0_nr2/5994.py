#include <iostream>
#include <iomanip>
#include <fstream>
#include <limits>

using namespace std;

double timeToWin(double farmCost, double farmRate, double numOfFarms, double winCost)
{
    double farmCollectionTime = 0.0d;
    double fullRate = winCost / (2.0d + numOfFarms * farmRate);
    numOfFarms--;
    while (numOfFarms >= 0.0d)
    {
        farmCollectionTime += (farmCost / (2.0d + numOfFarms * farmRate));
        numOfFarms--;
    }
    //cout << "Full Rate Time Cost: " << fullRate << endl;
    //cout << "Farm Collected Time: " << farmCollectionTime << endl;
    return (farmCollectionTime + fullRate);
}

int main(int argc, char** argv)
{
    int testCases, secondsUsed;
    double farmPrice, farmRate, cookiesToWin;
    string line;
    ifstream file(argv[1]);
    if (file.is_open())
    {
        file >> testCases;
        cout << fixed << setprecision(7);// << testCases << endl;
        /*cout << timeToWin(500.0, 4.0, 0, 2000.0) << endl;
        cout << timeToWin(500.0, 4.0, 1, 2000.0) << endl;
        cout << timeToWin(500.0, 4.0, 2, 2000.0) << endl;
        cout << timeToWin(500.0, 4.0, 3, 2000.0) << endl;
        cout << timeToWin(500.0, 4.0, 4, 2000.0) << endl;
        cout << timeToWin(500.0, 4.0, 5, 2000.0) << endl;*/
        for(int testCaseCount = 1; testCaseCount <= testCases; testCaseCount++)
        {
            file >> farmPrice >> farmRate >> cookiesToWin;
            //cout << farmPrice << " " << farmRate << " " << cookiesToWin << " " << endl;
           
            double prevResult = numeric_limits<double>::max();
            double farmCounter = 0;
            double result = timeToWin(farmPrice, farmRate, farmCounter, cookiesToWin);
            //cout << "First Result: " << result << endl;
            while (prevResult > result)
            {
                prevResult = result;
                farmCounter++;
                result = timeToWin(farmPrice, farmRate, farmCounter, cookiesToWin);
                if (prevResult < result)
                {
                    result = prevResult;
                    break;
                }
                //cout << "Previous Result: " << prevResult;
                //cout << "\tCurrent Result: " << result << endl;
            }
            cout << "Case #" << testCaseCount << ": " << result << endl;
        }
    }
    file.close();
    return 0;
}
