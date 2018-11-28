#include <bits/stdc++.h>
using namespace std;

int TC, N, arr[1005];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        int ans = 2000000000;
        scanf("%d", &N);
        for (int i = 0; i < N; i++) scanf("%d", &arr[i]);
        for (int i = 1; i <= 1002; i++) {
            int sum = 0;
            for (int j = 0; j < N; j++) sum += (arr[j] - 1) / i;
            ans = min(ans, sum + i);
        }
        printf("Case #%d: %d\n", tc, ans);
    }
}
