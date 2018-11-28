//
// Created by 金宇超 on 16/4/9.
//

#include <iostream>

/*
5
-
-+
+-
+++
--+-

Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3

 */

int main() {
    int T;
    FILE* f=fopen("./B-large.in","r");
    FILE* o=fopen("./small.out","w");
    fscanf(f,"%d",&T);
    for(int i=0; i<T+1; i++) {
        int a, b;
        a = 0;
        b = 0;
        char p;
        p = fgetc(f);
        while (p == '+' || p == '-') {
            if (p == '+') {
                a = std::min(a, b + 1);
                b = a + 1;
            } else {
                b = std::min(b, a + 1);
                a = b + 1;
            }
            p = (char) fgetc(f);
        }
        if (i == 0) continue;
        printf("Case #%d: %d\n", i, std::min(a, b + 1));
        fprintf(o, "Case #%d: %d\n", i, std::min(a, b + 1));
    }
}