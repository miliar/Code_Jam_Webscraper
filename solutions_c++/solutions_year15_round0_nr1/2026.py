#include <bits/stdc++.h>

using namespace std;

int acc;
int ans;
string s;

int main() {
    int t;
    cin >> t;
    for (int z = 1; z <= t; z++) {
        int n;
        ans = 0;
        acc = 0;
        cin >> n >> s;
        for (int i = 0; i <= n; i++) {
            if (i > acc) {
                ans++;
                acc++;
            }
            acc += s[i] - '0';
        }
        printf("Case #%d: %d\n", z, ans);
    }

    return 0;
}
