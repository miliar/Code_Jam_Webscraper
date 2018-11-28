#include <bits/stdc++.h>
using namespace std;

int get(int start, int n) {
    if (n == 0) return 0;
    if (start == '-') return get('+', n-1) + 1;
    if (start == '+') return get('-', n-1) + 1;
    assert(false);
}

void solve(string s) {
    string tmp = "";
    for (int i = 0, last = -1; i < s.size(); ++i) {
        if (s[i] == last) continue;
        tmp += s[i];
        last = s[i];
    }
    if (tmp.back() == '+') cout << get(tmp[0], tmp.size()-1) << endl;
    else cout << get(tmp[0], tmp.size()) << endl;
}

int main() {
    int t;
    cin >> t;
    for (int it = 0; it < t; ++it) {
        string s;
        cin >> s;
        cout << "Case #" << (it+1) << ": ";
        solve(s);
    }

    return 0;
}