#include<iostream>

int main()
{
    int T,X,R,C;
    scanf("%d",&T);
    for (int i = 0; i<T; i++) {
        scanf("%d %d %d",&X,&R,&C);
        
        if((R*C)%X != 0)
            printf("Case #%d: RICHARD\n",(i+1));
        else
        {
            if (X < 3)
                printf("Case #%d: GABRIEL\n",(i+1));
            else
                if (R*C <= X * (X-2))
                    printf("Case #%d: RICHARD\n",(i+1));
                else
                    printf("Case #%d: GABRIEL\n",(i+1));
        }
    }
    return 0;
}