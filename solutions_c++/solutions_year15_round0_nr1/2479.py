#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    string str;
    cin >> n >> str;
    int ans = 0, count = str[0] - '0';
    for (int i = 1; i < str.size(); i++) {
        if (str[i] > '0' && i > count) {
            ans += i - count;
            count += i - count;
        }

        count += str[i] - '0';
    }

    printf("%d\n", ans);
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
