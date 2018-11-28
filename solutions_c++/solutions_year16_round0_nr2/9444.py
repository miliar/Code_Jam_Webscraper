#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int t;
    int att;
    char s[100];
    scanf("%d", &t);

    for(int i = 0; i < t; ++i) {
        att = 0;
        scanf("%s", s);

        for(int j = strlen(s) - 1; j >= 0; --j) {
            if(s[j] == '-') {
                att++;
                for(int k = 0; k <= j; ++k) {
                    if(s[k] == '-') {
                        s[k] = '+';
                    } else {
                        s[k] = '-';
                    }
                }
            }
        }

        printf("Case #%d: %d\n", i + 1, att);
    }

    return 0;
}
