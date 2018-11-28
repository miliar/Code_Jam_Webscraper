#include <bits/stdc++.h>

using namespace std;

const int MAXK = 100 + 10;
const int MAXC = 100 + 10;

int k, c, s;

long long get_pos(int start_pos, int k, int c) {
    long long p = start_pos;
    for(int i = 2; i <= c; i++) {
        p = (p - 1) * k + start_pos;
    }
    return p;
}

void solve() {
    cin >> k >> c >> s;
    for(int i = 1; i <= k; i++) {
        cout << get_pos(i, k, c);
        if (i + 1 <= k) cout << " ";
    }
    cout << endl;
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);

    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; tc++) {
        cout << "Case #" << tc << ": ";
        solve();
    }
}
