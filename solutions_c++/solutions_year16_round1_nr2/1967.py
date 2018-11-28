//
//  main.cpp
//  B.Rank and File
//
//  Created by eycia on 16/4/16.
//  Copyright © 2016年 eycia. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int hash[2505];

void work(int ff) {
    int n, ele;
    scanf("%d", &n);
    
    memset(hash, 0, sizeof(hash));
    
    for (int i = 0; i < 2*n-1; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &ele);
            if (hash[ele] % 2) {
                hash[ele]--;
            } else {
                hash[ele]++;
            }
        }
    }
    
    printf("Case #%d: ", ff);
    
    for (int i = 1; i <= 2500; i++) {
        if (hash[i]) {
            printf("%d ", i);
        }
    }
    
    puts("");
}

int main(int argc, const char * argv[]) {
    freopen("/Users/eycia/Downloads/B-small-attempt0.in", "r", stdin);
    freopen("/Users/eycia/Downloads/b.small.out", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        work(i);
    }
}
