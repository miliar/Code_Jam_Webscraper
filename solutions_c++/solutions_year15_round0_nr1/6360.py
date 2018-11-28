#include <bits/stdc++.h>

using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int k;
        string str;
        cin >> k >> str;
        long long friends = 0, ans = 0;
        for (int i = 0; i < (int)str.size(); i++) {
            if (i > friends) { 
                ans += i - friends;
                friends += i - friends;
            }
            friends += (str[i] - '0');
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
    return 0;
}
