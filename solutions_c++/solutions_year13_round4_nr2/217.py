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

long long rec1(long long n, long long p)
{
    if(n == p)
        return n-1;
    
    if(p > n/2)
    {
        long long temp = rec1(n/2, p-n/2);
        return max(n-2, 2*temp + 1);
    }
    else
    {
        long long temp = rec1(n/2, p);
        return 2*temp;
    }
}

long long rec2(long long n, long long p)
{
    if(n == p)
        return n-1;
    
    if(p > n/2)
    {
        long long temp = rec2(n/2, p-n/2);
        return max((long long)0, 2*(temp+1));
    }
    else
        return 0;
}

int main()
{
    ifstream cin("B-large.in.txt");
    ofstream cout("output.txt");
    
    long t;
    cin>>t;
    
    for(long w=0; w<t; w++)
    {
        long long n, p;
        cin>>n>>p;
        long long res1 = rec1(((long long)1)<<n, p);
        long long res2 = rec2(((long long)1)<<n, p);
        
        cout<<"Case #"<<w+1<<": ";
        cout<<res2<<" "<<res1<<"\n";
    }
}