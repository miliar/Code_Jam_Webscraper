#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int T; long long n;
    cin >> T;
    string s;
    for (int o = 1; o <= T; o++) {
        cin >> s;
        s += '+';
        int ans = 0;
        for (int i = s.size() - 1; i > 0; i--)
            if (s[i]!=s[i-1]) ans++;
        printf("Case #%d: %d\n", o, ans);
    }
}
