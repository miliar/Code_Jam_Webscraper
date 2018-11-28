#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
const int maxn = 10005;

int a[maxn];
int n, m;

int main()
{
    // freopen("in.cpp", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int T, ncase = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)scanf("%d", &a[i]);
        sort(a, a + n);
        int ret = 0;
        int l = 0, r = n - 1;
        while (l < r)
        {
            if (a[l] + a[r] <= m)
            {
                ret++;
                l++, r--;
            }
            else
            {
                while (l < r && a[l] + a[r] > m)r--;
                if (l < r && a[l] + a[r] <= m)
                {
                    ret++;
                    l++, r--;
                }
                else
                {
                    l++;
                }
            }
        }
        printf("Case #%d: %d\n", ++ncase, n - ret);
    }
    return 0;
}