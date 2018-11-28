#include <iostream>
#include <string>

using namespace std;

void solve(int cas) {
    string str;
    cin >> str;
    int ans = 0;
    bool seen = false;
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == '+') seen = true;
        if (str[i] == '-' && (i == 0 || str[i-1] == '+')) ans += 1 + seen;
    }
    cout << "Case #" << cas << ": ";
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        solve(i+1);
    }
}
