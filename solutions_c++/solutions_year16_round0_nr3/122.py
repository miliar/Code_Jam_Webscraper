#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 100005;
LL power[40][40] , g[40];
int ca;

int n , m;

int main() {
    cin >> n >> m;
    printf("Case #%d:\n" , ++ ca);
    for (int i = 0 ; i < 40 ; ++ i) {
        power[i][0] = 1;
        for (int j = 1 ; j < 40 ; ++ j)
            power[i][j] = power[i][j - 1] * i;
    }
    int cnt = 0 , mask = 1 << ((n >> 1) - 1);    
    for (int i = 0 ; i < mask ; ++ i) {
        for (int j = 0 ; j < mask ; ++ j) {
            int x = i + mask;
            int y = j + j | 1;

            bool flag = 1;
            for (int k = 2 ; k <= 10 ; ++ k) {
                LL a = 0;
                for (int w = 0 ; w < n / 2 ; ++ w)
                    if (x >> w & 1)
                        a += power[k][w];
                LL b = 0;
                for (int w = 0 ; w < n / 2 ; ++ w)
                    if (y >> w & 1)
                        b += power[k][w];
                g[k] = __gcd(a , b);                
                if (g[k] == 1) {
                    flag = 0;
                    break;
                }
            }
            if (!flag)
                continue;
            int z = x << (n / 2) | y;
            for (int k = n - 1 ; k >= 0 ; -- k)
                putchar('0' + (z >> k & 1));
            for (int k = 2 ; k <= 10 ; ++ k)
                printf(" %lld" , g[k]);
            puts("");
            if (++ cnt == m)
                return 0;
        }
        
    }
    printf("%d\n" , cnt);
    return 0;
}
