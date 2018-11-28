#include<bits/stdc++.h>

using namespace std;

const double eps = 1e-6;
double farm, farm_ratio, goal;



int main()
{

    int cases;
    cin>>cases;
    for(int i = 1; i <= cases; i++)
    {

        cin>>farm>>farm_ratio>>goal;
        bool won = false;
        double rate = 2.0;
        double time = 0;
        double cookies = 0;
        double acum_time = 0;
        double ans = INFINITY;
        while(true)
        {
            double wait_time = goal/rate;
            double farm_time = farm/rate;
            if(wait_time + acum_time > ans)
            {
                break;
            }
            ans = min(ans, acum_time + wait_time);
            acum_time+=farm_time;
            rate +=farm_ratio;
        }

        cout<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<ans<<endl;
    }
}
