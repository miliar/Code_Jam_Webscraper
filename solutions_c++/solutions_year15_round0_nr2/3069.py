#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int a[1005];

int gao() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) scanf("%d", &a[i]);
    sort(a, a + n);
    int ans = a[n-1];
    for(int block = 2; block <= a[n-1]; block ++) {
        int cnt = 0;
        for(int i = 0; i < n; i ++) if(a[i] > block) {
            if(a[i] % block == 0) cnt += a[i] / block - 1;
            else cnt += a[i] / block;
        }
        //printf("block=%d, cnt=%d\n", block, cnt);
        ans = min(ans, cnt + block);
    }
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase ++) {
        printf("Case #%d: %d\n", kase, gao());
    }
    return 0;
}
