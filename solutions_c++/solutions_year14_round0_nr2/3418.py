#include<stdio.h>
#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    double time = 0, temp1, temp2, c, f, x, rate=2;

    long long int noofcases, i;
    cout.precision(6);
    cout.fixed;
    cin>>noofcases;
    for(i=0; i<noofcases; i++)
    {
        cin>>c>>f>>x;

        temp1 = x/rate;

        while(1)
        {
            temp2 = c/rate + x/(rate + f);
            if(temp1 > temp2)
            {
                time = time + c/rate;
                rate = rate + f;
                temp1 = x/rate;
            }
            else
                {
                    time = time + x/rate;
                    break;
                }
        }

        printf("Case #%lld: %.7lf\n",i+1,time);
        time = 0;
        rate = 2;

    }



return 0;
}
