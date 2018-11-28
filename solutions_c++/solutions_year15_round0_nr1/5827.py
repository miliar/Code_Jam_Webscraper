#include <cstdio>
#include <stdlib.h>

int T;
int S;
char a;
int standing_audience;
int y;

int main () {
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    
    for (int x = 1; x <= T; x++) {
        scanf("%d", &S);
        for (int i = 0; i < S; i++) {
            scanf(" %c ", &a);
            standing_audience += atoi(&a);
            if (standing_audience < i + 1) {
                y += i + 1 - standing_audience;
                standing_audience = i + 1;
            }
        }
        scanf(" %c ", &a);
        
        printf("Case #%d: %d\n", x, y);
        
        y = 0;
        standing_audience = 0;
    }
    
    return 0;
}