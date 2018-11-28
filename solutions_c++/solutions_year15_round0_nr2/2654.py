//
//  main.cpp
//  B
//
//  Created by Li Qiu on 4/10/15.
//  Copyright (c) 2015 Li Qiu. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <cstring>

using namespace std;

int tcase = 0;
const int maxn = 1e5 + 10;
const int inf = 1e8;
int p[maxn];
int n;


int getTime(int mx ){
    int cut = 0;
    for(int i = 0; i < n; ++i ){
        cut += ( p[i] - 1 ) / mx;
    }
    return cut + mx;
}
void solve(int tcase){
    int mx = *max_element(p, p + n );
    int res = inf;
    for(int i = 1; i <= mx; ++i ){
        res = min(res, getTime(i) );
    }
    printf("Case #%d: %d\n", tcase, res );
}
int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("/Users/liqiu/Desktop/B/B.in", "r", stdin );
    freopen("/Users/liqiu/Desktop/B/B.out", "w", stdout );
    int T;
    cin >> T;
    while(T-- ){
        tcase++;
        cin >> n;
        for(int i = 0; i < n; ++i ) cin >> p[i];
        solve( tcase );
    }
    return 0;
}
