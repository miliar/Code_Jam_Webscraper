#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

int calc(const vector<int> &v, int m)
{
    int res = v.back();
    for (int l = 0, r = m - 1; l < r; l++, r--)
        res = max(res, v[l] + v[r]);
    return res;
}

void solve(int test)
{
    int n, x;
    cin >> n >> x;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    sort(v.begin(), v.end());
    int l = 0;
    int r = n / 2;
    while (l < r)
    {
        int m = (l + r + 1) / 2;
        int sz = calc(v, 2 * m);
        if (sz <= x)
            l = m;
        else
            r = m - 1;
    }
    cout << "Case #" << test << ": ";
    l *= 2;
    cout << l / 2 + (n - l) << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cout.setf(ios::fixed);
    cout.precision(10);
    cerr.setf(ios::fixed);
    cerr.precision(10);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
