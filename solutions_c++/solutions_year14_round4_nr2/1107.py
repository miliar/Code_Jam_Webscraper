#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
using namespace std;
const int MAXN = 100;

int n, a[MAXN];
int ans;
bool isl[MAXN];
int l[MAXN], r[MAXN], ln, rn;
int b[MAXN], maxa;
map<int, int> ai;
map<int, int> bi;
int c[MAXN], temp[MAXN];

int merge(int l, int r)
{
    if (r - l <= 1)
    {
        return 0;
    }
    int m = (l + r) >> 1;
    int res = merge(l, m) + merge(m, r);
    int i = l, j = m, k = 0;
    while (i < m && j < r)
    {
        if (c[i] <= c[j])
        {
            temp[k++] = c[i++];
        }
        else
        {
            res += m - i;
            temp[k++] = c[j++];
        }
    }
    while (i < m) temp[k++] = c[i++];
    while (j < r) temp[k++] = c[j++];
    k = 0;
    for (int i = l; i < r; ++i)
    {
        c[i] = temp[k++];
    }
    return res;
}

void judge()
{
    ln = 0;
    rn = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] == maxa)
        {
            continue;
        }
        else if (isl[i])
        {
            l[ln++] = a[i];
        }
        else
        {
            r[rn++] = a[i];
        }
    }
    sort(l, l + ln);
    sort(r, r + rn);
    int k = 0;
    for (int i = 0; i < ln; ++i)
    {
        b[k++] = l[i];
    }
    b[k++] = maxa;
    for (int i = rn - 1; i >= 0; --i)
    {
        b[k++] = r[i];
    }
    for (int i = 0; i < n; ++i)
    {
        bi[b[i]] = i;
        //printf("%d ", b[i]);
    }
//    printf("\n");
    for (int i = 0; i < n; ++i)
    {
        c[i] = bi[a[i]];
    }
    for (int i = 0; i < n; ++i)
    {
        //printf("%d ", c[i]);
    }
    //printf("\n");
    ans = min(ans, merge(0, n));
}

void dfs(int index)
{
    if (index == n)
    {
        judge();
        return;
    }
    if (a[index] == maxa)
    {
        dfs(index + 1);
        return;
    }
    isl[index] = true;
    dfs(index + 1);
    isl[index] = false;
    dfs(index + 1);
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d", &n);
        maxa = 0;
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &a[i]);
            maxa = max(maxa, a[i]);
            ai[a[i]] = i;
        }
        ans = 0x3f3f3f3f;
        dfs(0);
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
