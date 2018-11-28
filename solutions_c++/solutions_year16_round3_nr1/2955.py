#include<cstdio>

char PA[] = {'A','B','C','D','E','F','G','H','i'};
int P[9];
int N;
void sol(int N){

    while(true){
        int max1Idx;
        int max1=0;
        int max2Idx;
        int max2=0;
        for(int i=0;i<N;i++){

            if(P[i]>max1){
                max1=P[i];
                max1Idx=i;
            }
        }
        for(int i=0;i<N;i++){
            if(P[i]>max2&&max1Idx!=i){max2=P[i];max2Idx=i;}
        }
        if(max1==0)break;
        int sum=0;
        for(int i=0;i<N;i++){
            sum+=P[i];
        }
        if(sum==3){
            for(int i=0;i<N;i++){
                if(P[i]==1){
                    printf("%c",PA[i]);
                    P[i]--;
                    break;
                }
            }
        }else if(P[max1Idx]==P[max2Idx]){
            P[max1Idx]-=1;
            P[max2Idx]-=1;
            printf("%c%c",PA[max1Idx],PA[max2Idx]);
        }
        else if(P[max1Idx]%2==0){P[max1Idx]-=2;printf("%c%c",PA[max1Idx],PA[max1Idx]);}
        else{

            if(P[max1Idx]>0){
                printf("%c",PA[max1Idx]);
                P[max1Idx]-=1;
                }
            if(P[max2Idx]>0){
                printf("%c",PA[max2Idx]);
                P[max2Idx]-=1;
            }



        }
        if(sum>2)
        printf(" ");
    }
}

void init(){

    scanf("%d",&N);
    for(int i=0;i<N;i++){
        int tmp;
        scanf("%d",&P[i]);
    }

}

int main(){

    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++){

        init();
        printf("Case #%d: ",i+1);
        sol(N);
        printf("\n");
    }
    return 0;
}
