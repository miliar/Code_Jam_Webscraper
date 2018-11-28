#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
    int n, x, i, j, toInvite, stood, charToInt;
    scanf("%d", &n);
    for(i = 1; i <= n; i++) {
        if(i != 1)
            puts("");
        char ent[1002];
        scanf("%d", &x);
        scanf("%s", ent);
        toInvite = 0, stood = 0;
        //printf("%s\n", ent);
        for(j = 0; j < strlen(ent); j++) {
            charToInt = ent[j] - '0';
            //printf("%d %d %d\n", stood, j, charToInt);
            if(stood >= j)
                stood += charToInt;
            else if(charToInt) {
                toInvite += (j - stood);
                stood += charToInt + toInvite;
            }
        }
        printf("Case #%d: %d", i, toInvite);
    }
    return 0;
}



