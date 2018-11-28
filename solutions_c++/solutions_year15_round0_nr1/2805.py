#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int n;
string s;

void read() {
    cin >> n >> s;
}

void solve() {
    int ans = 0;
    int cur = 0;

    for (int i = 0; i <= n; i++) {
        cur += s[i] - '0';
        cur --;
        if (cur < 0) {
            ans ++;
            ++ cur;
        }
    }

    printf ("%d", ans);
}

int main() {
    int i, cases;

    scanf("%d", &cases);
    for (i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
        printf ("\n");
    }
    return 0;
}

