#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("op2.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        double c,f,x,ans=0,t1,t2=0,s=2;
        cin>>c>>f>>x;
        t1=x/s;
        t2=c/s+(x/(s+f));
        if(t1<t2)
        ans=t1;
        else{
        while(t1>t2)
        {
            ans+=(c/s);
            s+=f;
            t1=x/s;
            t2=c/s+(x/(s+f));
        }
        ans+=t1;
        }
        printf("Case #%d: %.8lf\n",q,ans);
    }
    return 0;
}
