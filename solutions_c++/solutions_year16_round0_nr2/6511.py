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

char str[105], tmp[105];

void solve() {
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; Case++) {
        scanf(" %s", str);
        int n = (int)strlen(str);
        int ans = 0, cur = n-1;
        while(cur >= 0) {
            while (cur>=0 && str[cur] == '+')  --cur;
            if(cur < 0)  break;
            int i = 0;
            while(i<cur && str[i]=='+')  str[i++] = '-';
            if(i > 0)  ++ans;
            int cnt = 0;
            for(int j = cur; j >= 0; j--) {
                if(str[j] == '+')
                    tmp[cnt++] = '-';
                else
                    tmp[cnt++] = '+';
            }
            for(int j = 0; j <= cur; j++)
                str[j] = tmp[j];
            ++ans;
        }
        printf("Case #%d: %d\n", Case, ans);
    }
}

int main(int argc, const char * argv[]) {
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/B-large.in", "r", stdin);
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/data.out", "w", stdout);
    solve();
    return 0;
}















