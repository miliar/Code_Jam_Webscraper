#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    int cases, i, X, R, C, temp;

    scanf("%d ", &cases);

    for (i = 1 ; i <= cases ; i++){
        scanf("%d %d %d ", &X, &R, &C);

        if (R > C){
            temp = R;
            R = C;
            C = temp;
        }

        switch(X){
            case 1:
                printf("Case #%d: GABRIEL\n", i);
                break;
            case 2:
                if (R % 2 == 0 || C % 2 == 0)
                   printf("Case #%d: GABRIEL\n", i);
                else
                   printf("Case #%d: RICHARD\n", i);
                break;
            case 3:
                if (R == 1 || R == 4)
                   printf("Case #%d: RICHARD\n", i);
                else if (R == 3)
                    printf("Case #%d: GABRIEL\n", i);
                else if (C == 3)
                    printf("Case #%d: GABRIEL\n", i);
                else
                    printf("Case #%d: RICHARD\n", i);
                break;
            case 4:
                if (R != 4 && (R != 3 || C != 4))
                    printf("Case #%d: RICHARD\n", i);
                else
                    printf("Case #%d: GABRIEL\n", i);
        }
    }
    return 0;
}
