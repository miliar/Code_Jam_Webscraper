#include <bits/stdc++.h>

using namespace std;

#define lol long long
#define fi first
#define se second
#define pb push_back
#define sz(s) (int)s.size()
#define must ios_base::sync_with_stdio(0)

#define inp(s) freopen(s, "r", stdin)
#define out(s) freopen(s, "w", stdout)

const int N = 2e+2 + 50;
int a[N];
double p[N], ans;
int n, k;

double check(int cur, int kol)
{
    if (cur == n + 1) {
        if (kol != 0)
            return 0;
        return 1;
    }
    if (a[cur] == 1)
        return p[cur] * check(cur + 1, kol + 1) + (1 - p[cur]) * check(cur + 1, kol - 1);
    return check(cur + 1, kol);
}

void rec(int n, int k)
{
    if (k < 0)
        return;
    if (n == 0)
    {
        if (k == 0)
        {
            ans = max(ans, check(1, 0));
        }
        return;
    }
    a[n] = 0;
    rec(n - 1, k);
    a[n] = 1;
    rec(n - 1, k - 1);
}

int main()
{
    inp("input.txt");
    out("output.txt");
    int t, tt;
    scanf("%d", &t);
    for (tt = 1; tt <= t; tt++)
    {
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++)
            scanf("%lf", &p[i]);
        ans = 0;
        rec(n, k);
        printf("Case #%d: %.10f\n", tt, ans);
    }
    return 0;
}
