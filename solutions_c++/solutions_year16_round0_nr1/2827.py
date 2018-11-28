#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main() {
    int T;
    bool vst[10];
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int n;
        scanf("%d", &n);
        if (!n) {
            printf("Case #%d: INSOMNIA\n", ca);
            continue;
        }
        memset(vst, 0, sizeof(vst));
        for (int i = n; ; i += n) {
            int x = i;
            while (x) {
                vst[x % 10] = 1;
                x /= 10;
            }
            bool find = false;
            for (int j = 0; j < 10; ++j) {
                if (!vst[j]) {
                    find = true;
                    break;
                }
            }
            if (!find) {
                printf("Case #%d: %d\n", ca, i);
                break;
            }
        }
    }
    return 0;
}
