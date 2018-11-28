//
//  main.cpp
//  gcj02
//
//  Created by 黄浩然 on 15/4/11.
//  Copyright (c) 2015年 Haoran Huang. All rights reserved.
//

#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    freopen("B-large.in.txt","r",stdin);
    scanf("%d", &t);
    int test = 0;
    while (test < t) {
        int d;
        scanf("%d", &d);
        int p[1001];
        int max = 0;
        for (int i = 0; i < d; i++) {
            scanf("%d", &p[i]);
            if (p[i] > max) {
                max = p[i];
            }
        }
        int min = max;
        int cur = 0;
        for (int i = 1; i <= max; i++) {
            cur = i;
            for (int j = 0; j < d; j++) {
                if( p[j] > i ) {
                    if( p[j] % i == 0 )
                        cur += p[j] / i - 1;
                    else
                        cur += p[j] / i;
                }
            }
            if (min > cur) {
                min = cur;
            }
        }
        test++;
        printf("Case #%d: %d\n", test, min);
    }
    return 0;
}
