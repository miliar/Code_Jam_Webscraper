#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <map>
#include <bitset>
#include <string.h>
using namespace std;

inline long readI()
{
    int x=0;
    char t;
    t=getchar_unlocked();
    while(t<48 || t>57)
        t=getchar_unlocked();
    while(t>=48 && t<=57)
    {
        x*=10;
        x+=t-'0';
        t=getchar_unlocked();
    }
    return x;
}

double ans=0;
double c,f,x;

void div(double cr,double time)
{
    double c1=0,c2=0;
    c1 = x/cr;
    c2 = (double)(c/cr) + (double)(x/(cr+f));
    ans+= (c1 < c2 )?(double)(x/cr):(double)(c/cr);
    if(c1 < c2 )
        return;
    else
        div((cr+f),ans); 
}

int main()
{
    int t = readI();
    int j = 0;
    for(j=1;j<=t;j++)
    {
        cin>>c>>f>>x;
        div(2.0,0.0);
        printf("Case #%d: %f\n",j,ans);
        c=f=x=ans=0.0;
    }
    return 0;
}