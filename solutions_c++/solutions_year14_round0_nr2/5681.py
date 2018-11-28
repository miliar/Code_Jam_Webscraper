#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int t,w=1;
    freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    double c,f,x,t1,t2,n,c_1=0,i;
    cin>>t;
    while(t--)
    {
        cin>>c>>f>>x;
        c_1=0.000000;
        t2=0.0000000;
        t1=0.000000;
        t1=(double)x/2;
        n=1;
        while(1)
        {
            c_1=0;
            for(i=0;i<n;++i)
                c_1=c_1+( double)(c/(2+( double)(i*f)));
            t2=c_1+( double)(x/(2+(double)(n*f)));
            if(t2>t1)
                break;
            t1=t2;
            n=n+1;

        }
        printf("Case #%d: %.7f\n",w,t1);
    ++w;
    }
    return 0;
}
