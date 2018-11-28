#include <cstdio>
#include <algorithm>
using namespace std;

char s[10];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++) {
        int n;
        scanf("%d%s", &n, s);
        int cot = 0, ans = 0;
        for (int i = 0; i <= n; i ++) {
            ans += max(0, i - ans - cot);
            cot += s[i] - '0';
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
