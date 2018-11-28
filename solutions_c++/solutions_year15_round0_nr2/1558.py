#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 200005;
int ca;
int n , a[N];

void work() {
    int i , j;
    scanf("%d" , &n);
    priority_queue<int> Q;
    for (i = 0 ; i < n ; ++ i) {
        scanf("%d" , &a[i]);
    }
    int res = 1 << 30;
    for (i = 1 ; i <= 1000 ; ++ i) {
        int x = 0;
        for (j = 0 ; j < n ; ++ j)
            x += (a[j] + i - 1) / i - 1;
        res = min(res , x + i);
    }
    printf("Case #%d: %d\n" , ++ ca , res);
}

int main() {
    freopen("1.out" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
