#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MS(x, y) memset(x, y, sizeof(x))

typedef long long LL;
const int MAXN = 1000 + 5;

char str[MAXN];
int ans, len, newstr[MAXN], k;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, kase = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%s%d", str, &k);
        len = 0;
        for (len = 0; str[len]; ++len) {
            if (str[len] == '+') newstr[len] = 1;
            else newstr[len] = 0;
        }
        ans = 0;
        for (int i = 0; i <= len - k; ++i) if (!newstr[i]) {
//            cout << i << endl;
            ++ans;
            for (int j = 0; j < k; ++j) newstr[j + i] ^= 1;
        }
        bool flag = false;
        for (int i = 0; i < len; ++i) if (!newstr[i]) {
            flag = true;
            break;
        }
        printf("Case #%d: ", ++kase);
        if (flag) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}
