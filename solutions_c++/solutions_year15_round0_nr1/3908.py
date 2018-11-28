#include <cstdio>
#include <algorithm>

using namespace std;

char s[1010];
int n;

int main(void) {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
        scanf("%d%s", &n, s);
        int Ans = 0, sum = 0;
        for (int i = 0; i < n; i++) {
            Ans = max(Ans, i + 1 - (sum += s[i] - 48));
        }
        printf("Case #%d: %d\n", _,Ans);
    }
    return 0;
}

