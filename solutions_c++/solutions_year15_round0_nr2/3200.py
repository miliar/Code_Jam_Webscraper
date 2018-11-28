#include<stdio.h>
#include<iostream>
#include<string>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
#define LL long long
using namespace std;

const int N = 1010;
int cnt[N], a[N];

int dfs (int n, int m) {
    if (n <= m) return 0;
    return dfs (n / 2, m) + dfs (n - n / 2, m) + 1;
}

int main () {
//    freopen ("in.txt", "r", stdin);
//    freopen ("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        memset (cnt, 0, sizeof cnt);
        int mx = 0;
        for (int i = 1; i <= n; i++) {
            scanf ("%d", &a[i]);
            mx = max (mx, a[i]);
        }
        int res = mx;
        for (int i = mx; i >= 1; i--) {
            int tmp = 0;
            for (int j = 1; j <= n; j++) {
                tmp += (a[j] - 1) / i;
            }
            res = min (res, tmp + i);
        }
        printf ("Case #%d: %d\n", cas++, res);
    }
}
