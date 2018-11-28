#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", i + 1);
        if (n == 0) {
            printf("INSOMNIA\n");
        } else {
            int was[10];
            for (int i = 0; i < 10; ++i) {
                was[i] = 0;
            }
            for (int c = 1;; ++c) {
                int x = c*n;
                while (x != 0) {
                    was[x%10] = 1;
                    x /= 10;
                }
                int gd = 1;
                for (int i = 0; i < 10; ++i) {
                    if (was[i] == 0) gd = 0;
                } 
                if (gd == 1) {
                    printf("%d\n", c*n);
                    break;
                }
            }
        }
    }
}