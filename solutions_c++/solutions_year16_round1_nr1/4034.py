//
//  main.cpp
//  round1A
//
//  Created by zhangshuijie on 16/4/16.
//  Copyright © 2016年 zhangshuijie. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

char str[1100];

int main()
{
    freopen("/Users/zhangshuijie/Desktop/round1A/round1A/A-large.in-2.txt", "r", stdin);
    freopen("/Users/zhangshuijie/Desktop/round1A/round1A/A-large.out-2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca++) {
        scanf("%s", str);
        int len = strlen(str);
        char ans[1100];
        memset(ans, 0, sizeof(ans));
        ans[0] = str[0];
        for (int i = 1; i < len; i++) {
            if (str[i] >= ans[0]) {
                for (int j = strlen(ans); j >= 0; j--) {
                    ans[j+1] = ans[j];
                }
                ans[0] = str[i];
            } else {
                ans[strlen(ans)] = str[i];
            }
        }
        printf("Case #%d: %s\n", ca, ans);
    }
    return 0;
}
