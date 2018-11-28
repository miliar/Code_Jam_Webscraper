//
//  main.cpp
//  Main
//
//  Created by AIdancer on 16/4/6.
//  Copyright © 2016年 AIdancer. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

bool flag, visit[10];

void solve() {
    int T, N;
    cin >> T;
    for(int Case = 1; Case <= T; Case++) {
        cin >> N;
        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", Case);
            continue;
        }
        memset(visit, false, sizeof(visit));
        flag = false;
        LL sum = 0, tmp;
        while(!flag) {
            sum += N;
            tmp = sum;
            for(;tmp;) {
                visit[tmp%10] = true;
                tmp /= 10;
            }
            flag = true;
            for(int j = 0; j < 10; j++) {
                if(!visit[j]) {
                    flag = false;
                    break;
                }
            }
        }
        printf("Case #%d: %lld\n", Case, sum);
    }
}

int main(int argc, const char * argv[]) {
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/A-large.in", "r", stdin);
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/data.out", "w", stdout);
    solve();
    return 0;
}















