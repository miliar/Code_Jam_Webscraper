#include<stdio.h>
#include<fstream>
#include<iostream>
#define ll1 long long
using namespace std;
int main()
{
    ifstream finn;
    ofstream foutt;
    finn.open("input.txt");
    foutt.open("output.txt");
    int T;
    ll1 r,t;
    int p=0;
    finn>>T;
    while(T--)
    {
        p++;ll1 count=0;
        finn>>r>>t;
        while(t>=0)
        {
            t=t-((r+1)*(r+1)-r*r);
            r+=2;count++;
        }
        foutt<<"Case #"<<p<<": "<<count-1<<endl;
    }
    finn.close();
    foutt.close();
    return 0;
}