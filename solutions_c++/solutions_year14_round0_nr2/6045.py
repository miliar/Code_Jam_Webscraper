#include<iostream>
#include<algorithm>
#include<fstream>
#include<stdio.h>

using namespace std;

int main()
{
    ifstream in;
    in.open("B-large.in");
    FILE * out;
    out = fopen("outputB.txt","w");
    int t;
    in>>t;
    for(int z = 0; z<t;z++)
    {
        double c,f,x,time,cps;
        double table[100000];
        cps = 2.0;
        in>>c>>f>>x;
        time = 9999000;
        table[0] = 0;
        for(int i = 1; i<100000;i++)
        {
            table[i] = c/cps + table[i-1];
            //cout<<table[i]<<endl;
            cps+=f;
        }
        cps = 2.0;
        for(int i = 0; i<100000;i++)
        {
            table[i]+= x/cps;
            cps += f;
        }
        for(int i = 0; i<100000;i++)
        {
            time = min(time, table[i]);
        }
        //cout<<"Case #"<<z+1<<": "<<time<<endl;
        fprintf(out,"Case #%d: %.7f\n",z+1,time);
    }
    return 0;
}
