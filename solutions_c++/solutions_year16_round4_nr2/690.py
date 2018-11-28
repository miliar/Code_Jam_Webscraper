#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wunused-result"
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


int const maxn = 205;

double a[maxn];

double d[maxn][maxn];

double check(const vector<double>& a)
{
    for(int i = 0; i < maxn; ++i)
        for(int j = 0; j< maxn; ++j)
            d[i][j] = 0;

    d[0][0] = 1.0;
    int n = a.size();
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
        {
            d[i + 1][j + 1] += a[i] * d[i][j];
            d[i + 1][j] += (1.0 - a[i]) * d[i][j];
        }
    return d[n][n / 2];
}

void solve(int numtest)
{
    int n,k;
    cin >> n >> k;
    for(int i = 0; i < n; ++i)
        cin >> a[i];

    sort(a, a + n);
    double ans = 0.0;

    for(int i = 0; i < n - k; ++i)
    {
        vector<double> cur;
        for(int j = 0; j < k; ++j)
            cur.push_back(a[i + j]);
        double tmp = check(cur);
        if (tmp > ans)
            ans = tmp;
    }

    for(int l = 0; l < n; ++l)
        for(int r = l; r < n; ++r)
        {
            if (l + n - r == k)
            {
                vector<double> tmp;
                for(int i = 0; i < l; ++i)
                    tmp.push_back(a[i]);
                for(int i = r; i < n; ++i)
                    tmp.push_back(a[i]);

                double cur = check(tmp);
                if (cur > ans)
                    ans = cur;
            }
        }

    cout << "Case #" << numtest << ": " << ans << '\n';
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        solve(i);
        cerr << "ok " << i << endl;
    }
}

