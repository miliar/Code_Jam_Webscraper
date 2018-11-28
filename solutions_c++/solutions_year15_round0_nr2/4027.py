#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
#define ll long long int

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    freopen("B.txt","r",stdin);
    freopen("Bout.txt","w",stdout);
    int t;
    cin>>t;
    for(int q=1;q<=t;++q) 
    {
        int n;
        cin>>n;
        int a[n+1000],b[n+1000],ans=0,tans,tn;
        for(int i=0;i<n;++i)
        {
            cin>>a[i];
            if(a[i]>ans)
                ans=a[i];
            b[i]=a[i];
        }
        if(ans==9)
        {
            tans=ans;
            tn=n;
            for(int m=1;m<100;++m)
            {
                int ma=0,pos;
                for(int j=0;j<n;++j)
                {
                    if(a[j]>ma)
                    {
                        ma=a[j];
                        pos=j;
                    }
                }
                if(ma%2==0)
                {
                    a[pos]=ma/2;
                    a[n]=ma/2;
                    n++;
                }
                else
                {
                    a[pos]=(ma+1)/2;
                    a[n]=(ma-1)/2;
                    n++;
                }
                ma=0;
                for(int j=0;j<n;++j)
                {
                    if(a[j]>ma)
                    {
                        ma=a[j];
                        pos=j;
                    }
                }
                ans=min(ans,ma+m);

            }
            for(int m=1;m<100;++m)
            {
                int ma=0,pos;
                for(int j=0;j<tn;++j)
                {
                    if(b[j]>ma)
                    {
                        ma=b[j];
                        pos=j;
                    }
                }
                if(ma%2==0)
                {
                    b[pos]=ma/2;
                    b[tn]=ma/2;
                    tn++;
                }
                else if(ma==9)
                {
                    b[pos]=3;
                    b[tn]=6;
                    tn++;    
                }
                else
                {
                    b[pos]=(ma+1)/2;
                    b[tn]=(ma-1)/2;
                    tn++;
                }
                ma=0;
                for(int j=0;j<tn;++j)
                {
                    if(b[j]>ma)
                    {
                        ma=b[j];
                        pos=j;
                    }
                }
                tans=min(tans,ma+m);

            }
            ans=min(ans,tans);
        }
        else
        {
            for(int m=1;m<100;++m)
            {
                int ma=0,pos;
                for(int j=0;j<n;++j)
                {
                    if(a[j]>ma)
                    {
                        ma=a[j];
                        pos=j;
                    }
                }
                if(ma%2==0)
                {
                    a[pos]=ma/2;
                    a[n]=ma/2;
                    n++;
                }
                else
                {
                    a[pos]=(ma+1)/2;
                    a[n]=(ma-1)/2;
                    n++;
                }
                ma=0;
                for(int j=0;j<n;++j)
                {
                    if(a[j]>ma)
                    {
                        ma=a[j];
                        pos=j;
                    }
                }
                ans=min(ans,ma+m);

            }
        }
        printf("Case #%d: %d\n",q,ans);
    } 
    return 0;
}
