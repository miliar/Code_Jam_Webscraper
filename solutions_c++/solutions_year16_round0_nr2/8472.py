//
//  main.cpp
//  Pro2
//
//  Created by dong on 4/9/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>

#define MAX_LENGTH 107

int getLength(char *s) {
    int l = 0;
    while (s[l] != '\0') {++l;}
    return l;
}

void reverse(char *s, int num) {
    char t;
    for (int k = 0; k < (num >> 1); ++k) {
        t = (s[k] == '+')?('-'):('+');
        s[k] = (s[num-1-k] == '+')?('-'):('+');
        s[num-1-k] = t;
    }
    if (num & 1) {
        s[num >> 1] = (s[num >> 1] == '+')?('-'):('+');
    }
}

int work(char *s) {
    int steps = 0;
    int i = 0, j = getLength(s);
    
    printf("length: %d\n", j);
    while (true) {
        while (j && s[j-1] == '+') {--j;}
        if (j == 0) {return steps;}
        if (s[i] == '+') {
            ++steps;
            while (i < j && s[i] == '+') {
                s[i] = '-';
                ++i;
            }
        }
        ++steps;
        if (i == j) {
            return steps;
        } else {
            reverse(s, j);
        }
        i = 0;
    }
}

int main(int argc, const char * argv[]) {
    FILE *file = fopen("Pro2.txt", "w");
    
    int T;
    scanf("%d", &T);getchar();
    
    char S[MAX_LENGTH];
    int steps;
    for (int k = 1; k <= T; ++k) {
        scanf("%s", S);
        steps = work(S);
        fprintf(file, "Case #%d: %d\n", k, steps);
    }
    
    fclose(file);
    return 0;
}
