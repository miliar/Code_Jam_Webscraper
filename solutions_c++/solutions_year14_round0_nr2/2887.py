// https://code.google.com/codejam/contest/2974486/dashboard#s=p1
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int numTests;
    cin >> numTests;
    for (int test = 0; test < numTests; ++test)
    {
        double farmCost, farmBoost, goal;
        cin >> farmCost >> farmBoost >> goal;

        double rate = 2;
        double best = goal / 2;
        double farmSeconds = 0;

        while (true)
        {
            // build another farm
            farmSeconds += farmCost / rate;
            rate += farmBoost;
            double timeToGoal = farmSeconds + (goal / rate);
            if (timeToGoal < best) {
                best = timeToGoal;
            }
            else {
                break;
            }
        }
        cout << "Case #" << test + 1 << ": "
             << setprecision(7) << fixed << best << endl;
    }
    return 0;
}
