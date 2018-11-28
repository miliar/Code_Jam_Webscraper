#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int check[10];

int last_digit(int p){
    int k=p%10;
    return k;
}

bool allfound( ){
    bool ok=true;
    for(int i=0; i<10; i++){
        if(check[i]==0) ok=false;
    }
    return ok;
}

int ssearch(int x){
    int p=x, K=x;
    while(x!=0){
        check[last_digit(x)]++;
    }
}

int main( ){
    int t, N;
    scanf("%d", &t);
    for(int j=1; j<=t; j++){
        scanf("%d", &N);
        int K=0;
        if(N!=0){
            while(!allfound( )){
                K+=N;
                int p=K;
                while(K!=0){
                    int q=last_digit(K);
                    check[q]++;
                    K-=q;
                    K/=10;
                }
                K=p;
            }
            printf("Case #%d: %d\n", j, K);
        }else printf("Case #%d: INSOMNIA\n", j);
        memset(check, 0, sizeof check);
    }
    return 0;
}
