#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

double bsol,c,f,x,cval,r;
int i,T;
vector<double> D;
bool stop;

int main()
{
    ifstream f1("1.in");
    ofstream f2("1.out");
    f1>>T;
    for(int ct=1;ct<=T;ct++)
    {
        f1>>c>>f>>x;
        r=2;
        bsol=x/r;
        D.clear();
        D.push_back(0);
        for(i=1;i<1000000;i++)
        {
            cval=D[i-1]+c/(r+(i-1)*f);
            D.push_back(cval);
        }
        stop=false;
        for(i=1;i<1000000&&!stop;i++)
        {
            cval=D[i]+x/(r+i*f);
            if(cval>bsol)
               stop=true;
            else
                bsol=cval;
        }
        f2<<"Case #"<<ct<<": ";
        f2<<fixed<<setprecision(7)<<bsol<<"\n";
    }
    return 0;
}
