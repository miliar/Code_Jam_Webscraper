#include <iostream>
#include <cstdio>
using namespace std;

int t,x,c,r;
bool valasz[100];

int main()
{
 //   freopen("D-small-attempt0.in","r",stdin);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>x>>c>>r;
        if(x==1) valasz[i]=true;
        if(x==2 && (c*r)%2==0) valasz[i]=true;
        if(x==3)
        {
            if((c*r)%3==0 && min(c,r)>1) valasz[i]=true;
        }
        if(x==4)
        {
            if((c*r)%4==0 && min(c,r)>2) valasz[i]=true;
        }
        if(x==5)
        {
            if((c*r)%5==0 && min(c,r)>2 && max(c,r)>4) valasz[i]=true;
        }
        if(x==6)
        {
            if((c*r)%6==0 && min(c,r)>3) valasz[i]=true;
        }
    }
 //   freopen("output.in","w",stdout);
    for(int i=1;i<=t;i++)
    {
        if(valasz[i]) cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
        if(!valasz[i]) cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
    }
    return 0;
}
