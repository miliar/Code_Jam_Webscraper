#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int a;
        string s;
        cin >> a >> s;
        int n = 0, res = 0;
        for (int i = 0; i <= a; ++i) {
            if (n < i) res++, n++;
            n += (s[i]-'0');
        }
        printf("Case #%d: %d\n", t, res);
    }
}
