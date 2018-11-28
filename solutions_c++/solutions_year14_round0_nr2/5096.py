#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    double coo,foo,xoo,v,cf,f1,cf1,i,v1,v2,t;int y=0;
    cin>>t;
    while(t--)
    {
i=0;
f1=2;
v1=0;
    cin>>coo>>foo>>xoo;
    while(1)
    {
    if(i==0)
    {
        i++;
    v=coo/2;
    v1+=v;
    v2=xoo/2;
    cf=v2;   
    cf1=cf;
    if(coo>xoo){cf1=xoo/2;break;}
//cout<<cf<<"a ";
    }
    else{
            f1+=foo;
        v=coo/f1;
    v1+=v;
    v2=xoo/f1;
    cf=v1-v+v2;
//cout<<cf<<"b ";
    if(cf>cf1)break;
cf1=cf;
    }
}
printf("Case #%d: %.7lf\n",++y,cf1);    }
    return 0;
}
