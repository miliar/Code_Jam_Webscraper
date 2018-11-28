#include <bits/stdc++.h>
using namespace std;

string s;

void solve() {
    cin >> s;
    stack<char> stk;
    int dubs = 0;
    for (char c : s) {
        if (!stk.empty() && c == stk.top()) {
            stk.pop();
            ++dubs;
        } else {
            stk.push(c);
        }
    }

    cout << 10 * dubs + 5 * stk.size() / 2;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
