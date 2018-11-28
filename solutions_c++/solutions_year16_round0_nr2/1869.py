#include <bits/stdc++.h>
using namespace std;

void change(char &c) {
    c = (c == '+' ? '-' : '+');
}

int solve(string &s, int pos) {
    change(s[pos]);
    for (auto i = s.begin() + 1 + pos; i != s.end(); i++) {
        if (*i == *(i - 1))
            return 1 + solve(s, i - s.begin());
        change(*i);
    }
    return (s[pos] == '+');
}

int main() {
    int t;
    cin >> t;
    for (int ndt = 1; ndt <= t; ndt++) {
        int ans = 0;
        string p;
        cin >> p;
        cout << "Case #" << ndt << ": ";
        cout << solve(p, 0) << endl;
    }
}
