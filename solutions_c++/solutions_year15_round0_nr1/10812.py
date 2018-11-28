#include <stdio.h>
#include <stdlib.h>

int jesimoDigito(int a, int j, int numdigits){
    int mult=1, aux;
    for(int i=1; i<=numdigits-j; i++){
        a=a/10;
    }
    aux=(a)%10;
    return aux;
}

int main(){
    // mensagem inicial na tela
    printf("Inicio do programa. \n");

    // abrir arquivos de entrada e saida
    FILE * entrada;
    entrada = fopen("C:\\GoogleCodeJam\\A-small-attempt1.in", "r");
    FILE * saida;
    saida = fopen("C:\\GoogleCodeJam\\output.txt", "w");

    int n, smax, vetor[1010];
    int a, i, j, sum, precisa;
    char hashtag='#';

    fscanf(entrada, " %d", &n);

    for(i=1; i<=n; i++){
        sum=0, precisa=0;
        fscanf(entrada, "%d %d", &smax, &a);
        for(j=0; j<=smax; j++){
            vetor[j]=jesimoDigito(a, j+1, smax+1);
            //printf("\n %d-esimo Digito=%d \n", j+1, vetor[j]);
        }
        for(j=0; j<=smax; j++){
            if(j-sum>0){
                precisa=precisa+(j-sum);
                sum=sum+(j-sum);
            }
            sum=sum+vetor[j];
           // fprintf(saida, "%d\n", precisa);
        }
        fprintf(saida, "Case %c%d: %d", hashtag, i, precisa);

        if(i!=n)
            fprintf(saida, "\n");
    }

    // fechar arquivos de entrada e saida
    fclose(entrada);
    fclose(saida);

    // mensagem final na tela + pausa
    printf("\nFim do programa. \n \n");

    // finalizar
    return 0;
}
