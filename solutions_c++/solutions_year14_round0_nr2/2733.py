#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#define out "case #"
#define FOR(i,a,b) for(i=a;i<=b;i++)

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    long int t,j,num_of_farms,k;
    long double c,f,x,time,nof,rate;

    fin.open("1.in",ios::in);

    fout.open("1_0.out");

    fout.precision(15);

    fin.seekg(0);

    fin>>t;

FOR(j,1,t)
{

    rate=2;time=0;
    fin>>c>>f>>x;

    nof=(x/c)-(2/f);

    num_of_farms=floor(nof);


    FOR(k,1,num_of_farms)
    {
        time+=c/rate;
        rate+=f;
    }

    time+=x/rate;

    fout<<out<<j<<": "<<time<<'\n';
}
fin.close();
fout.close();
    return 0;
}
