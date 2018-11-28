#include <iostream>
#include <stdio.h>
using namespace std;

bool ver(bool arre[10]){
    for(int i=0;i<=9;i++)
        if(!arre[i])
            return true;
    return false; ///si todos son false, retorna false
}

int digitos(long long int x){
    long long int pot=10;
    int j=1;
    while(x>=pot){
        pot*=10;
        j++;
    }
    return j;
}

int main()
{
    int t,i,digi,j,lim,p;
    long long int n,n2;
    bool arre[10];

    FILE *archi=fopen("output.out","wt");

    FILE *lee=fopen("lee.in","rt");

    fscanf(lee,"%d",&t);
    for(i=1;i<=t;i++){
        for(j=0;j<=9;j++)
            arre[j]=false;

        fscanf(lee,"%d",&p);
        n2=p;
        lim=1;
        n=n2;
        do{
            digi=digitos(n);
            for(j=1;j<=digi;j++){
                arre[n%10]=true;
                n/=10;
            }
            lim++;
            n=n2*lim;
            if(lim==100001)
                break;
        }while(ver(arre));
        if(lim==100001){
            fprintf(archi,"Case #%d: INSOMNIA\n",i);
        }else{
            fprintf(archi,"Case #%d: %lld\n",i,n-n2);
        }
    }
    fclose(archi);
    fclose(lee);
    return 0;
}
