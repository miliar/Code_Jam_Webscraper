// -*- C++ -*-
// File: a.cpp
// Copyright (C) 2013
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

/*** TEMPLATE CODE ENDS HERE */

struct nData {
    double gain, sec, cookies;
};

double get_leftovers(double gain, double cookies, double target) {
    if(target<=cookies) return 0;
    return (target-cookies)/gain;
}

nData get_next_farm(double gain, double cookies, double C, double F, double sec) {
    double farm_getting_time = get_leftovers(gain, cookies, C);
    sec += farm_getting_time;
    cookies -= farm_getting_time * gain;
    gain += F;
    cookies = max(0.0, cookies);
    return {gain, sec, cookies};
}

double solve(double C, double F, double X) {
    double gain = 2;
    double cookies = 0;
    double T = get_leftovers(gain, cookies, X);
    nData nd = {gain, cookies, 0};
    
    while(true) {
        nd = get_next_farm(gain, cookies, C, F, nd.sec);
        double left = get_leftovers(nd.gain, nd.cookies, X);
        if(left + nd.sec < T) {
            T = nd.sec + left;
            gain = nd.gain;
            cookies = nd.cookies;
        }
        else
            break;
    }
    
    return T;
}

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int T;
    cin >> T;
    
    double C,F,X;
    
    FOR(cs,1,T+1) {
        
        cin >> C >> F >> X;
        
        double ans = solve(C, F, X);
        
        printf("Case #%d: %.7f", cs, ans);
        if(cs!=T) printf("\n");
    }

    return 0;
}
