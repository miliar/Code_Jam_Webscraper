#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;



int main() {
    freopen("Documents/NUSHigh/Year_5/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/NUSHigh/Year_5/Informatics/GoogleCodeJam/pancake.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        char s[1010];
        scanf("%s", s);
        int n = 0;
        int k;
        while (s[n] == '+' || s[n] == '-') n++;
        scanf("%d", &k);
        int ans = 0;
        for (int i = 0; i <= n-k; i++) {
            if (s[i] == '-') {
                for (int j = i; j < i+k; j++) {
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
                ans++;
            }
        }
        bool finished = true;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                finished = false;
                break;
            }
        }
        if (finished) {
            printf("Case #%d: %d\n", cas, ans);
        }
        else printf("Case #%d: IMPOSSIBLE\n", cas);
    }
}
