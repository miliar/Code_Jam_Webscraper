#include <bits/stdc++.h>

using namespace std;

#define MAXN 1010

int ans;
int v[MAXN];

int main() {
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++) {
        ans = MAXN * MAXN;
        int n, maxi = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &v[i]);
            maxi = max(maxi, v[i]);
        }
        int acc;
        for (int i = 1; i <= maxi; i++) {
            acc = i;
            for (int j = 0; j < n; j++) {
                if (v[j] > i) {
                    acc += ceil((double)(v[j] - i)/(double)i);
                }
            }
            ans = min(acc, ans);
        }
        printf("Case #%d: %d\n", z, ans);
    }
    return 0;
}
