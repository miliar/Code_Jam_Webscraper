#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

char s[150];
typedef long long ll;
ll mod_mul(ll a, ll b, ll n) {
    ll res = 0;
    while(b) {
        if(b&1)    res = (res + a) % n;
        a = (a + a) % n;
        b >>= 1;
    }
    return res;
}
ll mod_exp(ll a, ll b, ll n) {
    ll res = 1;
    while(b) {
        if(b&1)    res = mod_mul(res, a, n);
        a = mod_mul(a, a, n);
        b >>= 1;
    }
    return res;
}
bool miller_rabin(ll n) {
    if(n == 2 || n == 3 || n == 5 || n == 7 || n == 11)    return true;
    if(n == 1 || !(n%2) || !(n%3) || !(n%5) || !(n%7) || !(n%11))    return false;

    ll x, pre, u;
    int i, j, k = 0;
    u = n - 1;

    while(!(u&1)) {
        k++; u >>= 1;
    }
    srand((ll)time(0));
    for(i = 0; i < 15; ++i) {
        x = rand()%(n-2) + 2;
        if((x%n) == 0)    continue;

        x = mod_exp(x, u, n);
        pre = x;
        for(j = 0; j < k; ++j) {
            x = mod_mul(x, x, n);
            if(x == 1 && pre != 1 && pre != n-1)    return false;
            pre = x;
        }
        if(x != 1)    return false;
    }
    return true;
}
ll getDivisor(ll d) {
    ll a = sqrt(d);
    for(ll i = 2; i <= a; i++) {
        if(d % i == 0) return i;
    }
}
ll L[55], bin[20];
void print(ll aaa, int n) {
    for(int i = n - 1; i >= 0; i--) {
        bin[i] = aaa % 2;
        aaa /= 2;
    }
    for(int i = 0; i < n; i++) printf("%d", bin[i]);
}
int main()
{
    #ifdef LOCAL
//    freopen("in.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif // LOCAL
    int T;
    T = 100;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        printf("Case #%d:\n", cas);
        int n, J, cnt = 0;
        scanf("%d%d", &n, &J);
        int k = n - 2, maxx = (1 << k) - 1;
        for(int i = 0; i <= maxx; i++) {
            int b = (i << 1) + 1 + (1 << (n - 1));
            ll d[15] = {0};
//            print(b, n);
//            puts("\n---\n");
            while(b) {
                for(int j = 2; j <= 10; j++) {
                    d[j] = d[j] * j + (b & 1);
                }
                b /= 2;
            }
            bool flag = true;
            for(int j = 2; j <= 10; j++) {
                if(miller_rabin(d[j])) {
//                    printf("%lld ", d[j]);
                    flag = false;
                }
            }
            if(flag) {
                print(d[2], n);
                for(int i = 2; i <= 10; i++) {
                    printf(" %d", getDivisor(d[i]));
                }
                puts("");
                cnt++;
                if(cnt >= J) break;
            }
        }
    }
    return 0;
}
