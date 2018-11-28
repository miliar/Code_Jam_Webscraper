#include <cstdio>
using namespace std;

typedef long long LL;

LL change(LL x, int d) {
    LL s = 1;
    LL y = 0;
    while (x) {
        if (x & 1)
            y += s;
        x >>= 1;
        s *= d;
    }
    return y;
}

int div(LL x) {
    for (int i = 2; (LL)i * i <= x; i++)
        if (x % i == 0)
            return i;
    return -1;
}

void work() {
    int n, j;
    scanf("%d%d", &n, &j);
    LL x = 1 << (n - 1) | 1;
    while (j > 0) {
        int d[11];
        bool flag = true;
        for (int i = 2; i <= 10; i++) {
            LL y = change(x, i);
            d[i] = div(y);
            if (d[i] == -1) {
                flag = false;
                break;
            }
        }
        if (flag) {
            j--;
            printf("%lld", change(x, 10)); 
            for (int i = 2; i <= 10; i++)
                printf(" %d", d[i]);
            puts("");
        }
        x += 2;
    }
}

int main() {
    int T, C = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d:\n", ++C);
        work();
    }
    return 0;
}
