#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int p[1010], n;
int gao(int lim) {
    int res = 0;
    for (int i = 1; i <= n; i++)
        for (int x = p[i]; x > lim; x -= lim) res++;
    return res;
}
int main() {
    int __;
    scanf("%d", &__);
    for (int ca = 1; ca <= __; ca++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) {
            scanf("%d", &p[i]);
        }
        int result = 1000;
        for (int i = 1; i <= 1000; i++) {
            result = min(result, gao(i) + i);
        }
        printf("Case #%d: %d\n", ca, result);
    }
    return 0;
}
