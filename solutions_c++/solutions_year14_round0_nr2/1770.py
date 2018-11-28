#include <iostream>
#include <iomanip>
#define factor 7 

using namespace std;

int main()
{
    double x,c,f, result;
    int casenum = 1;
    int numcases;
    int bestFarms;
    double bestTime;
    double time;
    cin >> numcases;
    while (numcases--)
    {
        cin >> c; //Cost of a farm.
        cin >> f; //Farm production rate.
        cin >> x; //Goal.
       
        int farms = 0;
        double cps = 2;
        bestTime = 999999999;
        for (farms = 0; farms < 100000; farms++)
        {
            cps = 2;
            time = 0;
            for (int j = 0; j < farms; j++)
            {
                time+= (c/cps);
                cps = cps + f;
            }
            time+=(x / cps);

            if (time <= bestTime)
            {
                bestFarms = farms;
                bestTime = time;
            } else {
                break; //Hit the apex.
            }
        }
        cout << "Case #" << casenum++ << ": " << fixed << setprecision(7) << bestTime << endl;
    }
}
