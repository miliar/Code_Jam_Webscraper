#include<stdio.h>

int main()
{
    int Tcase,I;
    double K,L,M,N,C,F,X,A,B;
    FILE *F1;
    F1=fopen("D:\\Out.txt","w");

    scanf("%d",&Tcase);
    for(I=1;I<=Tcase;I++){
        scanf("%lf %lf %lf",&C,&F,&X);
        N=2.0;M=0.0,K=0.0;
        while(true){
            A=C/N;
            B=N+F;
            A+=X/B;
            B=X/N;
            if(A<B){
                K+=C/N;
                N+=F;
            }
            else{
                K+=B;
                break;
            }

        }
        fprintf(F1,"Case #%d: %0.7lf\n",I,K);

    }
    return 0;
}
