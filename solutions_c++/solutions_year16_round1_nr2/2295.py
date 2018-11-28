//
//  main.cpp
//  Pro2
//
//  Created by dong on 4/16/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>
#include <stdio.h>

#define MAX_HEIGHT 2500

int main(int argc, const char * argv[]) {
    // insert code here...
    FILE *file = fopen("Pro2.txt", "w");
    
    int count[MAX_HEIGHT];
    int T, N;
    int tmp;
    int ans[50];
    int flag;
    for (int i = 0; i < MAX_HEIGHT; ++i) {
        count[i] = 0;
    }
    scanf("%d", &T);getchar();
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d:", t);
        scanf("%d", &N);getchar();
        printf(" %d\n", N);
        flag = 0;
        for (int i = 0; i < (N << 1) - 1; ++i) {
            for (int j = 0; j < N; ++j) {
                scanf("%d", &tmp);
                
                printf(" %d", tmp);
                ++count[tmp-1];
            }
            getchar();
            printf("\n");
        }
        for (int i = 0; i < MAX_HEIGHT; ++i) {
            if ((count[i] & 1) != 0) {
                ans[flag++] = i+1;
                printf("%d ", i+1);
                ++count[i];

            }
        }
        printf("\n");
        fprintf(file, "Case #%d:", t);
        for (int i = 0; i < flag; ++i) {
            fprintf(file, " %d", ans[i]);
        }
        fprintf(file, "\n");
    }
    
    fclose(file);
    return 0;
}
