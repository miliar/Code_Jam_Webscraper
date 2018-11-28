#include <iostream>
#include<stdio.h>
using namespace std;
double T,c,f,x,i,n,sum,t;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    t=T;
    while(T--)
    {
        cin>>c>>f>>x;
        n=(double(f*x-2*c-f*c)/double(f*c));
        sum=0;
        if(n>=0)
        {n=int(double(f*x-2*c-f*c)/double(f*c));
            for(i=0;i<=n;i++)
        {
            sum+=double(double(c)/double(2+f*i));
        }
        sum+=double(double(x)/double(2+f*(n+1)));
        }
        else
        {
            sum=double(double(x)/double(2));
        }
        printf("Case #%d: %.7lf\n",int(t-T),sum);
    }
    return 0;
}
