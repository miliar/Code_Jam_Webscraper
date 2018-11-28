#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main(){
    int runs, X, R, C, i, j, grid;
    scanf("%d", &runs);
    for(j=1; j<=runs; j++){
        scanf("%d %d %d", &X, &R, &C);
        grid = R*C;
        switch (X){
            case 1: printf("Case #%d: GABRIEL\n", j);
                    break;

            case 2: if(grid%2 == 0)
                        printf("Case #%d: GABRIEL\n", j);
                    else
                        printf("Case #%d: RICHARD\n", j);
                    break;

            case 3: if( (min(R,C) >=2) && (grid%3 == 0) )
                        printf("Case #%d: GABRIEL\n", j);
                    else
                        printf("Case #%d: RICHARD\n", j);
                    break;

            case 4: if( (min(R,C) >=3) && (grid%4 == 0) )
                        printf("Case #%d: GABRIEL\n", j);
                    else
                        printf("Case #%d: RICHARD\n", j);
                    break;
        }
    }
    return 0;
}
