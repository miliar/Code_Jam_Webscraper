
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n, int *pVal) {
    for (int i = 2; 1LL * i * i <= n; i++) {
        if (n % i == 0) {
            *pVal = i;
            return false;
        }
    }
    return true;
}
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++) {
        int N, J;
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", _t);
        for(int s = (1 << (N - 1)) | 1 , cnt = 0; cnt < J; s += 2) {

            int ans[11] = {0};
            int flag = 1;
            for (int b = 2; b <= 10; b++) {
                long long val = 0;
                long long x = 1;
                for (int i = 0; i < N; i++, x = x * b) {
                    if (s & (1 << i)) {
                        val += x;
                    }
                }
                if (isPrime(val, &ans[b])) {
                    flag = 0;
                    break;
                }

            }

            if (flag) {
                for (int i = N - 1; i >= 0; i--) {
                    printf("%d", (s & (1 << i)) ? 1 : 0 );
                }
                for (int b = 2; b <= 10; b++) {
                    printf(" %d", ans[b]);
                }
                printf("\n");
                cnt++;
            }
        }
    }
    return 0;
}
