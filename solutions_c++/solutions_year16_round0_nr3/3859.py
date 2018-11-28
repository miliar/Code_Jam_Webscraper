#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string.h>
#include <iostream>
#include <time.h>
using namespace std;
typedef long long LL;
vector<LL> p;
const int maxn = 1 << 20;
bool vis[maxn];
void init() {
    for (int i = 2; i < maxn; ++i) {
        if (vis[i]) continue;
        p.push_back(i);
        for (int j = i; j < maxn; j += j) vis[j] = true;
    }
}
LL mult_mod(LL a, LL b, LL c) {
    a %= c;
    b %= c;
    LL ret = 0;
    LL tmp = a;
    while (b) {
        if (b & 1) {
            ret += tmp;
            if (ret > c) ret -= c;
        }
        tmp <<= 1;
        if (tmp > c) tmp -= c;
        b >>= 1;
    }
    return ret;
}
LL pow_mod(LL a, LL n, LL mod) {
    LL ret = 1LL;
    LL temp = a % mod;
    while (n) {
        if (n & 1) ret = mult_mod(ret, temp, mod);
        temp = mult_mod(temp, temp, mod);
        n >>= 1;
    }
    return ret;
}
bool check(LL a, LL n, LL x, LL t) {
    LL ret = pow_mod(a, x, n);
    LL last = ret;
    for (int i = 1; i <= t; ++i) {
        ret = mult_mod(ret, ret, n);
        if (ret == 1 && last != 1 && last != n-1) return true;
        last = ret;
    }
    if (ret != 1) return true;
    else return false;
}
bool MB(LL n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if ((n & 1) == 0) return false;
    LL x = n - 1;
    LL t = 0;
    while ((x & 1) == 0) {
        x >>= 1;
        ++t;
    }
    srand(time(NULL));
    for (int i = 0; i < 30; ++i) {
        LL a = rand() % (n - 1) + 1;
        if (check(a, n, x, t)) return false;
    }
    return true;
}
int T, tt, n, m;
LL num[12];
LL sum[40];
void output(LL k) {
    for (int i = 0; i < p.size(); ++i) {
        LL sp = p[i];
        if (k % sp == 0) {
            cout << " " << sp;
            return;
        }
    }
    cout << " haha ";
}
bool pan(LL k) {
    for (int i = 2; i <= 10; ++i) num[i] = 0LL;
    LL d = k;
    for (int i = 0; i < n; ++i) {
        if (d % 2 == 0) sum[i] = 0LL;
        else sum[i] = 1LL;
        d /= 2LL;
    }
    for (int i = n - 1; i >= 0; --i) {
        for (int j = 2; j <= 10; ++j) {
            num[j] = num[j] * (LL)j + sum[i];
        }
    }
    for (int i = 2; i <= 10; ++i) {
        if (MB(num[i])) return false;
    }
    for (int i = n - 1; i >= 0; --i) cout << sum[i];
    for (int i = 2; i <= 10; ++i) {
        output(num[i]);
    }
    cout << "\n";
    return true;
}
int main() {

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    init();
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &n, &m);
        printf("Case #%d:\n", ++tt);
        LL s = (1LL << (n - 1LL)) | 1LL;
        while (m) {
            if (pan(s)) --m;
            s += 2;
        }
    }
    return 0;
}
