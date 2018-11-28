#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
using namespace std;
const double INF = 1e12;

int main()
{
    int T;
    double C, F, X;
    cin>>T;
    
    for(int tt = 1; tt <= T; ++tt)
    {
        cin>>C>>F>>X;
        double speed = 2.0;
        double ans = X / speed;
        double currentCost = 0.0;
        while(currentCost < ans)
        {
            double DayReachC = C / speed;
            speed += F;
            currentCost += DayReachC;
            if(ans > currentCost + X / speed)
                ans = currentCost + X / speed;
        }

        cout<<"Case #"<<tt<<": "<<fixed<<setprecision(8)<<ans<<endl;
    }

    return 0;
}
