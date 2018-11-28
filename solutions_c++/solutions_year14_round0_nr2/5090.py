#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    cout.precision(10);
    int test,t=1;
    double c,f,x;
    cin>>test;
    while(t<=test)
    {
        double time=0.0,rate=2.0;
        cin>>c>>f>>x;
        while(1)
        {
            if( x/rate < c/rate+ x/(rate+f) )
            {
                time+=x/rate;
                break;
            }
            else
            {
                time+=c/rate;
                rate=rate+f;
            }

        }
        printf("Case #%d: %0.7lf\n",t,time);
        t++;
    }

}
