#include <bits/stdc++.h>
using namespace std;

char change(char x) {
    return x == '+' ? '-' : '+';
}

int solve(string s, char x) {
    if (s.empty()) return 0;
    if (*s.rbegin() == x)
        return solve(s.substr(0, s.size() - 1), x);
    if (*s.begin() != x) {
        string t = s.substr(1);
        reverse(t.begin(), t.end());
        return 1 + solve(t, change(x));
    }
    return 1 + solve(s.substr(0, s.size() - 1), change(x));
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; ++t) {
        string s;
        cin >> s;

        printf("Case #%d: %d\n", t, solve(s, '+'));
    }
}
