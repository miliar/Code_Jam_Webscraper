// Copyright 2015 © Ayush Garg
// All rights reserved.
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,x,y) for(i=x;i<y;i++)
#define f first
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%I64d",&x)
#define author ayushgarg
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
string s;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,t,ct,mod,len;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        mod=0;
        ct=0;
        cin>>s;
        len = (int)(s.size());
        for(i=len-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                if(mod==1)
                {
                    ct++;
                    mod=0;
                }
            }
            else
            {
                if(mod==0)
                {
                    ct++;
                    mod=1;
                }
            }
        }

        printf("Case #%d: %d\n",tt,ct);
    }
    return 0;
}
