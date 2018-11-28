//
//  main.cpp
//  noob
//
//  Created by Lingsong Zeng on 2/29/16.
//  Copyright © 2016 Lingsong Zeng. All rights reserved.
//


#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=33333335;
bool mark[maxn+5];
vector<int>p;
vector<string>ans;
vector<vector<int> >f;
int prime(long long x)
{
    if(x==1)
        return 1;
    for(int i=0;i<p.size();i++)
    {
        if(p[i]>x/p[i])break;
        if(x%p[i]==0)return p[i];
    }
    return 1;
}
int main()
{
    for(int i=2;i<=maxn;i++)
    if(!mark[i])
    {
        p.push_back(i);
        for(int j=1;j*i<=maxn;j++)
            mark[j*i]=true;
    }
    for(int i=(1<<15)+1;i<=(1<<16)-1;i+=2)
    {
        bool flag=true;
        vector<int>t;
        string s="";
        long long tmp=i;
        while(tmp)
        {
            s+=to_string(tmp%2);
            tmp/=2;
        }
        reverse(s.begin(),s.end());
        for(int j=0;j<9;j++)
        {
            long long ret=0;
            long long base=j+2;
            long long cnt=1;
            long long tmp=i;
            while(tmp)
            {
                ret+=cnt*(tmp%2);;
                cnt*=base;
                tmp/=2;
            }
            int fac=prime(ret);
            if(fac==1)
            {
                flag=false;
                break;
            }
            t.push_back(fac);
        }
        if(flag)
        {
            f.push_back(t);
            ans.push_back(s);
            if(ans.size()>=50)
                break;
        }
    }
    printf("Case #1:\n");
    for(int i=0;i<ans.size();i++)
    {
        cout<<ans[i];
        for(int j=0;j<f[i].size();j++)
            cout<<" "<<f[i][j];
        cout<<endl;
    }
}