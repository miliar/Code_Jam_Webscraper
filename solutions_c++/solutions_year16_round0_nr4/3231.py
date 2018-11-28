# include <iostream>
# include <cmath>
# include <algorithm>
# include <map>
# include <vector>
using namespace std;


void solve(int test) {
    cout << "Case #" << test << ": ";
    long long k, c, s;
    cin >> k >> c >> s;
    for (int i = 1; i <= k; i++) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        solve(t);
    }
    return 0;
}