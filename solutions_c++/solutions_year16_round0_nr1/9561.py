#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
    para colocar arquivo de entrada e de saida basta encrever
    FILE *entrada;
    FILE *saida;
    entrada=fopen("A-small-attempt0.in", "r");
    saida=fopen("output.in", "w");

    e durente o codigo, todo scanf(""), voce trocar por fscanf(entrada,"")
    e durente o codigo, todo printf(""), voce trocar por fprintf(saida,"")

    */

    FILE *entrada;
    FILE *saida;
    entrada=fopen("A-large.in", "r");
    saida=fopen("output.in", "w");

    int x=0, num, i=1;
    long long n;
    int x0=0,x1=0,x2=0,x3=0,x4=0,x5=0,x6=0,x7=0,x8=0,x9=0, aux, aux1;
    int b=0, j=2;

    fflush(stdin);
    fscanf(entrada,"%d", &num);
    for(i; i<=num; i++)
    {

    x0=0;x1=0;x2=0;x3=0;x4=0;x5=0;x6=0;x7=0;x8=0;x9=0;
    b=0; j=2;

    fflush(stdin);
    fscanf(entrada,"%d", &n);

    aux1=n;

    for(int b=0; b>=0; b++)
    {

    if(n==0)
    {
        fprintf(saida,"Case #%d: INSOMNIA\n", i);
        break;
    }
    else
    {
    aux=n;
    while(aux>0)
    {
    x=aux%10;
    aux=aux/10;

    if(x==0)
        x0=1;
    else if(x==1)
        x1=1;
    else if(x==2)
        x2=1;
    else if(x==3)
        x3=1;
    else if(x==4)
        x4=1;
    else if(x==5)
        x5=1;
    else if(x==6)
        x6=1;
    else if(x==7)
        x7=1;
    else if(x==8)
        x8=1;
    else if(x==9)
        x9=1;
    }
    }

    if(x1==1 && x2==1 && x3==1 && x4==1 && x5==1 && x6==1 && x7==1 && x8==1 && x9==1 && x0==1)
        {
            fprintf(saida,"Case #%d: %d\n", i, n);
            break;
        }

    n=aux1*j;
    j++;

    }
    }


return 0;
}
