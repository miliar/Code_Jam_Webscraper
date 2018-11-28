#include <iostream>
#include <cstdio>
#define N 1002

int main() {
    int T;
    int s_max;
    char level[N];
    scanf("%d", &T);
    for (int cnt = 1; cnt <= T; ++cnt) {
        scanf("%d", &s_max);
        getchar();
        for (int i = 0; i < s_max + 1; ++i) {
            scanf("%c", &level[i]);
        }

        int stand_up = level[0] - '0';
        int friend_needed = 0;
        for (int i = 1; i < s_max + 1; ++i) {
            if (level[i] > '0') {
                if (stand_up < i) {
                    friend_needed += i - stand_up;
                    stand_up = i;
                }
                stand_up += level[i] - '0';
            }
        }

        printf("Case #%d: %d\n", cnt, friend_needed);
    }

}