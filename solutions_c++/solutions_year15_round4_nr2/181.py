#include <cstdio>
#include <cmath>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 105;

double R[N], C[N];

bool can(int n, double v, double x, double T)
{
    vector<pair<double, double> > A;
    for (int i = 0; i < n; i++)
        A.push_back(make_pair(C[i], T * R[i]));
    sort(A.begin(), A.end());
    double en_mx = 0, rem_mx = v;
    for (int i = n - 1; i >= 0; i--)
    {
        double am = min(rem_mx, A[i].second);
        en_mx += am * A[i].first;
        rem_mx -= am;
    }
    if (rem_mx > 1e-6)
        return false;
    double en_mn = 0, rem_mn = v;
    for (int i = 0; i < n; i++)
    {
        double am = min(rem_mn, A[i].second);
        en_mn += am * A[i].first;
        rem_mn -= am;
    }
    if (rem_mx > 1e-6)
        return false;
    double t_mn = en_mn / v, t_mx = en_mx / v;
    return (x / t_mn >= 1 - 1e-13 && t_mx / x >= 1 - 1e-13);
}

void solve(int cs)
{
    int n;
    scanf("%d", &n);
    double v, x;
    scanf("%lf %lf", &v, &x);
    double sr = 0, mr = 1e100;
    double mxt = -1e100, mnt = 1e100;
    double mxts = 0, mnts = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%lf %lf", &R[i], &C[i]);
        sr += R[i];
        mr = min(mr, R[i]);
        if (mxt < C[i] - 1e-5)
            mxt = C[i], mxts = 0;
        if (mxt < C[i] + 1e-5)
            mxts += R[i];
        if (mnt > C[i] + 1e-5)
            mnt = C[i], mnts = 0;
        if (mnt > C[i] - 1e-5)
            mnts += R[i];
    }
    bool bad = false;
    bool found = false;
    if (x < mnt - 1e-5)
        bad = true;
    if (x > mxt + 1e-5)
        bad = true;
    double a = 0, b = 1;
    if (!bad)
    {
        if (x < mnt + 1e-5)
            b = v / mnts, found = true;
        if (x > mxt - 1e-5)
            b = v / mxts, found = true;
    }

    while (!found && !bad && !can(n, v, x, b))
    {
        b *= 2.0;
        if (b > 1e100)
            bad = true;
    }
    if (!found && !bad)
    {
        for (int it = 0; it < 2000; it++)
        {
            double m = (a + b) / 2.0;
            if (can(n, v, x, m))
                b = m;
            else
                a = m;
        }
    }
    if (found)
        printf("Case #%d: %.9lf\n", cs, b);
    else if (bad || !can(n, v, x, b))
        printf("Case #%d: IMPOSSIBLE\n", cs);
    else
        printf("Case #%d: %.9lf\n", cs, b);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i + 1);
}
