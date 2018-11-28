#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int t,ca;
    double c,f,x,time,rate;
    cin>>t;
    ca=1;
    while(t--)
    {
        rate=2.0;
        time=0;
        cin>>c>>f>>x;
        while(x/rate > (c/rate + x/(rate+f)))
        {
            time += (c/rate);
            rate +=f;
        }
        time += (x/rate);
        printf("Case #%d: %.7lf\n",ca,time);
        ca++;
    }
    return 0;
}
