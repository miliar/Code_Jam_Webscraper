#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}

void solve(int numtest)
{
    string s;
    cin >> s;
    int n = s.length();
    int k;
    cin >> k;

    int ans = 0;

    for(int i = 0; i + k <= n; ++i)
    {
        if (s[i] == '-')
        {
            for(int j = 0; j < k; ++j)
                s[i + j] = s[i + j] == '-'? '+' : '-';
            ++ans;
        }
    }

    bool good = true;
    for(int i = 0; i < n; ++i)
        good &= s[i] == '+';
    cout << "Case #" << numtest << ": ";
    if (good)
        cout << ans << '\n';
    else
        cout << "IMPOSSIBLE\n";
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    //cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
