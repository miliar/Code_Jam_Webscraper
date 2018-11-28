#include <stdio.h>
#include <string.h>

#define MAX 112

int main(void){
    int t, moves, caso = 1, i, j;
    char s[MAX];

    scanf("%d",&t);
    while(t--){
        scanf("%s", s);
        moves = 0;
        for(i = strlen(s) - 1; i >= 0; i--){
            if(s[i] == '-'){
                for(j = i; j >= 0; j--) s[j] = s[j] == '-' ? '+' : '-';
                moves++;
            }
        }
        printf("Case #%d: %d\n",caso++, moves);
    }
    return 0;
}
