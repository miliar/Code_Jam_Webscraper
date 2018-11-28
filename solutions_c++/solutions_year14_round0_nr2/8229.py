#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#define ll long long
using namespace std;
int main()
{
    int t,k,i,j;
    double s1,s2,sum,c,f,x,rate;
    fstream f1,f2;
    f1.open("B-small-attempt0.in",ios::in);
    f2.open("output.txt",ios::out);
    f1>>t;
    for(k=1;k<=t;k++)
    {
        sum=0;
        rate=2.0000000;
        f1>>c>>f>>x;
        while(1)
        {
            s1=x/rate;
            s2=x/(rate+f)+c/rate;
            if(s1>s2){
                sum+=(c/rate);
                rate+=f;
            }
            else{
                sum+=s1;
                f2.precision(7);
                f2.setf(ios::fixed,ios::floatfield);
                f2<<"Case #"<<k<<": "<<sum<<endl;
                break;
            }
        }
    }
    return 0;
}
