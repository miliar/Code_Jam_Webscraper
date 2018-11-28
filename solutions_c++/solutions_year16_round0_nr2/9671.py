#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    FILE *entrada;
    FILE *saida;
    entrada=fopen("B-large.in", "r");    ///  + = 43
    saida=fopen("output.in", "w");                ///  - = 45

    int n, ma, cont=0;

    fscanf(entrada,"%d", &n);
    //scanf("%d", &n);
    for(int k=1; k<=n; k++)
    {
        char pan[101];
        fscanf(entrada,"%s", pan);
        //scanf("%s", pan);
        cont=0;

        for(int i=0; i<strlen(pan) ; i++)
        {
            if(pan[i]==45 && pan[i+1]==43)
            {
                for (int v=0; v<=i; v++)
                {
                    pan[v]=43;
                    ma=i+1;
                }
                cont++;
            }
            else if(pan[i]==43 && pan[i+1]==45)
            {
                for (int v=0; v<=i; v++)
                {
                    pan[v]=45;
                    ma=i+1;
                }
                cont++;
            }
        }
        if(pan[0]==45)
        {
            for (int v=0; v<=ma; v++)
            {
                pan[v]=43;
            }
            cont++;
        }
        fprintf(saida,"Case #%d: %d\n",k, cont);
        //printf("Case #%d: %d\n",k, cont);
        cont=0;
    }


}
