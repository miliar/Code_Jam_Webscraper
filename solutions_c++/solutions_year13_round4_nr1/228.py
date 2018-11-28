//
//  main.cpp
//  Codeforces
//
//  Created by Taygrim on 20.03.13.
//  Copyright (c) 2013 Taygrim. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

struct str
{
    long s;
    long f;
    long kol;
    str(long ss, long ff, long kkol)
    {
        s = ss;
        f = ff;
        kol = kkol;
    }
};

bool operator < (const str &a, const str &b)
{
    return a.s<b.s;
}

const long mod = 1000002013;

long long price(long long n, long long k)
{
    return (((2*n - k + 1) * k)/2) % mod;
}

int main()
{
    ifstream cin("A-large.in.txt");
    ofstream cout("output.txt");
    long t;
    cin>>t;
    
    for(long w=0; w<t; w++)
    {
        long n, m;
        cin>>n>>m;
        vector<long> mass;
        map<long, long> enter;
        map<long, long> leave;
        long long real = 0;
        for(long i=0; i<m; i++)
        {
            long s, f, kol;
            cin>>s>>f>>kol;
            mass.push_back(s);
            mass.push_back(f);
            enter[s] += kol;
            leave[f] += kol;
            real += price(n, f-s) * (long long)kol;
            real %=mod;
        }
        
        sort(mass.begin(), mass.end());
        
        map <long, long> now;
        
        long long pay = 0;
        
        for(long j=0, i=mass[j]; j<mass.size(); j++, i=mass[j])
        {
            if(j!=0 && mass[j] == mass[j-1])
                continue;
            
            if(enter[i] != 0)
                now[i] += enter[i];
            
            if(leave[i] != 0)
            {
                vector<long> er;
                map <long, long> ::iterator it = now.end();
                it--;
                for(;;it--)
                {
                    if(it->second <= leave[i])
                    {
                        leave[i] -= it->second;
                        pay += price(n, i - it->first) * it->second;
                        pay %= mod;
                        er.push_back(it->first);
                    }
                    else
                    {
                        it->second -= leave[i];
                        pay += price(n, i - it->first) * leave[i];
                        pay %= mod;
                        leave[i] = 0;
                    }
                    
                    if(leave[i] == 0)
                        break;
                }
                
                for(long q=0; q<er.size(); q++)
                    now.erase(er[q]);
            }
        }
        
        long long res = real - pay;
        while (res < 0)
            res += mod;
        
        res %=mod;
        cout<<"Case #"<<w+1<<": ";
        cout<<res<<"\n";
    }
}