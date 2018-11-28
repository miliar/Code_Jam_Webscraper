//
//
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<vector>
#include<string>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
double a[205];
int n,k;
int b[20];
double ans;
void choose(int p,int q)
{
    if(q==k)
    {
        vector<double>dp;
        for(int i=1;i<p;i++)
        if(b[i])
            dp.push_back(a[i]);
        string s="";
        for(int i=0;i<k/2;i++)
            s+="0";
        for(int i=0;i<k/2;i++)
            s+="1";
        double cnt=0;
        do
        {
            double tmp=1;
            for(int i=0;i<dp.size();i++)
            if(s[i]=='0')
                tmp*=(1-dp[i]);
            else
                tmp*=dp[i];
            cnt+=tmp;
        }while(next_permutation(s.begin(),s.end()));
        ans=max(ans,cnt);
        return;
    }
    if(p==n+1)
        return;
    if(n-p+1<k-q)
        return;
    b[p]=1;
    choose(p+1,q+1);
    b[p]=0;
    choose(p+1,q);
}
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        cin>>n>>k;
        for(int i=1;i<=n;i++)
            cin>>a[i];
        ans=0;
        choose(1,0);
        printf("%.12f\n",ans);
    }
}