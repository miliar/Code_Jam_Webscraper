#include "bits/stdc++.h"
using namespace std;

void solve()
{
    int n, v;
    vector<int> s;
    cin >> n >> v;
    for (int i = 0; i < n; ++i)
    {
        int x;
        cin >> x;
        s.push_back(x);
    }
    sort(s.begin(), s.end());
    int cnt = 0;
    int i = s.size() - 1;
    int j = 0;
    while (i > j)
    {
        ++cnt;
        if (s[i] + s[j] <= v) ++j;
        --i;
    }
    if (i == j) ++cnt;
    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
