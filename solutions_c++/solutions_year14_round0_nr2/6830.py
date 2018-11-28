#include<stdio.h>
#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
    int tests,t;
    double c,f,x,rate,time;
    cin>>tests;
    for(t=1;t<=tests;t++)
    {
        rate = 2.0 , time = 0.0;
        cin >> c >> f >> x ;
        while(c/rate + x/(rate+f) < x/rate)
        {
            time = time + c/rate;
            rate = rate + f;
        }
        time = time + x/rate;

        cout<<"Case #"<<t<<": ";
        printf("%.7lf\n",time);
    }
    return 0;
}
