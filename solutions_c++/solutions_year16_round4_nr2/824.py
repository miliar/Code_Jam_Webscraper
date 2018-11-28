#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdint>
#include <cstdio>
#include <algorithm>
#include <bitset>
#include <queue>
using namespace std;

void solve(int num_test = 0)
{
    int n, k;
    cin >> n >> k;
    vector<double> v(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> v[i];
    }
    int mask = 1 << n;
    double ans = 0.0;
    for (int i = 0; i < mask; ++i)
    {
        int cnt = 0;
        for (int u = 0; u < n; ++u)
        {
            if ((1 << u) & i)
                ++cnt;
        }
        if (cnt != k)
            continue;
        vector<int> id;
        for (int u = 0; u < n; ++u)
        {
            if ((1 << u) & i)
                id.push_back(u);
        }
        int mx = 1 << k;
        double sum = 0.0;
        for (int j = 0; j < mx; ++j)
        {
            cnt = 0;
            for (int u = 0; u < n; ++u)
            {
                if ((1 << u) & j)
                    ++cnt;
            }
            if (cnt != k / 2)
                continue;

            double cur = 1.0;
            for (int u = 0; u < k; ++u)
            {
                if ((1 << u) & j)
                {
                    cur *= v[id[u]];
                }
                else
                {
                    cur *= 1 - v[id[u]];
                }
            }
            sum += cur;
        }
        ans = max(ans, sum);
    }
    printf("Case #%d: %.7f\n", num_test, (float)ans);
}

int main(void)
{
#if 1
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        solve(i + 1);
    }
    return 0;
}