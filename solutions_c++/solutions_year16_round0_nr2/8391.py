#include <stdio.h>

int main()
{
    int contador=0;
    int l;
    char panqueca[105];
    char sinal1,sinal2;
    FILE *entrada;
    entrada=fopen("B-large.in", "r");
    FILE *saida;
    saida=fopen("output.in", "w");
    fscanf(entrada,"%d", &l);
    for(int i=1;i<=l;i++)
    {
        fscanf(entrada,"%s", &panqueca);
        for(int k=0; 1; k++)
        {
            sinal1=panqueca[k];
            sinal2=panqueca[k+1];
            if(panqueca[k+1]=='\0') break;
            if(sinal1!=sinal2) contador++;
        }
        if(sinal1=='-') contador++;
        fprintf(saida,"Case #%d: %d\n", i, contador);
        contador =0;
    }
    return 0;
}
