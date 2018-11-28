#include <stdio.h>

int a[4];
int count, ans;

void check(int x) {
    for (int i = 0; i < 4; i++) {
        if (a[i] == x) {
            count++;
            ans = x;
        }
    }
}


int main() {
    int n;
    scanf("%d", &n);
    for (int cn = 1; cn <= n; cn++) {
        printf("Case #%d: ", cn);
        count = 0;
        int r, x;
        scanf("%d", &r);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                if (i == r) {
                    scanf("%d", &a[j-1]);
                } else {
                    scanf("%d", &x);
                }
            }
        }
        scanf("%d", &r);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == r) check(x);
            }
        }
        if (count == 0) {
            puts("Volunteer cheated!");
        } else if (count == 1) {
            printf("%d\n", ans);
        } else {
            puts("Bad magician!");
        }
    }
}
