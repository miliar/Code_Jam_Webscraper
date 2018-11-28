#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 200005;

int n , ca , a[N] , m , b[N];

LL cal(LL t) {
    LL s = 0;
    for (int i = 0 ; i < n ; ++ i) {
        s += (t + a[i] - 1) / a[i];
    }
    return s;
}

void work() {
    scanf("%d%d",&n,&m);
    for (int i = 0 ; i < n ; ++ i)
        scanf("%d" , &a[i]);
    LL l = 0 , r = 1e18 , mid;
    while (l < r) {
        mid = l + r + 1 >> 1;
        if (cal(mid) < m)
            l = mid;
        else
            r = mid - 1;
    }
    int x = m - cal(l);
    for (int i = 0 ; i < n ; ++ i)
        if (l % a[i] == 0) {
            if (!-- x) {
                printf("Case #%d: %d\n" , ++ ca , i + 1);
                return;
            }
        }    
}

int main() {
    freopen("/home/sd0061/下载/B-large.in" , "r" , stdin);
    freopen("1" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
