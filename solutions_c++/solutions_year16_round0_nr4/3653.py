#include<stdio.h>
int main(void){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    int l;
    scanf("%i", &T);
    for(l=0;l<T;l++){
        int K; int C; int S;
        scanf("%i %i %i", &K, &C, &S);
        printf("Case #%i: ", l+1);
        int i;
        for(i=1;i<K;i++){
            printf("%i ", i);
        }
        printf("%i\n", K);
    }
    return 0;
}
