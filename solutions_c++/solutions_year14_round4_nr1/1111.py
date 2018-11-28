#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
using namespace std;
const int MAXN = 1e4 + 10;

int a[MAXN];

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        int n, x;
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &a[i]);
        }
        sort(a, a + n);
        int left = 0, right = n - 1;
        int cnt = 0;
        while (left <= right)
        {
            ++cnt;
            if (a[left] + a[right] > x)
            {
                --right;
            }
            else
            {
                --right;
                ++left;
            }
        }
        printf("Case #%d: %d\n", t, cnt);
    }
    return 0;
}
