#include<stdio.h>
#include<fstream>
#include<iostream>
#define ll long long
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    ll r,t;
    int p=0;
    fin>>T;
    while(T--)
    {
        p++;ll count=0;
        fin>>r>>t;
        while(t>=0)
        {
            t=t-((r+1)*(r+1)-r*r);
            r+=2;count++;
        }
        fout<<"Case #"<<p<<": "<<count-1<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}