//
//  main.cpp
//  A. Counting Sheep
//
//  Created by eycia on 16/4/9.
//  Copyright © 2016年 eycia. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Volumes/data/A-small-attempt0.in", "r", stdin);
    freopen("/Volumes/data/oo", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int ff = 1; ff <= t; ff++) {
        int n, cn;
        scanf("%d", &n);
        cn = n;
        
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", ff);
            continue;
        }
        
        bool mat[10] = {false};
        int cnt = 0;
        
        while (cnt < 10) {
            long long tmp = n;
            while (tmp > 0) {
                if (!mat[tmp%10]) {
                    mat[tmp%10] = true;
                    cnt++;
                }
                tmp /= 10;
            }
            n += cn;
        }
        
        printf("Case #%d: %d\n", ff, n-cn);
    }
}
