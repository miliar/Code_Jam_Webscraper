#include <cstdio>
#include <cstring>
const int maxn = 110;
char str[maxn];
int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int T, tcase = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%s", str);
        int r = strlen(str) - 1;
        while(r >= 0 && str[r] == '+') r--;
        int ans = r >= 0 ? 1 : 0;
        while(r > 0) {
            if(str[r] != str[r - 1]) {
                ans++;
            }
            r--;
        }
        printf("Case #%d: %d\n", tcase++, ans);
    }
    return 0;
}
