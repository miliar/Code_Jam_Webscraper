#include <bits/stdc++.h>

using namespace std;

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    int k, c, s;
    cin >> k >> c >> s;
    for (int i = 1; i <= k; i++)
    {
        cout << i << " ";
    }
    cout << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("out.txt", "w", stdout);
    freopen("D-small-attempt0.in", "r", stdin);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
