#include <stdio.h>

bool verificarfim(int c[10])
{
    int contador=0;
    bool teste;
    for(int i=0; i<10; i++)
    {
        if(c[i]==0) break;
        else if(c[i]==1) contador++;
    }
    if(contador==10) teste=true;
    else teste=false;
    return teste;
}

int main()
{
    FILE *entrada;
    FILE *saida;
    entrada=fopen("A-large.in", "r");
    saida=fopen("output.in", "w");
    int l,n,u,num;
    int cont[10] = {0,0,0,0,0,0,0,0,0,0};
    fscanf(entrada,"%d", &l);
    for(int t=1; t<=l; t++)
    {
        fscanf(entrada,"%d", &n);
        for(int i=2; 1 ; i++)
        {
            if(n==0) break;
            num = n;
            while(num!=0)
            {
                u=num%10;
                if(u==0) cont[0]=1;
                if(u==1) cont[1]=1;
                if(u==2) cont[2]=1;
                if(u==3) cont[3]=1;
                if(u==4) cont[4]=1;
                if(u==5) cont[5]=1;
                if(u==6) cont[6]=1;
                if(u==7) cont[7]=1;
                if(u==8) cont[8]=1;
                if(u==9) cont[9]=1;
                num=num/10;
            }
            if(verificarfim(cont)==true) break;
            n = n*i/(i-1);
        }
        if(n==0) fprintf(saida,"Case #%d: INSOMNIA\n",t);
        else fprintf(saida,"Case #%d: %d\n",t,n);
        for(int k=0;k<10;k++)
        {
            cont[k]=0;
        }
    }
    return 0;
}
