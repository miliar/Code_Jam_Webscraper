#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int smax, s[2000];
        char str[2000];
        scanf("%d%s", &smax, str);
        for (int i = 0; i <= smax; i++) {
            s[i] = str[i] - '0';
        }

        int ans = 0;
        int sum = 0;
        for (int i = 0; i <= smax; i++) {
            int a = max(i - sum, 0);
            ans += a;
            sum += s[i] + a;
        }

        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
