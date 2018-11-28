#include <bits/stdc++.h>

using namespace std;

int n;
string a, b;
int ans = INT_MAX;
int u, v;



void rec1(int num, int pum, int i) {
    if (i == n) {
        if (abs(num - pum) < ans || (abs(num - pum) == ans && pum < u) || (abs(num - pum) == ans && pum == u && pum < v)) {
            ans = abs(num - pum);
            u = num;
            v = pum;
        }
    } else {
        if (b[i] == '?') {
            for (int j = 0; j < 10; j++) {
                rec1(num, pum * 10 + j, i + 1);
            }
        } else {
            rec1(num, pum * 10 + (b[i] - '0'), i + 1);
        }
    }
}

void rec(int num, int i) {
    if (i == n) {
        rec1(num, 0, 0);
    } else {
        if (a[i] == '?') {
            for (int j = 0; j < 10; j++) {
                rec(num * 10 + j, i + 1);
            }
        } else {
            rec(num * 10 + (a[i] - '0'), i + 1);
        }
    }
}

string kek(int n) {
    string d = "";
    while (n > 0) {
        d += (n % 10 + '0');
        n /= 10;
    }
    reverse(d.begin(), d.end());
    return d;
}


void solve() {
    cin >> a >> b;
    n = a.size();
    ans = INT_MAX;
    rec(0, 0);
}

main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
        a = kek(u);
        b = kek(v);
        while (a.size() < n) {
            a = '0' + a;
        }
        while (b.size() < n) {
            b = '0' + b;
        }
        cout << "Case #" << i + 1 << ": " << a << " " << b << endl;
    }
}
