#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int t;
void solve() {
    printf("Case #%d: ", t);
    double c, f, x;
    cin >> c >> f >> x;

    double ans = 1e9, dt = 0.0, add = 2.0;
    for (int k = 0; k < (int)x + 2; ++k) {
        ans = min(ans, dt + x / add);
        dt += c / add;
        add += f;
    }
    cout.precision(30);
    cout << ans << "\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) solve();
    return 0;
}