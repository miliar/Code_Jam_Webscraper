#include <bits/stdc++.h>

using namespace std;

const int MX_NM = 10;
bool used[MX_NM];
string bad = "INSOMNIA";

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    memset(used, false, sizeof(used));
    long long n;
    cin >> n;
    if (n == 0)
    {
        cout << bad << '\n';
        return;
    }
    long long k = n;
    int cnt = 10;
    while (true)
    {
        long long c = k;
        while (c != 0)
        {
            if (!used[c % 10])
            {
                used[c % 10] = true;
                cnt--;
            }
            c /= 10;
        }
        if (cnt == 0)
        {
            cout << k << '\n';
            return;
        }
        k += n;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
