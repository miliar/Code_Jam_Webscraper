#include <stdio.h>
#include <string.h>

int main()
{
    FILE *arq;
    arq = fopen("out.txt", "w");
    int casos, troca;
    char palavra[100];
    scanf("%d", &casos);
for(int i=1;i<=casos;i++)
{
        scanf("%s", palavra);
        troca = 0;
        int a = 0, j =0;
    while(j<=strlen(palavra)-1){
        while(palavra[j] == palavra[a])
        {
            j++;
        }
        troca++;

        a = j;
    }
    if(palavra[strlen(palavra)-1] == '-') troca++;

    fprintf(arq, "Case #%d: %d\n", i, troca-1);
}

}
/*
int checarPalavra(char palavra[100])
{
    int x = 1;
    for(int i=1;i<=100;i++)
    {
        if(palavra[i] == '-')
            x = 0;
    }
    return x;
}

void sequenciarPalavra(char palavra[100], int i)
{
    if(palavra[i] == '+')
        while(palavra[i] == '+'){
            palavra[i] = '-';
            i++;
        }
    else
        while(palavra[i] == '-'){
            palavra[i] = '+';
            i++;
        }
}

int checarIndice(char palavra[100])
{
    int i=0;
    if(palavra[0] == '+')
        while(palavra[i] == '+')
            i++;
    else
        while(palavra[i] == '-')
            i++;

    return i;
}




int main()
{
    int casos;
    char palavra[100];
    scanf("%d", &casos);
    for(int i=1;i<=casos;i++)
    {
        printf("Case #%d: ", i);
        scanf("%s", palavra);
        int x = 0;
        int cont = 0;
        while(checarPalavra(palavra) == 0)
        {
           sequenciarPalavra(palavra, x);
           cont ++;
           x = checarIndice(palavra);
        }

    printf("%d\n", cont);

    }
    return 0;
}
*/
