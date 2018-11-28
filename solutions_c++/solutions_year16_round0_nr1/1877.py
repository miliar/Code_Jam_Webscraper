#include <bits/stdc++.h>

using namespace std;

bool mark[10];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for (int tp=1; tp<=t; tp++) {
        int i;
        scanf("%d\n", &i);
        if (i == 0) {
            printf("Case #%d: INSOMNIA\n", tp);
            continue;
        }
        for (int j=0; j<10; j++) mark[j] = 0;
        int total = 0;
        for (int j=1; ; j++) {
            int x = j*i;
            while (x) {
                if (!mark[x % 10]) {
                    mark[x % 10] = 1;
                    total++;
                }
                x /= 10;
            }
            if (total == 10) {
                printf("Case #%d: %d\n", tp, j*i);
                break;
            }
        }
    }

    return 0;
}
