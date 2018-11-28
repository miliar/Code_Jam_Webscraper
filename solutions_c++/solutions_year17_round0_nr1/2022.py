//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by 张天尧 on 2017/4/8.
//  Copyright © 2017年 张天尧. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    freopen("/Users/zty/Downloads/A-large.in", "r", stdin);
    freopen("/Users/zty/Downloads/A-large.txt", "w", stdout);
    int n, d;
    const int maxn = 1000 + 10;
    char ch[maxn];
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%s", ch);
        scanf("%d", &d);
        int len = strlen(ch);
        int ans = 0;
        for (int j = 0; j <= len - d; j++) {
            if (ch[j] == '-') {
                ch[j] = '+';
                ans++;
                for (int k = 1; k < d; k++) {
                    if (ch[j + k] == '-') {
                        ch[j + k] = '+';
                    } else {
                        ch[j + k] = '-';
                    }
                }
            }
        }
        bool flag = true;
        for (int j = 1; j < d && flag; j++) {
            if (ch[len - j] == '-') {
                flag = false;
            }
        }
        printf("Case #%d: ", i);
        if (flag) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
