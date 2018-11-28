#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

long long get(vector<long long> v)
{

}

void solve(int test)
{
    long long n, p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    vector<long long> v(n);
    long long tot = 0;
    for (long long i = 0; i < n; i++)
    {
        v[i] = (i * p + q) % r + s;
        tot += v[i];
    }
    long long lo = *max_element(v.begin(), v.end());
    long long hi = tot;
    while (lo < hi)
    {
        long long mid = (lo + hi) / 2;
        int l = 0;
        bool ok = false;
        for (int i = 0; i < 3; i++)
        {
            long long s = 0;
            for (; l < n && s <= mid; l++)
                s += v[l];
            if (l == n && s <= mid)
                ok = true;
            l--;
        }
        if (ok)
            hi = mid;
        else
            lo = mid + 1;
    }
    cout << "Case #" << test << ": ";
    cout << (tot - lo) * 1.0 / tot << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    cout.setf(ios::fixed);
    cout.precision(12);
    cerr.setf(ios::fixed);
    cerr.precision(12);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
