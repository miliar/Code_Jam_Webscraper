#include <bits/stdc++.h>

using namespace std;

int m[1000], dp[1010][1010];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= 1000; ++i)
        for (int j = i + 1; j <= 1000; ++j)
        {
            dp[i][j] = j;
            for (int z = 1; z < j; ++z)
                dp[i][j] = min(dp[i][j], dp[i][j - z] + dp[i][z] + 1);
        }
    for (int i = 0; i < t; ++i)
    {
        int n, rez = 10000;
        cin >> n;
        for (int j = 0; j < n; ++j)
            cin >> m[j];
        for (int j = 1; j <= 1000; ++j)
        {
            int k = 0;
            for (int i1 = 0; i1 < n; ++i1)
                k += dp[j][m[i1]];
            rez = min(rez, k + j);
        }
        cout << "Case #" << i + 1 << ": " << rez << '\n';
    }
    return 0;
}
