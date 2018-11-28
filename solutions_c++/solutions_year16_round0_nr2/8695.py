#include <stdio.h>
#include <string.h>

int main()
{
    int t, mov;
    int len;
    char s[112];
    int i, j;

    scanf("%d", &t);
    for(i=1; i<=t; i++){

        scanf("%s", s);
        len = strlen(s)-1;

        mov = 0;
        for(j=0; j<len; j++){
            if(s[j] != s[j+1]){
                mov++;
            }
        }
        if(s[len] == '-'){
            mov++;
        }
        printf("Case #%d: %d\n", i, mov);
    }

    return 0;
}
