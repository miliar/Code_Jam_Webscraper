#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 200005;

int n , ca , a[N];

void work() {
    int i , j , x = 0 , s1 = 0 , s2 = 0;
    scanf("%d" , &n);
    for (i = 0 ; i < n ; ++ i)
        scanf("%d" , &a[i]);
    for (i = 1 ; i < n ; ++ i)
        if (a[i] < a[i - 1]) {
            s1 += a[i - 1] - a[i];
            x = max(x , a[i - 1] - a[i]);
        }
    for (i = 1 ; i < n ; ++ i)
        s2 += min(x , a[i - 1]);
    printf("Case #%d: %d %d\n" , ++ ca , s1 , s2);
}

int main() {
    freopen("A-large.in" , "r" , stdin);
    freopen("1" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
