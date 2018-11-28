//
//  main.cpp
//  A
//
//  Created by Oleg Petrov on 12/04/2014.
//  Copyright (c) 2014 Oleg Petrov. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int getSteps(const vector<int> &v, int d)
{
    int sum = 0;
    int mx = 0;
    for(int i = 0; i < v.size(); ++i)
        if(v[i] >=  d)
        {
            int r = (v[i] + d - 1) / d - 1;
            sum += r;
        }
    return d + sum;
}

void test(int T)
{
    int n;
    vector<int> v;
    scanf("%d",&n);
    for(int i = 0; i < n; ++i)
    {
        int t;
        scanf("%d",&t);
        v.push_back(t);
    }
    int answ = 1e9;
    for(int i = 1; i <= 1000; ++i)
        answ = min(answ, getSteps(v, i));
    printf("Case #%d: %d\n", T, answ);
}

int main(int argc, const char * argv[])
{

    freopen("/Users/olpet/Downloads/tmp_files/b.in", "r", stdin);
    freopen("/Users/olpet/Downloads/tmp_files/b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}

