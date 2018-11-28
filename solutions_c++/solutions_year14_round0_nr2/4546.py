#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char** argv)
{
    double farmCost, farmCookieRate, cookieTarget;
    double baseRate = 2.0, curRate;

    double timeElapsed;
    double numCookies;

    int T;

    cin >> T;

    for (int i = 1; i <= T; i++) 
    {
        cin >> farmCost >> farmCookieRate >> cookieTarget;
        
        //cout << "Read: farmCost " << farmCost << ", farm rate " << farmCookieRate << ", target " << cookieTarget << endl;
        
        timeElapsed = 0;
        numCookies = 0;
        curRate = baseRate;
        
        while (numCookies < cookieTarget)
        {
            double timeTillTarget = (cookieTarget - numCookies) / curRate;
            double timeTillFarm = (farmCost - numCookies) / curRate;
            
            //cout << "Cur rate: " << curRate << ", time till farm: " << timeTillFarm << ", time till target: " << timeTillTarget << endl;
            
            if (timeTillFarm < timeTillTarget)
            {
                timeElapsed += timeTillFarm;
                numCookies += timeTillFarm * curRate;
                
                // Should we buy a farm?
                double timeWithNewFarm = (cookieTarget - (numCookies - farmCost)) / (curRate + farmCookieRate);
                double timeWithoutFarm = (cookieTarget - numCookies) / curRate;
                
                if (timeWithNewFarm < timeWithoutFarm)
                {
                    numCookies -= farmCost;
                    curRate += farmCookieRate;
                }
                else
                {
                    timeElapsed += timeWithoutFarm;
                    break;
                }
            }
            else
            {
                timeElapsed += timeTillTarget;
                break;
            }
        }
        
        cout << "Case #" << i << ": " << fixed << setprecision(7) << timeElapsed << endl;
    }
}