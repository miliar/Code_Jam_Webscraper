#include <bits/stdc++.h>
using namespace std;

FILE *in;
FILE *out;

int T, bloques, paridad, resp;
char arr[1100];

void convertir(){
    bloques=0,paridad=0,resp=0;
    int ant,act;
    if(arr[0]=='-'){
        ant=1;
        paridad=1;
    }
    else{
        ant=0;
        paridad=0;
    }
    bloques=1;
    for(int i=1; i<strlen(arr); i++){
        if(arr[i]=='-')
            act=1;
        else
            act=0;
        if(ant!=act){
            ant=act;
            bloques++;
        }
    }
}

int main(){
    in = fopen("in.in","r");
    out = fopen("out.txt","w");

    fscanf(in,"%d",&T);
    for(int t=1; t<=T; t++){
        bloques =0, resp=0, paridad=0;
        fscanf(in,"%s",arr);
        convertir();
        //printf("[Bloques: %d Paridad:%d]\n",bloques,paridad);
        if(paridad==1 && bloques%2==1)
            resp=bloques;
        else if(paridad==1 && bloques%2==0)
            resp=bloques-1;
        else if(paridad==0 && bloques%2==0)
            resp=bloques;
        else
            resp=bloques-1;
        fprintf(out,"Case #%d: %d\n",t,resp);
    }
}
