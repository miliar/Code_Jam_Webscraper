//
//  main.cpp
//  Pro1
//
//  Created by dong on 4/9/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>
#include <stdio.h>

int work(int N) {
    if (N == 0) {
        return -1;
    }
    
    bool hasDigit[10];
    for (int i = 0; i < 10; ++i) {
        hasDigit[i] = false;
    }
    
    int tmp;
    bool ok;
    for (int i = 1;;++i) {
        tmp = N * i;
        ok = true;
        while (tmp) {
            hasDigit[tmp % 10] = true;
            tmp /= 10;
        }
        for (int j = 0; j < 10; ++j) {
            if (!hasDigit[j]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return N * i;
        }
    }
    
}

int main(int argc, const char * argv[]) {
    FILE *file = fopen("Pro1.txt", "w");
    
    int T, N;
    scanf("%d", &T);getchar();
    
    int res;
    for (int k = 1; k <= T; ++k) {
        scanf("%d", &N);getchar();
        res = work(N);
        if (res != -1) {
            fprintf(file, "Case #%d: %d\n", k, res);
        } else {
            fprintf(file, "Case #%d: INSOMNIA\n", k);
        }
    }
    
    fclose(file);
    
}
