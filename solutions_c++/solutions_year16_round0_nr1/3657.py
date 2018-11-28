#include <cstdio>
#include <algorithm>
using namespace std;

void gao(int &mask, int x) {
    for (; x; x /= 10) mask |= 1 << (x % 10);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        int n, y = 0, mask = 0;
        scanf("%d", &n);
        if (!n) {
            printf("Case #%d: INSOMNIA\n", cas);
            continue;
        }
        do {
            gao(mask, y += n);
        } while (mask != 1023);
        printf("Case #%d: %d\n", cas, y);
    }
}
