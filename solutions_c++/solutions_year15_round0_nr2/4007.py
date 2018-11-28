#include<stdio.h>
int P[110000];
int min;
void Function(int N, int M){
    int i, j, max=1;
    if(min<=M) return;
    for(i=1; i<=N; i++) if(P[i]>0) break;
    if(i>N){
        if(M<min) min=M;
        return;
    }
    for(i=2; i<=N; i++) if(P[max]<P[i]) max=i;
    if(P[max]>3){
        for(j=1; j<=P[max]/2; j++){
            P[N+1]=j;
            P[max]-=j;
            Function(N+1, M+1);
            P[max]+=j;
        }
    }
    for(i=1; i<=N; i++) P[i]--;
    Function(N, M+1);
    for(i=1; i<=N; i++) P[i]++;
}
int main(){
    int T, D, i, j;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(i=1; i<=T; i++){
        scanf("%d", &D);
        for(j=1; j<=D; j++) scanf("%d", &P[j]);
        min=9;
        Function(D, 0);
        printf("Case #%d: %d\n", i, min);
    }
    return 0;
}
