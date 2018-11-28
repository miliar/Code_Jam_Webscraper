#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int Posiciones(char cad[]){
    char a = cad[0];
    int i =0;
    for(;cad[i];i++)
        if(cad[i]!=a)break;
    return i;
}

int verifica(char cad[]){
    for(int i =0;cad[i];i++)
        if(cad[i]!='+')
            return 0;
    return 1;
}

int main(){
    char pan[105];
    char respl[105];
    int casos, contador=1,resultado,pos;
    scanf("%d",&casos);
    while(casos--){
        scanf("%s",&pan);
        resultado=0;
        while(!verifica(pan)){
            pos=Posiciones(pan);
            for(int i =0,o=pos-1;i<pos;i++,o--)
                respl[o]=pan[i];
            for(int i =0,o=pos-1;i<pos;i++,o--)
                pan[i]=(respl[o]=='-'?'+':'-');
            resultado++;
        }
        printf("Case #%d: %d\n",contador++,resultado);
    }
    return 0;
}
