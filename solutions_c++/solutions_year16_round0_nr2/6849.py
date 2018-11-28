#include <stdio.h>
#include <string.h>

bool allPlus(char line[], int len) {
    for(int i = 0; i < len; i++) {
        if(line[i] == '-') {
            return false;
        }
    }
    return true;
}

long flipCount(char line[], int len) {
    long fcount = 0;
    while(!allPlus(line, len)) {
        if(line[0] == '-') {
            int i = 0;
            while(line[i] == '-') {
                line[i++] = '+';
            }
        } else {
            int i = 0;
            while(line[i] == '+') {
                line[i++] = '-';
            }
        }
        fcount++;
    }
    return fcount;
}

int main()
{
    char line[102];
    int len, T, t;
    scanf("%d", &T);
    for(t = 1; t <= T; t++) {
        scanf("%s", line);
        len = strlen(line);
        printf("Case #%d: %ld\n", t, flipCount(line, len));
    }
    return 0;
}
