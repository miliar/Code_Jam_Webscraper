#include <stdio.h>
#include <string.h>

// assume + or - only
void flip(char *cakes, int startIdx, int endIdx){
    for (int i = startIdx; i <= endIdx; i++){
        cakes[i] = (cakes[i] == '+') ? '-' : '+';
    }
}

int check(char *cakes){
    int attempt = 0;
    int end = 0;

    // special case with only one cake
    if (strlen(cakes) == 1){
        return (cakes[0] == '+') ? 0 : 1;
    }

    while (!end){
        // i hope it will be end if all cake are either + or - 
        end = 1;

        for (int i = 0; i < strlen(cakes) - 1; i++){
            // sosad it is nto end
            // end = end && (cakes[i] == '+') && (cakes[i + 1] == '+');

            if (cakes[i] != cakes[i + 1]){
                flip(cakes, 0, i);
                attempt++;
                end = 0;
            }
        }

    }

    // flip final round if they are - 
    if (cakes[0] == '-'){
        attempt++;
    }

    return attempt;
}

// greedy ?
int main(void){
    int T;
    char cakes [100 + 10];
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++){
        scanf("%s", cakes);
        int attempt = check(cakes);
        printf("Case #%d: %d\n", (i + 1), attempt);
    }

    return 0;
}
