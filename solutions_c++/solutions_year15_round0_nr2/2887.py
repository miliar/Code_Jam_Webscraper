#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

int a[1010];

int main() {
    freopen("B-large.in.txt", "r", stdin);
    freopen("bb.out", "w", stdout);
    int T; scanf("%d", &T);
    int cas = 0;
    while (T--) {
        int n; scanf("%d", &n);
        int mm = 0;
        for (int i=1; i<=n; ++i) {
            scanf("%d", &a[i]);
            if (mm < a[i]) mm = a[i];
        }
        int ans = 0x7fffffff;
        for (int i=1; i<=mm; ++i) {
            int ans1 = 0;
            for (int j=1; j<=n; ++j) {
                if (a[j] > i) {
                    ans1 += a[j] / i;
                    if (a[j] % i == 0) ans1--;
                }
            }
            ans1 += i;
            //printf("%d\n", ans1);
            if (ans > ans1) ans = ans1; 
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
