#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main ()
{
    int testCases;
    double seconds;
    double cps;
    double farmWorth;
    double farmCost;
    double winCount;
    
    
    cin >> testCases;
    cout << std::fixed;
    
    for (int k = 0; k < testCases; k++)
    {
        seconds = 0;
        cps = 2;
        
        cin >> farmCost >> farmWorth >> winCount;
        
        while (((winCount/(cps + farmWorth)) + (farmCost/cps)) < (winCount/cps))
        {
            seconds = seconds + (farmCost/cps);
            cps = cps + farmWorth;
        }
        
        seconds = seconds + (winCount/cps);
        
        cout << "Case #" << k+1 << ": " << std::setprecision(7) << seconds << endl;
    }
    
    return 0;
}
    