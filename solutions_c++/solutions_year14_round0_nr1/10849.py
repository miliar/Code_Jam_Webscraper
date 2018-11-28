#include <iostream>
#include <stdio.h>
using namespace std;

int main() {

int matriz[4][4];
int matriz2[4][4];
int r1linha[4];
int r2linha[4];
int ncasos;
int vez =1;
int linha;
int linha2, niguais=0, numero =0;

    scanf("%d", &ncasos);
    for(int n =1; n <=ncasos; n++){
            scanf("%d", &linha);
            linha--;

            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){
                    scanf("%d", &matriz[i][j]);
                    if(linha == i){
                        r1linha[j]=matriz[linha][j];
                    }
                }
            }
            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){

                    }
            }

            scanf("%d", &linha2);
            linha2--;

            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){
                    scanf("%d", &matriz2[i][j]);
                    if(linha == i){
                        r1linha[j]=matriz2[linha][j];
                    }
                }
            }
            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){

                    }
            }

            for(int i=0; i<4; i++){
                r1linha[i] = matriz[linha][i];
                r2linha[i] = matriz2[linha2][i];
            }
            for(int i=0; i<4; i++){
                for(int j=0; j<4; j++){
                    if (r1linha[i] == r2linha[j]){
                        niguais++;
                        numero = r1linha[i];
                    }
                }

            }
            if(niguais == 0){
                printf("Case #%d: Volunteer cheated!\n", n);
            }
            else if(niguais == 1){
                printf("Case #%d: %d\n", n, numero);
            }
            else{
                printf("Case #%d: Bad magician!\n", n);
            }
            niguais =0;
    }
    return 0;
}
