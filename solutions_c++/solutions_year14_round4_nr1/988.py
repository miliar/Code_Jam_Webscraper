#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int a[111111];

int main()
{
    int testcase, n, x;
    freopen("alarge.in", "r", stdin);
    freopen("alarge.out", "w", stdout);
    scanf("%d", &testcase);
    for (int test = 1; test <= testcase; test++) {
        scanf("%d%d", &n, &x);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        sort(a + 1, a + n + 1);
        int l, r;
        l = 1; r = n;
        int ans= 0;
        while (l <= r) {
            if (l == r) {ans++;break;}
            if (a[l] + a[r] <= x) {
                l++;r--;
                ans++;
            }
            else {
                r--;
                ans++;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
