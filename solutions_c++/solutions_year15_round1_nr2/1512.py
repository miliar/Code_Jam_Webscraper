//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
long long int gcd(long long int a,long long int b)
{
    if(a%b==0)
        return b;
    return gcd(b,a%b);
}
long long int a[1005],c[1005];
int main()
{
    //freopen("1ABSin.txt","r",stdin);
    //freopen("1ABSout1.txt","w",stdout);
    long long int n,b,i,j,k,s,min1;
    int t,x;
    sd(t);
    for(x=1;x<=t;x++)
    {
        slld(b);
        slld(n);
        for(i=0;i<b;i++)
            slld(a[i]);
        j=a[0];
        for(i=1;i<b;i++)
            j=(j*a[i])/gcd(j,a[i]);
        s=0;
        for(i=0;i<b;i++)
            s+=j/a[i];
        n=n%s;
        if(n==0)
            n=s;
        if(n<=b)
            s=n;
        else
        {
            for(i=0;i<b;i++)
                c[i]=a[i];
            for(i=b;i<n;i++)
            {
                min1=c[0];
                k=1;
                for(j=0;j<b;j++)
                {
                    if(c[j]<min1)
                    {
                        min1=c[j];
                        k=j+1;
                    }
                }
                c[k-1]+=a[k-1];
            }
            s=k;
        }
        printf("Case #%d: %lld\n",x,s);
    }
    return 0;
}
