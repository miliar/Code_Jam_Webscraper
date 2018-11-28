#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll pList[20];

inline ll convert(ll n, int m);


inline bool isPrime(ll n);

inline bool prime(ll x, int idx);

inline ll convertTo(ll n);

int main() {
#ifdef LOCAL
    freopen("/Users/yew1eb/ClionProjects/CppGo/in.txt", "r", stdin);
    freopen("/Users/yew1eb/ClionProjects/CppGo/out.txt", "w", stdout);
#endif
    int T, N, J;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        printf("Case #%d:\n", cas);
        scanf("%d%d", &N, &J);
        ll start = 1L << (N - 1);
        ll end = 1L << N;
        //cout<<start<<" "<<end<<endl;
        ll key;
        for (ll i = start + 1; i < end; i += 2) {
            key = convertTo(i);
            //if(key != 100111) continue;
            if (isPrime(key)) {
                continue;
            }

            printf("%lld", key);
            for (int j = 2; j <= 10; ++j) {
                printf(" %d", pList[j]);
            }
            printf("\n");
            if (--J <= 0) break;
        }
    }
    return 0;
}

inline ll convertTo(ll n) {
    ll ret = 0;
    ll base = 1;
    while (n > 0) {
        ret += (n & 1) * base;
        n >>= 1;
        base *= 10;
    }
    return ret;
}

inline bool isPrime(ll n) {
    for (int i = 2; i <= 10; ++i) {
        ll x = convert(n, i);
        //printf("%d i=%d\n", x, i);
        if (prime(x, i)) {
            return true;
        }
    }
    return false;
}

inline bool prime(ll x, int idx) {
    for (int i = 2; i <= x / i; ++i) {
        if (x % i == 0) {
            pList[idx] = i;
            return false;
        }
    }
    return true;
}

inline ll convert(ll n, int m) {
    ll ret = 0;
    ll base = 1;
    while (n > 0) {
        ret += (n % 10) * base;
        n /= 10;
        base *= m;
    }
    return ret;
}
