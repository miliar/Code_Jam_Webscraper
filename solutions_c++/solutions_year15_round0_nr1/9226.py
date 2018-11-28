#include<stdio.h>
#include<string.h>

int main(){
    int num, i, saida, ma, j, pe;
    char pessoas[10000];
    scanf("%d ", &num);
    for(i = 0; i < num; i++){
        saida = 0;
        pe = 0;
        scanf("%d ", &ma);
        fgets(pessoas, 10000, stdin);
        for(j = 0; j <= ma; j++){
            if(pe >= j){
                pe += pessoas[j] - '0';
            }
            else{
                if(pessoas[j] - '0' != 0){
                    saida += j - pe;
                    pe += pessoas[j] - '0' + j - pe;
                }
            }
        }
        printf("Case #%d: %d\n", i+1, saida);
    }
    return 0;
}
