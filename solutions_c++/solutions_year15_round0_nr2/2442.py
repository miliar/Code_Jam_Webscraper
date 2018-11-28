#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <limits.h>
#define MAXN 1010
using namespace std;
int n, a[MAXN];
int ans;
int judge(int MAX_DAY) {
    for(int day = 1; day <= MAX_DAY; day++) {
        int temp = 0;
        bool flag = true;
        int i = upper_bound(a, a + n + 1, day) - a;
        for( ; i <= n; i++) {
            if(a[i] % day) temp += (a[i] / day);
            else temp += ((a[i] / day) - 1);
            if(day + temp > MAX_DAY) {
                flag = false; break;
            }
        }
        if(flag) ans = min(ans, day + temp);
    }
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        int maxNum = 0;
        for(int i = 1; i <= n; i++)
            scanf("%d", &a[i]);
        sort(a + 1, a + 1 + n);
        ans = INT_MAX;
        judge(a[n]);
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}


