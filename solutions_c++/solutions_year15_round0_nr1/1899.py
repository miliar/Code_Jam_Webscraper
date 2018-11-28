#include <cstdio>
#include <cstring>

int t, s;
char str[1005];

int main() {
    scanf("%d", &t);
    int cas = 0;
    while (t--) {
        int sum = 0;
        int ans = 0;
        scanf("%d%s", &s, str);
        for (int i = 0; i <= s; i++) {
            int num = str[i] - '0';
            if (sum >= i) sum += num;
            else {
                ans += i - sum;
                sum = i + num;
            }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
