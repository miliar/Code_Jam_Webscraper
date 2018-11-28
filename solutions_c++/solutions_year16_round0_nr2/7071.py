//
//  main.cpp
//  d
//
//  Created by LegaDyan on 16/4/9.
//  Copyright © 2016年 LegaDyan. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        if (s == k) {
            long long sum = 1;
            for (int j = 0; j < c - 1; j++) sum *= k;
            printf("Case #%d:", i + 1);
            for (int j = 0; j < k; j++) printf(" %lld", sum * j + 1);
            cout << endl;
        }
        else {
            if (c == 1 || s < ceil(k / 2.0)) {printf("Case #%d: IMPOSSIBLE\n", i + 1);continue;}
            printf("Case #%d:", i + 1);
            long long sum = 1;
            for (int j = 0; j < c - 1; j++) sum *= k;
            for (int j = 0; j < k; j += 2) printf(" %lld", sum * j + j + 2);
            printf(" %lld", sum * (k - 1) + 1);
            cout << endl;
        }
    }
    return 0;
}
