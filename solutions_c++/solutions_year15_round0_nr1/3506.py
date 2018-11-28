#include <bits/stdc++.h>
using namespace std;

int solve()
{
    int Smax;
    string aud;
    cin >> Smax >> aud;

    int cur = 0;
    int ans = 0;
    for (int i = 0; i < Smax + 1; i++)
    {
        int d = aud[i] - '0';
        if (cur < i)
        {
            ans += i - cur;
            cur = i;
        }
        cur += d;
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++)
        printf("Case #%d: %d\n", test, solve());
}

