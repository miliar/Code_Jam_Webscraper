#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, m, k;
    cin >> n >> m >> k;
    assert(n == k);
    for (int i = 1; i <= n; i++)
        cout << i << (i == n ? '\n' : ' ');
    return;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++){
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}