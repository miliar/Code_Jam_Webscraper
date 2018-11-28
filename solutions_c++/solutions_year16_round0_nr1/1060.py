// Written by Luis Garcia, 2016.
// OJ-ID: CJ1601A

#include <cstdio>

using namespace std;

int main() {
    int T, N;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d", &N);
        if (!N) {
            printf("Case #%d: INSOMNIA\n", _T);
        } else {
            int m = N;
            for (int mask = 0; mask != 1023; m += N)
                for (int k = m; k != 0; k /= 10)
                    mask |= 1 << (k % 10);
            printf("Case #%d: %d\n", _T, m - N);
        }
    }
    return 0;
}
