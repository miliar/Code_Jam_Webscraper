// Copyright 2015 © Ayush Garg
// All rights reserved.
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,x,y) for(i=x;i<y;i++)
#define f first
#define s second
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%I64d",&x)
#define author ayushgarg
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

int a[13];

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,t,flag,ct;
    ll x,ans,n;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        flag=ct=0;
        x=0LL;
        memset(a,0,sizeof(a));
        scanf("%lld",&n);
        for(i=1;i<100;i++)
        {
            x=i*n;
            ans=x;
            while(x>0LL)
            {
                j=x%10LL;
                if(a[j]==0)
                {
                    ct++;
                    a[j]=1;
                }
                x/=10LL;
            }
            if(ct>=10)
            {flag=1;break;}
        }

        if(flag==1)
            printf("Case #%d: %lld\n",tt,ans);
        else
            printf("Case #%d: INSOMNIA\n",tt);
    }
    return 0;
}
