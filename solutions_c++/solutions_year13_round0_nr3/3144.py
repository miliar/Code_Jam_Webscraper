#include<iostream>
#include <stdio.h>
#include<math.h>
#include<fstream>
#include<cstring>
#include <stdlib.h>
using namespace std;

int main()
{
    ifstream r;
    ofstream w;
    r.open("C-small-attempt0.in");
    w.open("output.txt");

    int a[]={1,4,9,121,484},cno=0,t,st,end;

    r>>t;
    while(t--)
    {
        r>>st>>end;

        int i,ctr=0;
        ++cno;

        for(i=0;i<5;i++)
        {
            if(a[i]>=st && a[i]<=end)
                ctr++;
        }

        w<<"Case #"<<cno<<": "<<ctr<<endl;
    }
    return 0;
}
