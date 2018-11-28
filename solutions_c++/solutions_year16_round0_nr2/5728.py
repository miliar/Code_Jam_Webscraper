#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        string s; cin >> s;
        s.push_back('+');
        int ans = 0, l = s.length();
        for (int i = 1; i < l; i++) {
            ans += (s[i] != s[i-1]);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
