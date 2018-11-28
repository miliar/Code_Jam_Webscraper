#include <bits/stdc++.h>

using namespace std;

string b[3] = {"R", "P", "S"};

string answer(int n, int x) {
    if (n == 0) {
        return b[x];
    }
    string s1 = answer(n - 1, x);
    string s2;
    if (x == 0) {
        s2 = answer(n - 1, 2);
    }
    if (x == 1) {
        s2 = answer(n - 1, 0);
    }
    if (x == 2) {
        s2 = answer(n - 1, 1);
    }
    if (s1 < s2)
        return s1 + s2;
    else
        return s2 + s1;
}

void check(int n, long long &a, long long &b, long long &c, int x) {
    if (n == 0) {
        if (x == 0)
            --a;
        if (x == 1)
            --b;
        if (x == 2)
            --c;
        return;
    }
    check(n - 1, a, b, c, x);
    if (x == 0) {
        check(n - 1, a, b, c, 2);
    }
    if (x == 1) {
        check(n - 1, a, b, c, 0);
    }
    if (x == 2) {
        check(n - 1, a, b, c, 1);
    }
}


int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        long long n, a, b, c, r, p, s;
        cin >> n >> r >> p >> s;
        bool flag = false;
        string ans;
        for (int i = 0; i < 3; ++i) {
            a = r; b = p; c = s;
            check(n, a, b, c, i);
            if (a == 0 && b == 0 && c == 0) {
                if (!flag)
                    ans = answer(n, i);
                else {
                    string s = answer(n, i);
                    if (ans > s)
                        ans = s;
                }
                flag = true;
            }
        }
        if (flag)
            cout << ans << '\n';
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}
