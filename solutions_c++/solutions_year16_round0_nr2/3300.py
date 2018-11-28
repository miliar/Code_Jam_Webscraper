#include <bits/stdc++.h>

using namespace std;

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    string t;
    cin >> t;
    char last;
    int cnt = 0;
    for (int i = 0; i < (int)t.size(); i++)
    {
        if (i == 0 or last != t[i])
        {
            cnt++;
            last = t[i];
        }
    }
    if (last == '+')
    {
        cnt--;
    }
    cout << cnt << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
