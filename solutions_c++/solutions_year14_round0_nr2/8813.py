#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;

ifstream f("input2.txt");
FILE *g = fopen("output2.txt","w");

int T;
double C, F, X;

inline double timeNeeded(void)
{
    double t1 = X, t2 = X/2,auxt = 0;

    for(int i=1;t1 > t2;i++)
    {
        t1 = t2;

        auxt += C / (2.0 + F * (i-1));
        t2 = auxt + X / (2.0 + F * i);
    }

    return t1;
}

int main()
{
    f >> T;

    for(int i=1;i<=T;i++)
    {
        f >> C >> F >> X;
        fprintf(g,"Case #%d: %.7lf\n",i,timeNeeded());
    }
}
