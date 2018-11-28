#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

void go(int casenum) {
    string s;
    cin >> s;
    int n = s.length();
    int ans = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '-') {
            for (int j = 0; j < i; j++) s[j] = s[j] == '+' ? '-' : '+';
            ans++;
        }
    }

    cout << "Case #" << casenum << ": " << ans << '\n';
}

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) go(i);
}
