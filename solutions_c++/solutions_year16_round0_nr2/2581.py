#include <cstdio>
#include <string.h>

int main() {
    int ncases;
    scanf("%d", &ncases);
    for(int c = 0; c < ncases; ++c) {
        char str[512];
        scanf("%512s", str);
        char lookFor = '-';
        int turns = 0;
        for(int i = 0; i < strlen(str); ++i) {
            if(str[i] == lookFor) {
                if(lookFor == '-') {
                    turns += i == 0? 1 : 2;
                    lookFor = '+';
                } else {
                    lookFor = '-';
                }
            }
        }
        printf("Case #%d: %d\n", c+1, turns);
    }
}
