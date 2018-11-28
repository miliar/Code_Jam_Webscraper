#include <cstdio>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int n;
        char buf[1010];
        scanf("%d%s", &n, buf);
        int sum = 0, ans = 0;
        for (int i = 0; i <= n; i++) {
            if (buf[i] == '0') continue;
            if (sum < i) { ans += i - sum; sum = i; }
            sum += buf[i] - '0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
