#include <stdio.h>
#include <stdlib.h>
int T,X,Y;


int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for (int tt = 1 ; tt<= T ; tt++){
        scanf("%d %d",&X,&Y);
        printf("Case #%d: ",tt);
        if (X > 0) {
            for (;X > 0; X--) {
                printf("WE");
            }
        } else if (X < 0){
            for (; X < 0 ; X++) {
                printf("EW");
            }
        }
        if (Y > 0) {
            for (;Y > 0; Y--) {
                printf("SN");
            }
        } else if (Y < 0){
            for (; Y < 0 ; Y++) {
                printf("NS");
            }
        }
        printf("\n");
    }
}
