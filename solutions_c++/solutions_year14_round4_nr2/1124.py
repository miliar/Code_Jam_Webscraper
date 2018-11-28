#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>

using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
const int N = 2000;

int a[N], b[N], now;

void go(int l, int r)
{
    while (l != r) if (l < r)
    {
        int h = b[l];
        b[l] = b[l + 1], b[l + 1] = h;
        now++, l++;
    }
    else
    {
        int h = b[l];
        b[l] = b[l - 1], b[l - 1] = h;
        now++, l--;
    }
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        int ans = 2e9;
        for (int x1 = 1; x1 <= n; x1++) for (int y1 = 1; y1 <= n; y1++)
            for (int x2 = 1; x2 <= n; x2++) for (int y2 = 1; y2 <= n; y2++)
                for (int x3 = 1; x3 <= n; x3++) for (int y3 = 1; y3 <= n; y3++)
        {
            for (int i = 1; i <= n; i++) b[i] = a[i];
            now = 0;
            go(x1, y1);
        go(x2, y2);
        go(x3, y3);
            int nom = 1;
            for (int i = 2; i <= n; i++) if (b[i] > b[nom]) nom = i;
            for (int i = nom - 1; i >= 1; i--)
            {
                int ok = i;
                for (int j = i; j >= 1; j--) if (b[ok] < b[j]) ok = j;
                go(ok, i);
            }
            for (int i = nom + 1; i <= n; i++)
            {
                int ok = i;
                for (int j = i; j <= n; j++) if (b[ok] < b[j]) ok = j;
                go(ok, i);
            }
            ans = min(ans, now);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
