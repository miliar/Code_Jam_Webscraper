#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t, test;
    double c,f,x, total_time, prev_time, farm_time, extra_time, cookie_rate = 2.0;
    cin>>t;
    for(test=1; test<=t; test++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        cookie_rate = 2.0;
        prev_time = x/cookie_rate;
        farm_time = c/cookie_rate;
        cookie_rate += f;
        extra_time = x/cookie_rate;
        total_time = farm_time + extra_time;
        //cout<<prev_time<< " "<<total_time<<endl;
        while(total_time <= prev_time)
        {
            prev_time = total_time;
            farm_time = c/cookie_rate;
            cookie_rate += f;
            total_time -= extra_time;
            extra_time = x/cookie_rate;
            total_time += farm_time + extra_time;
            //cout<<prev_time<< " "<<total_time<<endl;
        }
        printf("Case #%d: %.7lf\n", test, prev_time);

    }
    return 0;
}
