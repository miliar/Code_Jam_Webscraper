#include <cstdio>

int main() {
    int T;
    int X, R, C;
    int winner = 0;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++) {
        scanf("%d %d %d", &X, &R, &C);
        if (R > C) {
            R ^= C;
            C ^= R;
            R ^= C;
        }
        int area = R*C;
        if ((area < X) || (area) % X != 0)
            winner = 0;
        else if (X == 1)
            winner = 1;
        else if (X == 2)
            winner = 1;
        else if (X == 3 && R > 1)
            winner = 1;
        else if (X== 4 && R > 2)
            winner = 1;
        else
            winner = 0;
        
        

        if (winner == 1)
            printf("Case #%d: GABRIEL\n",i);
        else
            printf("Case #%d: RICHARD\n",i);

    }
    return 0;
}
