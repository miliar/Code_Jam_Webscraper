#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int cntr=0,t;
    double c,f,x,r=2.0,sum=0,time=0,t1,t2;
    cin>>t;
    while((++cntr)<=t)
    {
        cin>>c>>f>>x;
        r=2.0,sum=0,time=0;
        while(sum<x)
        {
            t1=(x-sum)/r;
            t2=c/r + x/(r+f);
            if(t1<t2)
            {
                time+=t1;
                sum=x;
            }
            else
            {
                time+=c/r;
                sum=0;
                r+=f;
            }
        }
        printf("Case #%d: %.7lf\n",cntr,time);
    }
    return 0;
}
