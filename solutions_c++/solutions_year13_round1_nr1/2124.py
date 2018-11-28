#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,tc;
    long long int r,p,c,tot,used;
    scanf("%d",&t);
    //cout<<t<<endl;
    for(tc=1;tc<=t;tc++)
    {
        scanf("%I64d %I64d",&r,&p);
        //pa=pi*p;
        tot=0; c=0;
        while(tot<=p )//&& fabs(pa-tot)>epsilon)
        {
            tot+=(r<<1)+1;
            //cout<<used<<" "<<tot<<" "<<p<<endl;
            if(tot<=p )//|| fabs(pa-tot)<epsilon)
               c++;
            r+=2;
        }
        printf("Case #%d: %I64d\n",tc,c);
    }
    return 0;
}
