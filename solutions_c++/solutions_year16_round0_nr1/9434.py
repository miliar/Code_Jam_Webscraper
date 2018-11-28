#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int verifica(int arreglo[]){
    for(int i =0;i<10;i++){
        if(!arreglo[i])return 0;
    }
    return 1;
}


int main(){
    int casos,N;
    int arreglo[10]={0,0,0,0,0,0,0,0,0,0};
    scanf("%d",&casos);
    int cont =1;
     //18446744073709551615
     unsigned long long K;
    while(casos--){
        scanf("%d",&N);
        for(int i =0;i<10;i++)arreglo[i]=0;
        int i=1;
        for(unsigned long long a =0;a<18446744073709551615&&i<100000;a++,i++){
            K=N*(i);
            for(;K;K/=10)
                arreglo[(K%10)]++;

            if(verifica(arreglo)){
                break;
                }
        }
        printf("Case #%d: ",cont++);
        if(i>=100000)
            cout<<"INSOMNIA\n";
        else
            cout<<((i)*N)<<endl;
    }
    return 0;
}
