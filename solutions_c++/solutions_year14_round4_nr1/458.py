#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
const int N = 10000+10;
int a[N];
int n, s;
int main() {
    freopen("A-large (2).in","r",stdin);
    freopen("out.txt","w",stdout);
    int T, cas = 0; scanf("%d",&T);
    while (T--) {
        scanf("%d%d",&n,&s);
        for (int i = 0; i < n; i++) {
            scanf("%d",a+i);
        }
        sort(a, a+n);
        int l = 0, r = n-1;
        int ans = 0;
        while (l <= r) {
            if (l == r) {
                ans++; break;
            }
            if (a[l] + a[r] <= s) {
                l++; r--;
                ans++;
            }else {
                r--;
                ans++;
            }
        }
        printf("Case #%d: %d\n",++cas, ans);
    }
    return 0;
}
