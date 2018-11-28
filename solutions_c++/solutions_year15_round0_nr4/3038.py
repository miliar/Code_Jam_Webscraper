#include<stdio.h>

bool checkRichard(int x, int r, int c);
int main() {
    
    int X, R, C;
    int testCases;
    scanf("%d", &testCases);
    
    for(int i=1; i <= testCases; i++) {
        scanf("%d", &X);
        scanf("%d", &R);
        scanf("%d", &C);
        
        if(checkRichard(X, R, C)) {
            printf("Case #%d: RICHARD\n", i);
        } else {
            printf("Case #%d: GABRIEL\n", i);
        }
    }

}

bool checkRichard(int x, int r, int c) {
     //printf(" XRC %d%d%d ",x,r,c);
     
     if(((r*c)%x) != 0)
         return true;
         
     if(x <= 2)
         return false;
     
     if(r*c == x)
         return true;
     
     if(x ==4 && r*c == 8)
         return true;
        
     return false;     
}
