#include<iostream>
#include <iomanip>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("fun.in", "r", stdin);
    freopen("fun.out", "w", stdout);
    int T,t;
    double C,F,X;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>C>>F>>X;
        double sum_time=0,add_time=0;
        double cur_time=0;
        double add=2.0;
        sum_time=X/2.0;
        while(1)
        {
            cur_time=add_time;
            cur_time+=(X/add);
            if(cur_time<=sum_time){
                sum_time=cur_time;

                cur_time=add_time;
                cur_time+=C/add;
                add+=F;
                add_time=cur_time;
            }
            else
                break;
        }
        cout<<"Case #"<<t<<": ";
        cout << fixed << setprecision(7) <<sum_time<< endl;
    }
    return 0;
}
