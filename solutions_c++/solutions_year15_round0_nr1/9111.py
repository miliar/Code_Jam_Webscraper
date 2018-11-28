#include<bits/stdc++.h>
using namespace std;


void solve() {

    int n, ans = 0;
    scanf("%d ", &n);
    string s;
    getline(cin, s);

    for (int i = 0, c = 0; i <= n; c += s[i++] - '0')
        if (i > c) {
            ans += i - c;
            c += i - c;
        }

    printf("%d\n", ans);
}


main() {

    //freopen("1.txt", "r", stdin);
    //freopen("2.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
