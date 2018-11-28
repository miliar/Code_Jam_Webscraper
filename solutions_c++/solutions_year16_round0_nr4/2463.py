#include <stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d: ", i+1);
        for(int i=1; i<=K; i++) printf("%d ", i);
        printf("\n");
    }
}