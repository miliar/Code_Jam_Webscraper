#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int test,t;
    double time=0.0,timenext=0.0,timefinal=0.0,rate;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>test;
    double C,F,X;
    for(t=1;t<=test;t++)
    {
        cin>>C>>F>>X;
        time=0.0,timenext=0.0,timefinal=0.0;
        rate= 2.0;
        while(1)
        {
            time= X/rate;
            timenext = (C/(rate*1.0))+ (X/(rate+F)*1.0);
            if(timenext < time )
            {
                timefinal+= (C/rate*1.0);
                rate = rate+F*1.0;
            }
            else
            {
                timefinal+= time;
                break;
            }


        }
        cout<<"Case #"<<t<<": ";
        printf("%0.7f\n",timefinal);
    }
}
