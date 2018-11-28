#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int t;
    int c = 0;
    scanf("%d", &t);
    while (t--) {
        long long int n, ans;
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", ++c);
            continue;
        }
        int *seen = (int*) calloc(10, sizeof(int));
        int cnt = 1;
        while (true) {
            long long int dup = cnt * n;
            cnt++;
            while (dup != 0) {
                int digit = dup % 10;
                dup /= 10;
                seen[digit] = 1;
            }
            int done = 1;
            for (int i = 0; i < 10; i++) {
                if (seen[i] == 0) {
                    done = 0;
                    break;
                }
            }
            if (done) {
                ans = (cnt-1) * n;
                break;
            }
        }
        printf("Case #%d: %lld\n", ++c, ans);
        free(seen);
    }
    return 0;
}
