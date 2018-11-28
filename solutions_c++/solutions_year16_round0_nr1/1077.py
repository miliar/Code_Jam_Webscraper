#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int T, n, flag[10];
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }
        int cnt = 0, m = 0;
        memset(flag, 0, sizeof(flag));
        while (cnt < 10) {
            m += n;
            for (int x = m; x > 0; x /= 10) {
                if (!flag[x % 10]) {
                    flag[x % 10] = 1;
                    cnt++;
                }
            }
        }
        printf("%d\n", m);
    }
}
