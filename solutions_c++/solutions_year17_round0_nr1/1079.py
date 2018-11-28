/*
 *  Author:
 *      Indestinee
 *  Date:
 *      2017/04/08
 *  Name:
 *      a.cpp
 */

#include <bits/stdc++.h>
using namespace std;
const int maxn = 1 << 10, flag = '+' ^ '-';
int cas, n, k, a[maxn];
char s[maxn];
inline int work() {
    int ans = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt ^= a[i];
        if (cnt & 1)
            s[i] ^= flag;
        if (s[i] == '+')
            continue;
        if (i + k > n)
            return -1;
        cnt ^= 1;
        a[i + k] ^= 1;
        ans++;
    }
    return ans;
}
int main() {
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++) {
        scanf("%s%d", s, &k);
        n = strlen(s);
        memset(a, 0, n << 2);
        int ans = work();
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }
    }
    return 0;
}
