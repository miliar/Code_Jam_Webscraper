#include <stdio.h>

int ch[20];
void check(){

    int a, i, j, k;
    scanf("%d", &a);
    
    for (i = 1; i <= 4; i++){
        for (j = 1; j <= 4; j++){
            scanf("%d", &k);
            if (a == i) ch[k] += 1;
        }
    }
    
}
int main(){

    int T, i, m, b, C = 0;
    scanf("%d", &T);

    while (C++ != T){
    
        m = 0;
        b = 0;
        check();
        check();

        for (i = 1; i <= 16; i++){
            if (ch[i] == 2){
                b+=1;
                m = i;
            }
            ch[i] = 0;
        }

        if (b == 1){
            printf("case #%d: %d\n", C, m);
        }else if (b == 0){
            printf("case #%d: Volunteer cheated!\n", C);
        }else{
            printf("case #%d: Bad magician!\n", C);
        }

    }
    return 0;

}
