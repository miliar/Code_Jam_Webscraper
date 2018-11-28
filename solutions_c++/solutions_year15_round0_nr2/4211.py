#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int p[1010], n;
int calc(int limit) {
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
        int x = p[i];
        while (x > limit) {
            x -= limit;
            ++sum;
        }
    }
    return sum;
}
int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &p[i]);
        }
        int res = 1000000000;
        for (int i = 1; i <= 1000; ++i) {
            res = min(res, calc(i) + i);
        }
        printf("Case #%d: %d\n", ca, res);
    }
    return 0;
}
