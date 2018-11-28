//
//  main.cpp
//  b
//
//  Created by Zhu Haifan on 14-4-12.
//  Copyright (c) 2014年 Zhu Haifan. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])
{
    freopen("/Users/whshev/Dropbox/Programs/GCJ2014/Data/QR/B-large.in", "r", stdin);
    freopen("/Users/whshev/Dropbox/Programs/GCJ2014/Data/QR/B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        double c, f, x, t = 0.0l, v = 2.0l, eps = 1e-9;
        scanf("%lf%lf%lf", &c, &f, &x);
        while (true) {
            if (x / v + eps < c / v + x / (v + f)) {
                t += x / v;
                break;
            } else {
                t += c / v;
                v += f;
            }
        }
        printf("Case #%d: %.7lf\n", i, t);
    }
    return 0;
}

