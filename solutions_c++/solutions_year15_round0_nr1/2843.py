#include "bits/stdc++.h"
using namespace std;

int t;

int solve()
{
    vector<int> a, b;
    string s;
    int m;

    cin >> m >> s;
    for (int i = 0; i < s.length(); ++i)
    {
        a.push_back(s[i] - '0');
    }
    b.push_back(0);
    for (int i = 1; i < s.length(); ++i)
    {
        b.push_back(b.back() + a[i - 1]);
    }

    int ans = 0;
    for (int i = 0; i < s.length(); ++i)
    {
        if (ans < i - b[i])
            ans = i - b[i];
    }
    return ans;
}

int main()
{
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
    return 0;
}
