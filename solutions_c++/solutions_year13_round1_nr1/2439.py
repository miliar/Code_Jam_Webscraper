#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <map>
#include <set>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define RFOR(i,a,b) for(int i=a;i>=b;i--)
#define FORC(i,a,b,c) for(int i=a;i<b;i+=c)
#define pi 3.14159265358979
using namespace std;

int i,j,k;
int main()
{
    ofstream fout("A-small-attempt0.out");
    ifstream fin ("A-small-attempt0.in");

    //freopen("entrada.txt","r",stdin);
    //freopen("salida.txt","w",stdout);
    long long T;
    //long long t,T,r;
    fin >> T;
    FOR(i,0,T)
    {
        long long r,t;
        fin >> r >> t;
        int s = 0;
        long long td;
        long long areab;
        long long arean;
        long long rg = r+1;


        td = t;
        bool sw = true;
        while( sw)
        {
            arean = rg*rg;
            areab = r*r;


             if(td < (arean-areab))
                break;
            td = td - (arean-areab);
            //cout <<td << endl;
            s++;


            r+=2;
            rg+=2;

        }
        fout <<"Case #"<<i+1<<": " <<s << endl;/*

        long double r,t,a,s;
        fin>>r>>t;
        int c=0;
        a=pi*r*r;
        s=a;
        while(t>=s)
        {
            //fout<<a<<endl;
            a=pi*(r+1)*(r+1)-s;
            s+=a;
            r++;
            c++;
        }
        fout<<c<<endl;*/

    }



    return 0;
}
