#include <bits/stdc++.h>
using namespace std;
#define FOR(i, s, t) for(int i = s, _t = t; i < _t; i++)

const int maxn = 1000 + 5;
int n;
int a[maxn];
int ans1, ans2, maxdelta;

int main()
{
    freopen ("A-large (1).in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int kase;
    scanf("%d", &kase);
    FOR(T, 1, kase + 1)
    {
        scanf("%d", &n);
        FOR(i, 0, n) scanf("%d", a+i);
        ans1 = ans2 = maxdelta = 0;

        FOR(i, 0, n-1)
        {
            ans1 += (a[i] - a[i+1]) > 0 ? (a[i] - a[i+1]) : 0;
            maxdelta = max(maxdelta, a[i] - a[i+1]);
        }
        FOR(i, 0, n-1)
        {
            ans2 += (a[i] < maxdelta) ? a[i] : maxdelta;
        }

        printf("Case #%d: %d %d\n", T, ans1, ans2);
    }
    return 0;
}
