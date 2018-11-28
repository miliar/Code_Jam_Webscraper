#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n;
int cnt[2505];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d", &nTests);

    for(int Case = 1; Case <= nTests; ++Case) {
        printf("Case #%d: ", Case);
        memset(cnt, 0, sizeof(cnt));

        scanf("%d", &n);
        for(int i = 1; i <= 2 * n - 1; ++i) {
            for(int j = 1; j <= n; ++j) {
                int x; scanf("%d", &x);
                ++cnt[x];
            }
        }

        for(int i = 1; i <= 2500; ++i)
            if (cnt[i] & 1) printf("%d ", i);
        printf("\n");
    }

    return 0;
}

