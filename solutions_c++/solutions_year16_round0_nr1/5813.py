#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int a[20];
int tam=0;

void pegarn(long long int x){
    int alga;
    for(int k=0; k<tam;k++){
        alga=x%10;
        a[alga]=1;
        x=x/10;
    }

}

int main(){
    int t;
    scanf("%d", &t);
    int teste=1;
    for(int i=0;i<t;i++){
        for(int j=0;j<20;j++)
            a[j]=0;
        long long int resp=0;
        int casoi=1;
        int sum=0;

        long long int n;
        scanf("%lld", &n);

        if(n==0)
            printf("Case #%d: INSOMNIA\n", teste);

        else{
            while(sum!=10){
                int sub=n*casoi;
                sum=0;
                tam=0;
                tam= log10(sub);
                tam+=1;
               // printf("%d", tam);
                pegarn(sub);

                for(int j=0;j<10;j++){
                    sum+=a[j];
                }

                if(sum==10){
                    resp=sub;
                    break;
                }
                casoi++;

            }

            printf("Case #%d: %lld\n", teste, resp);
        }
        teste++;
    }

    return 0;
}
