#include <bits/stdc++.h>

using namespace std;

const int N = (int)1e5 + 10;

int cases;

string s;
int len;
int d[N], nm[N], n, p;
int ans;

void read_input() {
    cin >> s >> len;
    n = s.length();
    for (int i = 0; i < n; ++i) {
        if (s[i] == '+')
            nm[i] = 0;
        else
            nm[i] = 1;
    }
}

void solve() {
    for (int i = 0; i <= n - len; ++i) {
        p += d[i];
        if ((nm[i] + p) & 1) {
            p++;
            d[i + len] += -1;
            ans++;
        }
    }

    for (int i = n - len + 1; i < n; ++i) {
        p += d[i];
        if ((nm[i] + p) & 1) {
            ans = -1;
            break;
        }
    }
}

void write_output(int test) {
    cout << "Case #" << test << ": ";
    if (ans == -1)
        cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
}

void clear_data() {
    for (int i = 0; i <= n; ++i) nm[i] = d[i] = 0;
    n = p = len = ans = 0;
}

int main() {
    ios_base::sync_with_stdio(false);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> cases;
    for (int test = 1; test <= cases; ++test) {
        read_input();
        solve();
        write_output(test);
        clear_data();
    }
    return 0;
}
