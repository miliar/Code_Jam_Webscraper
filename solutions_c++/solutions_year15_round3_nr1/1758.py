#include <stdio.h>

int main(){
    int TC, R, C, W, ret;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        scanf("%d %d %d", &R, &C, &W);
        //printf("Case #%d: %d\n", c, (C%W + (W-1)+C/W)*R);
        //printf("Case #%d: %d\n", c, (C/W + W)*R);
        ret = C/W + (W-1);
        if(C%W != 0) ret++;
        ret *= R;
        printf("Case #%d: %d\n", c, ret);
    }
}
