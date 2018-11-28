#include <stdio.h>
int main(int argc, char const *argv[])
{
    int i, t, x, r, c;
    scanf("%d", &t);
    for (i=1; i<=t; i++){
        scanf("%d%d%d", &x, &r, &c);
        /*if (r*c <= x){
            printf("Case #%d: RICHARD\n", i);
        }else{*/
            if (x == 4){
                if (r*c%4 == 0 && r>2 && c>2){
                    printf("Case #%d: GABRIEL\n", i);
                }else{
                    printf("Case #%d: RICHARD\n", i);        
                }
            }else if (x == 3){
                if (r*c%3 == 0 && r*c>3){
                    printf("Case #%d: GABRIEL\n", i);
                }else{
                    printf("Case #%d: RICHARD\n", i);        
                }   
            }
            else if ((r*c)%x == 0){
                printf("Case #%d: GABRIEL\n", i);
            }else{
                printf("Case #%d: RICHARD\n", i);
            }
        //}
    }
    return 0;
}