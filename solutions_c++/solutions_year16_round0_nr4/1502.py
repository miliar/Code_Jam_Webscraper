#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 200;

int k, c, s;
ll id[maxN];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d", &nTests);
    for(int Case = 1; Case <= nTests; ++Case) {
        scanf("%d %d %d", &k, &c, &s);
        if (s < k) printf("Case #%d: IMPOSSIBLE\n", Case);
        else {
            for(int i = 1; i <= k; ++i) id[i] = i;
            for(int j = 2; j <= c; ++j) {
                for(int i = 1; i <= k; ++i)
                    id[i] = ll(id[i] - 1) * k + i;
            }
            printf("Case #%d: ", Case);
            for(int i = 1; i <= k; ++i) printf("%I64d ", id[i]);
            printf("\n");
        }
    }
    return 0;
}
