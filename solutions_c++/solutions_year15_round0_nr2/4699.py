//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
int main()
{
    int t,x,n,a[10],i,j,s,max1,tmin;
    sd(t);
    for(x=1;x<=t;x++)
    {
        sd(n);
        for(i=0;i<n;i++)
             sd(a[i]);
        max1=a[0];
        for(i=1;i<n;i++)
        {
            if(a[i]>max1)
                max1=a[i];
        }
        tmin=max1;
        for(i=1;i<=max1;i++)
        {
            s=i;
            for(j=0;j<n;j++)
            {
                s+=a[j]/i;
                if(a[j]%i==0)
                    s--;
            }
            if(s<tmin)
                tmin=s;
        }
        printf("Case #%d: %d\n",x,tmin);
    }
    return 0;
}
