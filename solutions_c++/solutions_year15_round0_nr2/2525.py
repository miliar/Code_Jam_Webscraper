#include<bits/stdc++.h>
using namespace std;
#define cin(n) scanf("%d",&n)
int a[1008];

int main() 
{
    int t,m,n,i,j,k,l;
    int ct=1;
    cin(t);
    
    while(t--)
    {
        cin(n);
        int mx=0;
        for(i=1;i<=n;i++)
        {
            cin(a[i]);
            mx=max(mx,a[i]);
        }
        int ans=mx;
        for(i=1;i<=mx;i++)
        {
            int vl=0;
            for(j=1;j<=n;j++)
            {
                k=(a[j]+i-1)/i;
                vl+=k-1;
            } 
            ans=min(ans,vl+i);
        } 
        cout<<"Case #"<<ct++<<": "<<ans<<"\n";
    }    
    
    return 0;
}
