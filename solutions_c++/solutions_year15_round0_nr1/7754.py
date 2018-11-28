#include <bits/stdc++.h>
using namespace std;

const int MaxN = (int) 1e3 + 10;
int n;
char st[MaxN];

int main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int TC;
    scanf("%d", &TC);

    for (int xTC = 1; xTC <= TC; ++xTC) {
        scanf("%d%s", &n, st);

        int s = st[0] - 48;
        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            if (s < i) {
                ans += i - s;
                s = i;
            }
            s += st[i] - 48;
        }

        printf("Case #%d: %d\n", xTC, ans);
    }

    return 0;
}
