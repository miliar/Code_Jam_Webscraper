#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void nextFarm(int farm, vector<double>& timePerFarmBuilt, double C, double F)
{
    double time = C/(F*farm + 2);
    timePerFarmBuilt.push_back(time + timePerFarmBuilt[farm]);
}

void solve(int testCase, double C, double F, double X, ostream& output)
{
    vector<double> timePerFarmBuilt(1,0);
    double timeToFinishPrev = X/(2.0);
    int numFarm = 0;
    nextFarm(numFarm, timePerFarmBuilt, C, F);
    numFarm++;
    double timeToFinish = timePerFarmBuilt[numFarm] + X/(F * numFarm +  2.0);

    while(timeToFinish < timeToFinishPrev)
    {
        timeToFinishPrev = timeToFinish;
        nextFarm(numFarm, timePerFarmBuilt, C, F);
        numFarm++;
        timeToFinish = timePerFarmBuilt[numFarm] + X/(F * numFarm +  2.0);
    }

    double res = timeToFinishPrev;

    output.precision(7);
    output.setf( std::ios::fixed, std:: ios::floatfield );
    output << "Case #"<< testCase <<": " << res << endl;

}

int main()
{
    ifstream file("B-large.in");
    int testCases;
    file >> testCases;
    ofstream output("outputLarge.txt");

    for(int i = 0; i < testCases; i++)
    {
        double C, F, X;
        file >> C >> F >> X;
        solve(i+1, C, F, X, output);
    }
    return 0;
}
