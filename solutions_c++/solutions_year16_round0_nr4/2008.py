#include <bits/stdc++.h>
using namespace std;

long k, c, s;

void input()
{
    cin >> k >> c >> s;
}

void solve()
{
    if (c * s < k) {
        cout << " IMPOSSIBLE" << endl;
        return;
    }
    for (int a = 0; a < k; a += c) {
        const int b = min(a + c, k);
        long t = 0;
        for (int i = a; i < b; ++i) {
            t = t * k + i;
        }
        cout << " " << t + 1;
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        input();
        cout << "Case #" << i << ":";
        solve();
    }
}
