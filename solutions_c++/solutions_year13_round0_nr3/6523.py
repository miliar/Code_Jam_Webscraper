#include<stdio.h>
#include<math.h>
using namespace std;

int main()
{
    unsigned long long I,K,L,M,N=0,Tcase,A,B,Count,X;
    double Root;
    FILE *F;
    F=fopen("D:\\Output.txt","w");
    scanf("%llu",&Tcase);
    while(Tcase--){
        Count=0;
        ++N;
        scanf("%llu %llu",&A,&B);
        for(I=A;I<=B;I++){
            K=I;
            M=0;
            while(K>0){
                L=K%10;
                M=M*10+L;
                K/=10;
            }
            //printf("%llu   %llu\n",M,I);
            if(M==I){
                //printf("here\n");
                //X=I;
                Root=sqrt ((double)M);
                M=Root;
                X=M;
                //printf("%llu    %lf\n",M,Root);
                if(M==Root){
                    //printf("here2\n");
                    L=0;
                    while(M>0){
                        L=L*10+M%10;
                        M/=10;
                    }
                    //printf(" hgh h %llu    %lf\n",X,L);
                    if(X==L) ++Count;
                }
            }
        }
        printf("Case #%llu: %llu\n",N,Count);
        fprintf(F,"Case #%llu: %llu\n",N,Count);
    }
    return 0;
}
