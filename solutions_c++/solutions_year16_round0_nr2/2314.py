//
// Created by Lqs on 2016/4/9.
//

#include <cstdio>
#include <cstring>

#include "io.h"

int main() {
    setInput("b.in");
    setOutput("b.out");
    char str[1000];
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int cnt = 0;
        scanf("%s", str);
        //printf("%s\n", str);
        int len = strlen(str);
        int pt = 0;
        while (pt < len) {
            char now = str[pt];
            while (pt < len && now == str[pt]) {
                pt++;
            }
            if (pt != len) {
                cnt++;
            }
        }
        printf("Case #%d: %d\n", t, cnt + (str[len-1] == '-' ? 1 : 0));
    }
}