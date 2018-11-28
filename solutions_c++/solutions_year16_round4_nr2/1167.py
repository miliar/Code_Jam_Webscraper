#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 202
double a[N];
int n, m;
double ans;

int count(int n)
{
    int s = 0;
    while (n)
    {
        n &= (n - 1);
        ++s;
    }
    return s;
}

double f(int k)
{
    vector<double> b;
    b.clear();
    for (int i = 0; i < n; ++i)
    {
        if ((k >> i) & 1)
            b.push_back(a[i]);
    }
    int mm = 1 << m;
    int m2 = m >> 1;
    double ans = 0;
    for (int i = 1; i < mm; ++i)
    {
        if (count(i) == m2)
        {
            double s = 1;
            for (int j = 0; j < m; ++j)
                if ((i >> j) & 1)
                    s *= b[j];
                else
                    s *= (1 - b[j]);
            ans += s;
        }
    }
    // printf("%d %f\n", k, ans);
    return ans;
}

void solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
        scanf("%lf", &a[i]);
    int nn = 1 << n;
    ans = 0;
    for (int i = 3; i < nn; ++i)
        if (count(i) == m)
        {
            ans = max(ans, f(i));
        }
    printf("%.7f\n", ans);
}

int main()
{
    int t;
    freopen("3.txt", "r", stdin);
    freopen("4.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}