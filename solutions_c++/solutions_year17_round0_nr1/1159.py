#include <bits/stdc++.h>
#define fr(i, n) for (int i = 0; i < n; i++)
#define frab(i, a, b) for (int i = a; i < b; i++)

using namespace std;

typedef long long ll;

int solve() {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int ans = 0;
    int n = s.size();
    fr(i, n - k + 1) {
        if (s[i] == '-') {
            ans++;
            frab(j, i, i + k)
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
        }
    }
    fr(i, n)
        if (s[i] == '-')
            return -1;
    return ans;
}

int main() {
    //srand(time(NULL));
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    int tests;
    cin >> tests;
    fr(i, tests) {
        int ans = solve();
        if (ans != -1)
            cout << "Case #" << i + 1 << ": " << ans << endl;
        else
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
}
