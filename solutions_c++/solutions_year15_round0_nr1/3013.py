#include <bits/stdc++.h>

using namespace std;

int main() {
    int T, t, smax, s, vv, acc, ans;
    char v;
    scanf("%d", &T);
    for(t = 0; t < T; ++t) {
        scanf("%d", &smax);
        acc = ans = 0;
        for(s = 0; s <= smax; ++s) {
            scanf(" %c", &v);
            vv = v - '0';
            if(vv != 0 && acc < s) {
                ans += s - acc;
                acc = s;
            }
            acc += vv;
        }
        printf("Case #%d: %d\n", t+1, ans);
    }
}
