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
#include <map>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int,int> pii;
typedef pair<double,double> pdd;

int n;
pdd need;

double eps = 1e-7;

void test(int T)
{
    double answ = 0;
    scanf("%d%lf%lf",&n, &need.second, &need.first);
    vector<pdd> v;
    for(int i = 0; i < n; ++i)
    {
        pdd p;
        scanf("%lf%lf",&p.second,&p.first);
        v.push_back(p);
    }
    sort(v.begin(), v.end());
    if(need.first < v[0].first - eps || v.back().first + eps < need.first)
    {
        printf("Case #%d: IMPOSSIBLE\n", T);
        return;
    }
    if(n == 1)
    {
        answ = need.second / v[0].second;
    }
    else
        if(v[1].first - v[0].first < eps)
            answ = need.second / (v[0].second + v[1].second);
        else
        {
            double V0 = -(need.first - v[1].first) / (v[1].first - v[0].first) * need.second;
            double V1 = (need.first - v[0].first) / (v[1].first - v[0].first) * need.second;
            answ = max(V0 / v[0].second, V1 / v[1].second);
        }
    printf("Case #%d: %.9lf\n", T, answ);
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

/*
 1
 2 30.0000 65.4321
 0.0001 50.0000
 100.0000 99.9000
 */

