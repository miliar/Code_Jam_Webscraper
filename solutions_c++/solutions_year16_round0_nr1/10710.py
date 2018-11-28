#include <bits/stdc++.h>
#include<algorithm>
#include<set>
#include<string.h>
#define MAX_N 1000000000000
bool used[10];
int hitung(long long  A) {
    int ans = 0;
    while (A > 0) {
        if (!used[A % 10]) {
            used[A % 10] = true;
            ans++;
        }
        A /= 10;
    }
    return ans;
}
int main() {

    freopen("A-large.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
    int T;
    long long N;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%lld", &N);
        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        memset(used, false, sizeof(used));
        int ans = 0;
        long long  j = 1;
        while (j <= MAX_N && ans < 10) {
            ans += hitung(j * N);
            j++;
        }
        if (j <= MAX_N + 1 && ans == 10) printf("Case #%d: %lld\n", i, (long long) (j-1) * N);
        else printf("Case #%d: INSOMNIA\n", i);
    }

    return 0;
}
