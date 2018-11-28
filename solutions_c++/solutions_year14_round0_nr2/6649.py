#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int T;
        cin >> T;
    int i;
            for(i=1;i<=T;i++)
            {
                double C,F,X;
                cin >> C >> F >> X;
                double curr_cokkies=0;
                double rate=2;
                double total_time=0;
                while(curr_cokkies<X)
                {
                    double ans1=(X)/rate;
                    double ans2=((double)C/rate + (double)X/(rate+F));
                    if(ans1<=ans2)
                        {
                            curr_cokkies=X;
                            total_time = total_time + ans1;
                        }
                    else
                        {
                            curr_cokkies=0;
                            total_time = total_time + (double)C/rate;
                            rate=rate+F;
                        }
                }
           printf("Case #%d: %.7lf\n",i,total_time);
            }
}
