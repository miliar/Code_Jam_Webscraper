//
//  main.cpp
//  codejam
//
//  Created by shawpan on 4/12/14.
//  Copyright (c) 2014 shawpan. All rights reserved.
//
#include <iostream>
#include <queue>
#include <utility>
#include <string.h>
#include <map>
#include <vector>
using namespace std;
map<pair<long long, long long>, long long> h;
vector<pair<long long, long long>> parents;
long long gcd(long long a,long long b)
{
    if(!b) return a;
    
    return  gcd(b, a%b);
}
pair<long long, long> haveChild(pair<long long, long long> p1, pair<long long, long long> p2)
{
    long long p = p1.first * p2.second + p1.second * p2.first;
    long long q = p1.second * p2.second * 2;
    long long d = gcd(p, q);
    return make_pair(p/d,q/d);
}
int main(int argc, const char * argv[])
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long tc,i,p,q,d,j,k;
    scanf("%lld",&tc);
    h[make_pair(1, 1)] = 0; h[make_pair(0,1)] = 50;
    parents.push_back(make_pair(1, 1));
    parents.push_back(make_pair(0, 1));
    
    for(i=0;i<13;i++)
    {
        
        vector<pair<long long, long long>> nPs;
        for(j=0;j<parents.size();j++)
        {
            for(k=j;k<parents.size();k++)
            {
                pair<long long, long long> child = haveChild(parents[j],parents[k]);
                long long minP = h[parents[j]] < h[parents[k]] ? h[parents[j]] : h[parents[k]];
                if(h.find(child) == h.end())
                {
                    nPs.push_back(child);
                    h[child] = minP + 1;
                }
            }
        }
        parents.insert(parents.end(),nPs.begin(),nPs.end());
    }
    for(i=1;i<=tc;++i)
    {
        scanf("%lld/%lld",&p,&q);
        d =gcd(p,q);
        p /=d; q/=d;
        if(h.find(make_pair(p,q)) == h.end() || h[make_pair(p, q)] > 45)
            printf("Case #%lld: impossible\n",i);
        else
            printf("Case #%lld: %lld\n",i,h[make_pair(p, q)]);
    }
    return 0;
}

