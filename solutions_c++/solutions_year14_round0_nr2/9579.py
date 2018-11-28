#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;

double luiccha(double b,double val,double x,double f, double c)
{

    if((x/b)<=((x/(b+f))+(c/b)))
    {
        return val+(x/b);
    }
    else
    {
        val+=c/b;
        b+=f;
        return luiccha(b,val,x,f,c);

    }
}

int main()
{
    double b,t,i,j,k,l,val,c,f,x;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        val=0;
        b=2;
        cin>>c>>f>>x;
        k=luiccha(b,val,x,f,c);
        printf("Case #%.0lf: %.7lf\n",i,k);
    }
}

