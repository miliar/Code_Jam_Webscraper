//
//  main.cpp
//  gcj04
//
//  Created by 黄浩然 on 15/4/12.
//  Copyright (c) 2015年 Haoran Huang. All rights reserved.
//

#include <iostream>
#include <cstdio>
using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    int test = 0;
    while (test < t) {
        bool isRi;
        test++;
        int X, R, C;
        scanf("%d%d%d", &X, &R, &C);
        if (X == 1) {
            isRi = false;
        } else if (X == 2) {
            if ((R * C) % 2 == 0) {
                isRi = false;
            } else {
                isRi = true;
            }
        } else if (X == 3) {
            if ((R * C) % 3 == 0) {
                if (R < 2 || C < 2) {
                    isRi = true;
                } else {
                    isRi = false;
                }

            } else {
                isRi = true;
            }
        } else if (X == 4) {
            if ((R * C) % 4 == 0) {
                if (R < 3 || C < 3) {
                    isRi = true;
                } else {
                    isRi = false;
                }
            } else {
                isRi = true;
            }
        }
        
        if (isRi) {
            printf("Case #%d: RICHARD\n",test);
        } else {
            printf("Case #%d: GABRIEL\n",test);
        }
    }
    return 0;
}
