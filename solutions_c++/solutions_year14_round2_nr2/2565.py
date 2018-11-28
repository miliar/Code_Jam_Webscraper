#include<stdio.h>

int main()
{
    int I,K,L,M,N,Tcase;
    FILE *F;
    F=fopen("D://Out.txt","w");

    scanf("%d",&Tcase);

    for(I=1;I<=Tcase;I++){
        scanf("%d %d %d",&L,&M,&N);
        long Ans=0;
        for(K=0;K<L;K++){
            for(int Z=0;Z<M;Z++){
                int X=K&Z;
                if(X<N)  ++Ans;
                //printf("%d %d %d %d\n",K,Z,K&Z,N);
            }
                //printf("\n");
        }
        fprintf(F,"Case #%d: %ld\n",I,Ans);
    }

    return 0;
}
