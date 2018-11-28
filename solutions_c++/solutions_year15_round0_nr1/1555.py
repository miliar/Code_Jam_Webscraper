#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 200005;
int ca;
int n;
char str[N];

void work() {
    printf("Case #%d: " , ++ ca);
    int i , j , x , y = 0 , res = 0;
    scanf("%d%s" , &n , str);
    for (i = 0 ; i <= n ; ++ i) {
        x = str[i] - '0';
        if (y + res >= i)
            y += x;
        else {
            res = max(res , i - y);
            y += x;
        }
    }
    cout << res << endl;
}

int main() {
    freopen("1.out" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
