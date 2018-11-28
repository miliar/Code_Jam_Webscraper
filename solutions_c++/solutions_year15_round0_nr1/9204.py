#include <stdio.h>

int main(void){
    int T; //number of tests
    int smax; //maximum Si
    int cont = 0; //counter
    int extra = 0, result = 0; //extra friends needed
    int i = 0, j = 0;
    char s[1010];
    scanf("%d", &T);
    for(i = 1;i <= T;i++){
        scanf("%d", &smax);
        scanf("%s", s);
        for(j = 0;j < smax;j++){
            cont = cont + s[j] - '0';
            extra = 0;
            while(cont < j+1){
                extra++;
                cont = cont + extra;
                result++;
            }
        }
        printf("Case #%d: %d\n", i, result);
        cont = 0;
        extra = 0;
        result = 0;
    }
    return 0;
}
