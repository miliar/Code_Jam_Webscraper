#include <iostream>
#include <cstdio>
using namespace std;

const int maxn = 10000;
char s[maxn];
int n;

int main() {
    int tt; cin >> tt;
    int cas = 0;
    while (tt--) {
        int ans = 0, cnt = 0;
        scanf("%d", &n);
        scanf("%s", s);
        for (int i = 0; i <= n; ++i) {
            if (cnt < i) {
                ans += (i - cnt);
                cnt = i;
            }
            cnt += s[i] - '0';
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
