#include <stdio.h>

int n, i, j, tc, cases, friends, t;
char a[1005];

int main() {
    scanf("%d\n", &tc);
    cases = 1;
    while(tc--) {
        scanf("%d \n", &n);
        for(i=0; i<=n; i++) {
            scanf("%c\n", &a[i]);
        }
        t = 0;
        friends = 0;
        for(i=0; i<=n; i++) {
            if(a[i]-'0' > 0) {
                if(i <= t) {
                    t += a[i]-'0';
                } else {
                    friends += i-t;
                    t += friends+a[i]-'0';
                }
            }
        }
        printf("Case #%d: %d\n", cases++, friends);
    }
    return 0;
}
