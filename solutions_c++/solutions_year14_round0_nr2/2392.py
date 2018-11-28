#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for(int testCase = 1; testCase <= t; ++testCase)
    {
        double cookies = 0.0, rate = 2.0;
        double cost, bonus, goal;
        double minTime = 0;
        
        cin >> cost >> bonus >> goal;
        
        //cout << endl;
        
        if(cost > goal)
        {
            minTime = goal / rate;
        }
        else
        {
            double thisTime = 200000000.0;
            int tfarms = 0;
            
            do
            {
                minTime = thisTime;
                thisTime = 0.0;
                rate = 2.0;
                
                for(int nfarms = 0; nfarms < tfarms; ++nfarms)
                {
                    thisTime += cost / rate;
                    rate += bonus;
                }
                thisTime += goal / rate;
                
                //cout << thisTime << ", ";
                
                ++tfarms;
            }
            while(thisTime < minTime);
        }
        //cout << endl;
        
        cout << "Case #" << testCase << ": ";
        cout << fixed << setprecision(7) << minTime << endl;
    }
    
    return 0;
}
