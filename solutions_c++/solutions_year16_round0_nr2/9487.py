#include<stdio.h>


int main(){
    FILE * Entrada;
    FILE * Saida;
    int num;
    Entrada = fopen("C:\\jam\\panin.txt", "r");
    Saida = fopen("C:\\jam\\panout.txt", "w");
    fscanf(Entrada,"%d",&num);
    for (int u = 1; u <= num; u++){
    char pan[101];
    char c;
    int i = 0, j = 0, k, cont = 0;
    fscanf(Entrada,"%s", pan);
    do {
        c = pan[i];
        i++;
        if (c == pan[i])
            j++;
        else {
            cont++;
            for (k = 0; k <= j; k++)
                pan[k] = pan[i];
            i = 0;
            j = 0;
        }
    }while(pan[i] != '\0');
    if (c == '-')
        cont++;
    fprintf(Saida, "Case #%d: %d\n",u ,cont-1);
    }
}
