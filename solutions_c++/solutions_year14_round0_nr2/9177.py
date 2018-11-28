

#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<t+1;i++)
{
    double c, f, x,time,mt,v;
    v=2.0000000;
    time=0;
    cin>>c>>f>>x;
    mt=x;
    while(true)
    {
        double k;
        k=x/v;
        mt = min(mt,(time + k));
        time=time+(c/v);
        v=v+f;
        if(time>mt) break;
    }
    printf("Case #%i: %.7lf\n",i,mt);
}
}


