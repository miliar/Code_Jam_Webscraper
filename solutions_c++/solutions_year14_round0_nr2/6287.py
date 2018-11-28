#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <iomanip>

using namespace std;

double C,F,X,time[110],rate;
int i,j,T;
int main()
{
    fstream myfile;
    myfile.open("B-large.in",ios::in);
    myfile >> T;

    for(i=1;i<=T;i++)
    {
        time[i] = 0;
        rate = 2;
        myfile >> C >> F >> X;
        if(C >= X)
        {
            time[i] += X/rate;
        }
        else
        {
            while(true)
            {
                if(X/(rate+F) < (X-C)/rate)
                {
                    time[i]+= C/rate;
                    rate += F;
                }
                else
                {
                    time[i] += X/rate;
                    break;
                }
            }
        }
    }
    myfile.close();
    myfile.open("llala.in", ios::out);
    for(i=1;i<=T;i++)
    {
        myfile <<fixed<<setprecision(6)<< "Case #"<<i<<": "<<time[i]<<endl;
    }
    myfile.close();
    return 0;
}
