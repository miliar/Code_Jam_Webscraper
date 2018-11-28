#include <iostream>
#include <vector>
#include <string>
#include <fstream>

#include <cstdio>

using namespace std;

double getAnswer(double &farmCost, double &farmRate, double &goal)
{
    double rate = 2;
    double totalTime = 0;

    while (1)
    {
        double saveTime = goal/rate;
        double timeUntilFarm = farmCost/rate;

        if (saveTime < timeUntilFarm)
            return saveTime;

        double rate1 = rate + farmRate;
        //cout << "if " << goal/rate1 << " < " << (goal-farmCost)/rate << endl;
        totalTime += timeUntilFarm;
        //cout << "totalTime is now " << totalTime << endl;
        if (goal/rate1 < (goal-farmCost)/rate)
            rate = rate1;
        else
            return totalTime + (goal-farmCost)/rate;
    }

    return 0;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    int numTests;
    fin >> numTests;

    for (int i = 0; i < numTests; ++i)
    {
        double farmCost, farmRate, goal;
        fin >> farmCost >> farmRate >> goal;

        //cout << farmCost << " " << farmRate << " " << goal << endl;

        //printf(".6%lf .6%lf .6%lf\n", farmCost, farmRate, goal);

        printf("Case #%d: %.6lf\n", i+1, getAnswer(farmCost, farmRate, goal));

        //cout << "Case #"<<i+1<<": " << getAnswer(farmCost, farmRate, goal) << endl;
    }
    return 0;
}