#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int solve() {
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i < (int)s.size() - k + 1; i++)
        if (s[i] == '-') {
            ans++;
            for (int j = 0; j < k; j++)
                s[i + j] = (s[i + j] == '+' ? '-' : '+');
        }
    for (int i = 0; i < s.size(); i++)
        if (s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
    cout << ans << endl;
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
