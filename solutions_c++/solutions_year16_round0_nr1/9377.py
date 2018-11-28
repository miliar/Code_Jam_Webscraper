#include<stdio.h>

int main(){
    FILE * Entrada;
    FILE * Saida;
    int num;
    Entrada = fopen("C:\\jam\\sheepin.txt", "r");
    Saida = fopen("C:\\jam\\sheepout.txt", "w");
    fscanf(Entrada,"%d",&num);
    for (int u = 1; u <= num; u++){
    int n, bol = 1, k, i, l;
    int vetor[10] = {0,0,0,0,0,0,0,0,0,0};
    fscanf(Entrada,"%d", &n);
    for(i = 1; bol && n != 0; i++){
        k = n*i;
        l = k;
        while(k){
            vetor[k%10] = 1;
            k /= 10;
        }
        bol = 0;
        for(int j = 0; j <=9 && !bol; j++)
            bol = !vetor[j];
    }
    if (!n)
        fprintf(Saida,"Case #%d: INSOMNIA\n", u);
    else fprintf(Saida,"Case #%d: %d\n", u, l);
}
    fclose(Entrada);
    fclose(Saida);
}
