# include <cstdio>
#include<iostream>
#include <cstring>
#include <algorithm>
#include<bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 1001000009
#define MaxVal 200100


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int m;
        cin>>m;
        string s;
        cin>>s;
        int ans=0,cnt=0;
        for(int i=0;i<=m;i++)
        {
            if(cnt < i)
            {
                ans++;
                cnt++;
                cnt+=(s[i]-'0');
            }
            else
            {
                cnt+=(s[i]-'0');
            }
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}

