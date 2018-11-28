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
    freopen("1AAin.txt","r",stdin);
    freopen("1AAout.txt","w",stdout);
    long long int t,n,i,j,l,x,k,a[1005];
    slld(t);
    for(x=1;x<=t;x++)
    {
        slld(n);
        for(j=0;j<n;j++)
            slld(a[j]);
        k=0;j=0;
        for(i=0;i<n-1;i++)
        {
            if(a[i]>a[i+1])
            {
                if((a[i]-a[i+1])>k)
                    k=a[i]-a[i+1];
                j+=a[i]-a[i+1];
            }
        }
        l=0;
        for(i=0;i<n-1;i++)
        {
            if(a[i]>=k)
                l+=k;
            else
                l+=a[i];
        }
        printf("Case #%lld: %lld %lld\n",x,j,l);
    }
    return 0;
}
