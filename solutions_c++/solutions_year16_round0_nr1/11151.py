#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {

    long long N,i,numero,completou,multiplicador,cont,avaliar,resto;


    FILE * entrada;
    FILE * saida;
    entrada = fopen ("entradacontest2.in","r");
    saida = fopen ("saidacontest.txt","w");

    fscanf(entrada,"%lld",&N);

    for(i=0;i<N;i++){

        fscanf(entrada,"%lld",&numero);

        int numeros[10];
		memset(numeros, 0, sizeof(numeros));

		if(numero==0)
            fprintf(saida,"Case #%lld: INSOMNIA\n",i+1);
        else{
            multiplicador = 0;
            completou = 0;
            cont = 0;
            while(!completou){
                multiplicador++;
                avaliar = numero * multiplicador;
                while(avaliar/10!=0 || avaliar%10!=0){
                    resto = avaliar % 10;
                    if(numeros[resto]==0){
                        numeros[resto] = 1;
                        cont++;

                    }
                    avaliar = avaliar/10;
                }
                if(cont==10)
                    completou=1;

            }

            fprintf(saida,"Case #%lld: %lld\n",i+1,multiplicador*numero);
        }
    }

    return 0;
}
