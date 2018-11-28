#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int main() {

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T, ca = 0;
    cin >> T;
    while (T--) {
        int n;
        string s;
        cin >> n >> s;
        int cur = 0, ans = 0;
        for (int i = 0; i <= n; ++i) {
            int add = s[i] - '0';
            if (cur >= i) {
                cur += add;
            } else {
                ans += i - cur;
                cur += add + i - cur;
            }
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
