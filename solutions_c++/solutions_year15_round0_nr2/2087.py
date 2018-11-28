#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

vector <int> v;
int ans;
int n;

void solve() {

    for (int i = 1; i <= 1000; ++i) {
        int perel = 0;
        int mx = 0;
        for (int j = 0; j < v.size(); ++j) {
            mx = max(mx, min(i, v[j]));
            int lishnee = v[j] - i;
            if (lishnee < 0) continue;
            perel += lishnee / i + (lishnee % i != 0);
        }
        ans = min(ans, mx + perel);
    }

    return;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    for (int t = 1; t <= test; ++t) {
        cin >> n;
        v.clear();
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            v.push_back(x);
        }
        ans = 11111110;

        solve();

        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
