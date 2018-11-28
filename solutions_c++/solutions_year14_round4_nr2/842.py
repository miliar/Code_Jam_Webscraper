#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

int dp[1002][1002];

void solve()
{
	int n;
    cin >> n;
    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> v[i].first;
        v[i].second = i;
    }
    int mx = max_element(v.begin(), v.end())->first;
    
    sort(v.begin(), v.end());
    for (int i = 0; i < n; ++i)
    {
        int l = 0;
        int r = 0;
        for (int j = 0; j < n; ++j)
        {
            if (v[j].first < v[i].first)
            {
                if (v[j].second > v[i].second)
                    ++r;
                else
                    ++l;
            }
        }
        for (int j = 0; j <= i; ++j)
        {
            int p = v[i].second + (j - l);
            int cl = p - j;
            int cr = (n - 1 - i + j) - p;
            dp[j + 1][i - j] = dp[j][i - j] + cl;
            if (j < i)
                dp[j + 1][i - j] = min(dp[j + 1][i - j], dp[j + 1][i - j - 1] + cr);
            dp[j][i - j + 1] = dp[j][i - j] + cr;
            if (j > 0)
                dp[j][i - j + 1] = min(dp[j][i - j + 1], dp[j - 1][i - j + 1] + cl);
        }
    }
    int ans = numeric_limits<int>::max();
    for (int i = 0; i <= n; ++i)
    {
        ans = min(ans, dp[i][n - i]);
    }
    cout << ans;
}

void main()
{
	freopen("i.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}