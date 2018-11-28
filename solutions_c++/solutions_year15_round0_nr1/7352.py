#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tt;
    cin >> tt;
    for (int test = 1; test <= tt; ++test) {
        int n; string s;
        cin >> n >> s;
        ++n;
        int friendsHave = s[0] - '0';
        int friendsNeeded = 0;
        for (int i = 1; i < n; ++i) {
            int need = max(0, i - friendsHave);
            friendsNeeded += need;
            friendsHave += s[i] - '0' + need;
        }
        cout << "Case #" << test << ": " << friendsNeeded << endl;
    }
    return 0;
}
