#include <cstdio>

char stack[120];

int main() {
    int T;

    scanf("%d", &T);
    for (int kase = 1; kase <=T; kase ++) {
        scanf("%s", stack);
        int flip = 0;
        int index = 1;
        for (; stack[index] != '\0'; index++) {
            if (stack[index] != stack[index-1]) {
                flip ++;
            }
        }
        if (stack[index-1] == '-') {
            flip ++;
        }
        printf("Case #%d: %d\n", kase, flip);
    }

    return 0;
}
