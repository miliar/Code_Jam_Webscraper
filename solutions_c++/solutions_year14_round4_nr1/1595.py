#include <algorithm>
#include <iostream>
#include <vector>

#include <cassert>

using namespace std;

void solve()
{
    int n, x;
    cin >> n >> x;
    vector<int> s(n);
    vector<char> used(n, false);
    for (int& i: s) cin >> i;
    sort(s.begin(), s.end());
    int cnt = 0;
    int j = s.size() - 1;
    for (int i = 0; i < s.size(); ++i) {
        if (used[i]) continue;
        used[i] = true;
        while (j >= 0 && (used[j] || s[j] + s[i] > x)) --j;
        if (j >= 0) used[j] = true;
        ++cnt;
    }
    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
