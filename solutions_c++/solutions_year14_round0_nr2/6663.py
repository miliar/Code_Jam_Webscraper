#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<fstream>
#include<iomanip>
#define EPS						1e9
using namespace std;
int main()
{
    ofstream fout("output.in");
    ifstream fin("B-large.in");



    int t,k;
    fin>>t;
    for(k=1;k<=t;k++)
    {
        double C,F,X;
        fin>>C>>F>>X;
        //vector<double> time(500);
        //vector<double> rate(500);
        //rate[0]=2;
        int i,j;
        double rate=2,temp=0.0;
        double min=X/rate;
        while(1)
        {

             temp=temp+C/rate;
             rate=rate+F;
             double time=temp+X/(rate);
             if(time<min)
             {
                 min=time;
             }
             else
                break;
        }
        fout<<"Case #"<<k<<": "<<setprecision(12)<<min<<endl;

    }
}
