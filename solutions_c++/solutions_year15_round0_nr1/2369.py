//
//  main.cpp
//  gcj01
//
//  Created by 黄浩然 on 15/4/11.
//  Copyright (c) 2015年 Haoran Huang. All rights reserved.
//

#include <iostream>
#include <cstdio>
using namespace::std;

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d",&t);
    int test = 0;
    while (test < t) {
        int max_s,s;
        scanf("%d",&max_s);
        getchar();
        char c;
        int count = 0, guide = 0;
        for (int i = 0; i <= max_s; i++) {
            c = getchar();
            s = c - '0';
            if (count >= i) {
                count += s;
            } else if (s != 0){
                int temp = i - count;
                guide += temp;
                count += s + temp;
            }
        }
        printf("Case #%d: %d\n", test+1, guide);
        test++;
    }
    return 0;
}
