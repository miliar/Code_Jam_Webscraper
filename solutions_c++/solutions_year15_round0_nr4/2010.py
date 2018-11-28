#include <stdio.h>

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("outD.txt", "w+", stdout);
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;t++) {
        int X,R,C;
        scanf("%d%d%d", &X, &R, &C);
        if(((R*C)%X)!=0)  printf("Case #%d: RICHARD\n", t);
        else {
            if(X==1 || X==2)    printf("Case #%d: GABRIEL\n", t);
            else if((X==3 && R*C==3)||(X==4 && !((R>2 && C==4)||(R==4 && C>2)))) printf("Case #%d: RICHARD\n", t);
            else printf("Case #%d: GABRIEL\n", t);
        }
    }

    return 0;
}
