#include<stdio.h>
int main(){
    int T, X, R, C, i;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(i=1; i<=T; i++){
        scanf("%d %d %d", &X, &R, &C);
        if(X==1) printf("Case #%d: GABRIEL\n", i);
        if(X==2 && (R*C)%2==0) printf("Case #%d: GABRIEL\n", i);
        else if(X==2) printf("Case #%d: RICHARD\n", i);
        if(X==3 && (R*C)%3==0 && R*C!=3) printf("Case #%d: GABRIEL\n", i);
        else if(X==3) printf("Case #%d: RICHARD\n", i);
        if(X==4){
            if((R*C)%4!=0 || R*C<12) printf("Case #%d: RICHARD\n", i);
            else printf("Case #%d: GABRIEL\n", i);
        }
    }
    return 0;
}
