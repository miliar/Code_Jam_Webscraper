#include <stdio.h>

int x, r, c, tc, cases, temp;

int main() {
    cases = 1;
    scanf("%d\n", &tc);
    while(tc--) {
        scanf("%d %d %d\n", &x, &r, &c);
        printf("Case #%d: ", cases++);
        if(x==1) {
            printf("GABRIEL\n");
        } else if(x==2) {
            if((r*c)%2==0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if(x==3) {
            if((r==2&&c==3)||(r==3&&c==2)) printf("GABRIEL\n");
            else if((r==4&&c==3)||(r==3&&c==4)) printf("GABRIEL\n");
            else if(r==3&&c==3) printf("GABRIEL\n");
            else printf("RICHARD\n");
        } else if(x==4) {
            if((r==4&&c==3)||(r==3&&c==4)) printf("GABRIEL\n");
            else if(r==4&&c==4) printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
    }
    return 0;
}
