#include <cstdio>

int a[1005];

inline int min(int a, int b) {
    if (a < b) {
        return a;
    }
    return b;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d:", t);
        int n;
        scanf("%d", &n);
        
        scanf("%d", &a[0]);
        int sum = 0;
        int max = 0;
        for (int i = 1; i < n; ++i) {
            scanf("%d", &a[i]);
            if (a[i-1] - a[i] > 0) {
                sum += a[i-1] - a[i];
            }
            if (a[i-1] - a[i] > max) {
                max = a[i-1] - a[i];
            }
        }
        
        int sum2 = 0;
        for (int i = 0; i < n - 1; ++i) {
            sum2 += min(a[i], max);
        }
        
        printf(" %d %d\n", sum, sum2);
    }
}
