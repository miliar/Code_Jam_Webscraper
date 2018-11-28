//
//  main.cpp
//  A
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
int n;
string s;

void solve(int tcase){
    int sum = 0;
    int res = 0;
    for(int i = 0; i <= n; ++i ){
        int need = max(0, i - sum );
        res = max(res, need );
        sum += s[i] - '0';
    }
    printf("Case #%d: %d\n", tcase, res);
}

int main(int argc, const char * argv[]) {
    freopen("/Users/liqiu/Desktop/A/Alarge.in", "r", stdin );
    freopen("/Users/liqiu/Desktop/A/A.out", "w", stdout );
    int T;
    cin >> T;
    int tcase = 0;
    while(T--){
        ++tcase;
        cin >> n;
        cin >> s;
        solve(tcase);
    }
    return 0;
}
