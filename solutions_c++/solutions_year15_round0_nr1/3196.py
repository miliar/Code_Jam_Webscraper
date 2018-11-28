#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase ++) {
        int n;
        string s;
        scanf("%d", &n);
        cin >> s;
        int ans = 0, cur = 0;
        for(int i = 0; i <= n; i ++) {
            if(cur < i) {
                ans += i - cur;
                cur = i;
            }
            cur += s[i] - '0';
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
