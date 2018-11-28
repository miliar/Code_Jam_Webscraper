#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

double tim(double p, double c, double f, double x)
{
    //cout<<p<<" "<<c<<" "<<f<<" "<<x<<endl;
    if(x/p<=c)
        return x/p;
    return min( x/p, c/p+tim(p+f, c, f, x) );
}

#define MAX 100000

int main()
{
    int t;
    scanf("%d", &t);
    double tot[MAX];
    for(int i=0; i<t; i++)
    {
        printf("Case #%d: ", i+1);
        double p=2.0,c,f,x;
        scanf("%lf%lf%lf", &c, &f, &x);
        tot[0]=x/p;
        double minimo=x/p;
        for(int j=1; j<MAX; j++){
            tot[j]=tot[j-1]+x/(p+j*f)+(c-x)/(p+(j-1)*f);
            if(tot[j]>=minimo)
                break;
            else
                minimo=tot[j];
        }


        printf("%.7lf\n", minimo);
/*
        cout<<endl;
        for(int j=0; j<50; j++){
            cout<<j<<": "<<tot[j]<<endl;
        }*/

    }
}
