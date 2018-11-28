#include <cstdio>

using namespace std;

char s[51];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, l, f = 0, j, k;
        
        scanf("%d %d", &n, &l);
        
        for (j = 0; j < n; j++) {
            scanf("%s", s);
            
            for (k = 0; k < l; k++) {
                if (s[k] == '0') break;
            }
            
            if (k == l) f = 1;
        }
        
        scanf("%s", s);
        
        printf("Case #%d: ", i + 1);
        
        if (f == 1) {
            puts("IMPOSSIBLE");
        } else {
            putchar('0');
            for (j = 0; j < l - 1; j++) putchar('?');
            putchar(' ');
            for (j = 0; j < 25; j++) printf("01");
            printf("0?");
            for (j = 0; j < 25; j++) printf("01");
            puts("");
        }
    }
    
    return 0;
}
