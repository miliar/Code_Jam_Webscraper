#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, smax;
    char s[1005];
    scanf("%d", &t);
    for (int cas=1; cas<=t; cas++) {
        scanf("%d %s", &smax, s);
        int  add = 0, cur = 0;
        for (int j=0; j<=smax; j++) {
            if (cur < j && (s[j]-'0')>0) {
                add += j-cur;
                cur += add;
            }
            cur += s[j]-'0';
        }
        printf("Case #%d: %d\n", cas, add);
    }
    return 0;
}