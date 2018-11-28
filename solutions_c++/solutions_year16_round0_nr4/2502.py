#include <cstdio>

unsigned long long pow(int K,int C){
    int i;
    unsigned long long ret=K;
    for(i=1;i<C;i++){
        ret *= K;
    }
    return ret;
}

void Test(){
    int i,K,C,S;
    unsigned long long ans;
    scanf("%d%d%d",&K,&C,&S);
    if(C==1){
        if(S == K){
            for(i=1;i<=K;i++){
                printf("%d ",i);
            }
        }
        else{
            printf("IMPOSSIBLE");
        }
    }
    else if(1<C){
        if(S<K-2){
            printf("IMPOSSIBLE");
        }
        else{
            printf("2 ");
            S--;
            ans = (unsigned long long)pow(K,C);
            ans--;
            while(S--){
                printf("%lld ",ans--);
            }
        }
    }
    printf("\n");
}

int main(){
    int i,T;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        printf("Case #%d: ",i);
        Test();
    }
}