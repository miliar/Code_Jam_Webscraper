#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int tc;
    double C, F, X;
    cin>>tc;
    double eps = 1e-8;
    for(int t=1; t<=tc; t++)
    {
        cin>>C>>F>>X;
        double mn = X/2;
        double rate = 2;
        double ck = 0.0;
        while(1)
        {
            ck += C/rate;
            rate += F;
            if(mn>=(ck+(X/rate)+eps))
                mn = ck+(X/rate)+eps;
            else
                break;
        }
        printf("Case #%d: %.7lf\n", t, mn);
    }
}
