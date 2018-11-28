#include "bits/stdc++.h"
using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> a;
    for (int i = 0; i < n; ++i)
    {
        int x;
        cin >> x;
        a.push_back(x);
    }
    int s[n + 10], t[n + 10];
    for (int i = 0; i < n + 10; ++i) s[i] = t[i] = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i; ++j) s[i] += (a[j] > a[i]);
        for (int j = i + 1; j < n; ++j) t[i] += (a[j] > a[i]);
    }
    long long cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        cnt += min(s[i], t[i]);
    }
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
