//
//  main.cpp
//  A.The Last Word
//
//  Created by eycia on 16/4/16.
//  Copyright © 2016年 eycia. All rights reserved.
//

#include <cstdio>
#include <cstring>

char buf[1024];
char result[2048];

void work(int ff) {
    scanf("%s", buf);
    int l, r;
    l = r = 1024;
    size_t sl = strlen(buf);
    
    result[l] = buf[0];
    for (int i = 1; i < sl; i++) {
        if (buf[i] >= result[l]) {
            result[--l] = buf[i];
        } else {
            result[++r] = buf[i];
        }
    }
    result[++r] = '\0';
    printf("Case #%d: %s\n", ff, result+l);
}

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int ff = 1; ff <= t; ff++) {
        work(ff);
    }
}
