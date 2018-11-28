#include "bits/stdc++.h"
using namespace std;

int specialCnt(int hi, int d, vector<int>p)
{
    int cnt = 0;
    for (int i = 0; i < d; ++i)
    {
        cnt += (p[i] - 1) / hi;
    }
    return cnt;
}

int solve()
{
    int d;
    vector<int> p;
    int maxp = -1;
    cin >> d;
    for (int i = 0; i < d; ++i)
    {
        int x;
        cin >> x;
        p.push_back(x);
        if (x > maxp)
            maxp = x;
    }

    int ans = 99999999;
    for (int i = 1; i <= maxp; ++i)
    {
        int x = specialCnt(i, d, p);
        if (ans > i + x)
            ans = i + x;
    }
    return ans;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
    return 0;
}
