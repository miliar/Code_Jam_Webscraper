#include <stdio.h>
#include <string.h>

int main(){
    char vet[101];
    int t, i, j, tam, contador = 0, vai = 1;

    scanf("%d", &t);

    for(i = 1; i <= t; ++i){
        scanf(" %s", vet);
        tam = strlen(vet);

        for(j = 0; j < tam; j++){
            if(vet[j] == '-' && vai == 1){
                if(j == 0)
                    contador++;
                else
                    contador += 2;
                vai = 0;

            }
            if(vai == 0 && vet[j] == '+'){
                vai = 1;
            }
        }

        printf("Case #%d: %d\n", i, contador);
        contador = 0;
        vai = 1;
    }
    return 0;
}
