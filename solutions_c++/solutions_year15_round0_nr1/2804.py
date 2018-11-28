#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int TC;
    scanf("%d\n", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        int N;
        scanf("%d ", &N);
        int sum = 0, ans = 0;
        for (int i = 0; i <= N; i++) {
            char c;
            //printf("%d\n", sum);
            scanf("%c", &c);
            if (c == '0') continue;
            if (sum < i) {
                ans += i - sum;
                sum = i;
            }
            scanf("\n");
            sum += c - '0';
        }
        printf("Case #%d: %d\n", tc, ans);
    }
}
