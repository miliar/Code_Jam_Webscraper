#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    int Tcase,I,K,L,M,N,R,W,C,D;
    FILE *F;
    F=fopen("D:\\Out.txt","w");
    float A[1009],B[1009];
    scanf("%d",&Tcase);

    for(I=1;I<=Tcase;I++){
        scanf("%d",&N);

        for(K=0;K<N;K++)
            scanf("%f",&A[K]);

            if(N>1)
            sort(A,A+N);
        for(K=0;K<N;K++)
            scanf("%f",&B[K]);
            if(N>1)
            sort(B,B+N);
        R=0;W=0;
        if(N==1){
            if(A[0]>B[0]) ++R;
            W=R;
            fprintf(F,"Case #%d: %d %d\n",I,W,R);
        }
        else{
            C=0;D=N-1;
            for(K=0;K<N;K++){
                for(L=C;L<N;L++){
                    if(A[K]<B[L]){
                        C=L+1;
                        R++;
                        break;
                    }
                }
            }
            for(K=N-1;K>=0;K--){
                for(L=D;L>=0;L--){
                    //printf("%f %f %d\n",A[K],B[K],D);
                    if(A[K]>B[L]){
                        //printf("%f %f\n",A[K],B[K]);
                        D=L-1;
                        W++;
                        break;
                    }
                }
            }
            fprintf(F,"Case #%d: %d %d\n",I,W,N-R);
        }

    }
    return 0;

}
