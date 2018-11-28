#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long llint;
const int MAXN = 1000100;

int n, p, q, r, s;
int a[MAXN];
llint sum[MAXN];

llint get (int a, int b) {
    if (a > b) return 0;
    if (a > n - 1) return 0;
    llint ret = sum[b];
    if (a) ret -= sum[a-1];
    return ret;
}

void solve ()
{
    scanf ("%d%d%d%d%d", &n, &p, &q, &r, &s);

    for (int i = 0; i < n; ++i)
        a[i] = ((llint)i * p + q) % r + s;

    sum[0] = a[0];
    for (int i = 1; i < n; ++i)
        sum[i] = sum[i-1] + a[i];

    llint ans = 1LL << 60;
    for (int i = 0; i < n; ++i) {
        int lo = i, hi = n - 1, mid;

        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (get(i, mid) > get(mid + 1, n - 1)) hi = mid;
            else lo = mid + 1;
        }

        for (int j = max(0, max(lo - 3, i)); j < min(n, hi + 3); ++j)
            ans = min( ans, max(get(0, i - 1), max(get(i, j), get(j + 1, n - 1))) );
    }

    printf ("%.12Lf\n", 1 - (long double)ans / sum[n-1]);
}

int main (int argc, char *argv[])
{
    int No; scanf ("%d", &No);
    for (int i = 0; i < No; ++i) {
        if (argc == 1) printf ("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}


