#include<iostream>
#include<stdio.h>
#include <iomanip>
#include<fstream>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    cout<<setprecision(7)<<fixed;
    for(int k=1;k<=t;k++)
    {
        long double cost,add_rate,target;
        cin>>cost>>add_rate>>target;
        long double rate = 2;
        long double value =  target/rate;
        long double seconds = cost/rate;
        for(int i=1;i<=(target/cost);i++)
        {

           long double temp = seconds + target/(rate+i*add_rate);
            if(value > temp)
                value = temp;
//            else
//                break;
            seconds = seconds + cost/(rate+i*add_rate);
        }
        cout<<"Case #"<<k<<": "<<value<<endl;

    }
}
