#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
    ifstream fil;
    fil.open("B-small-attempt1.in");
    ofstream file;
    file.open("out.txt");
    int t;
    fil>>t;
    cout<<fixed;
    cout<<setprecision(7);
    for(int ct=1;ct<=t;ct++)
    {
        double i=2.0000000;
        double c,f,x,time=0.0000000;
        fil>>c;
        fil>>f;
        fil>>x;
        double ans=0.0000000;
        while(1)
        {
            if(x/i>(c/i+(x/(f+i))))
            {
                time+=c/i;
                i=i+f;
            }
            else
            {
                time+=x/i;
                break;
            }
        }
        //printf("Case #%d: %.7lf\n",ct,time);
        file<<"Case #"<<ct<<": "<<time<<"\n";
        cout<<"Case #"<<ct<<": "<<time<<"\n";

    }
    return 0;
}
