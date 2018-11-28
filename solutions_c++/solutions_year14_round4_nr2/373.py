#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cassert>
#include <cstring>

using namespace std;

const int MAXN = 1010;

int n;
int a[MAXN], o[MAXN], l[MAXN], r[MAXN];
int dp[MAXN];

int rec (int i) {
    if (i == n) return 0;

    int &ref = dp[i];
    if (ref != -1) return ref;
    ref = 1e9;

    int t = o[i];

    return ref = min(l[t], r[t]) + rec(i + 1);
}

void solve ()
{
    scanf ("%d", &n);

    for (int i = 0; i < n; ++i)
        scanf ("%d", a + i), o[i] = i;
    
    for (int i = 0; i < n; ++i) {
        l[i] = r[i] = 0;
        for (int j = 0; j < i; ++j)
            l[i] += a[j] > a[i];
        for (int j = i + 1; j < n; ++j)
            r[i] += a[j] > a[i];
    }

    sort (o, o + n, [] (int i, int j) {
            return a[i] < a[j]; });

    memset (dp, -1, sizeof dp);
    printf ("%d\n", rec(0));
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


