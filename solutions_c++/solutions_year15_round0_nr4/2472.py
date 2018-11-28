#include <cstdio>
#include <cstring>

int main(){
    freopen("Small3.in", "r", stdin);
    freopen("Small3.sol", "w", stdout);
    int k, x, R, C;
    bool win;
    scanf("%d", &k);
    for(int i = 1; i <= k; ++i){
        scanf("%d %d %d", &x, &R, &C);
        if(x == 1)
            win = 1;
        else if(x == 2){
            if(R*C % 2 == 0)
                win = 1;
            else
                win = 0;
        }
        else if(x == 3){
            if( ( R >= 3 && C >= 2 || R >=2 && C >= 3 ) && R*C % 3 == 0)
                win = 1;
            else
                win = 0;
        }
        else if(x == 4){
            if(R == 3 && C == 4 || R == 4 && C == 3 || R == 4 && C == 4)
                win = 1;
            else
                win = 0;
        }
        printf("Case #%d: ", i);
        if(win)
            printf("GABRIEL\n");
        else
            printf("RICHARD\n");
    }
    return 0;
}
/*
4
2 2 2
2 1 3
4 4 1
3 2 3
*/
