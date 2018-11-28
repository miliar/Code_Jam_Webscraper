#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long lld;

const int N = 1e6 + 5;

int pow_mod(int x, int n, int mod) {
    int ret = 1 % mod;
    while (n) {
        if (n & 1) {
            ret = 1LL * ret * x % mod;
        }
        x = 1LL * x * x % mod; n >>= 1;
    }
    return ret;
}

int notprime(lld x, int k) {
    for (int i = 2; i < 10000 && i * i <= x; i++) {
        if ((pow_mod(k, 31, i) + x % i) % i == 0) {
            return i;
        }
    }
    return 0;
}

int isok(lld x, int n) {
    vector<int> ans;
    for (int k = 2; k <= 10; k++) {
        lld K = 1, tmp = 0;
        for (int i = 0; i < n; i++) {
            if (x >> i & 1) {
                tmp += K;
            }
            K *= k;
        }
        int tt = notprime(tmp, k);
        if (!tt) return 0;
        ans.push_back(tt);
    }
    int bit[32] = {}, len = 0;
    while (x) {
        bit[len++] = x % 2;
        x >>= 1;
    }
    reverse(bit, bit + 32);
    bit[0] = 1;
    for (int i = 0; i < 32; i++) printf("%d", bit[i]);
    for (int i = 0; i < 9; i++) printf(" %d", ans[i]); puts("");
    return 1;
}

void work(int cas) {
    int J, n;
    scanf("%d%d", &n, &J);
    printf("Case #%d:\n", cas);
    for (lld i = 1; ; i += 2) {
        if (isok(i, n)) {
            if (-- J == 0) break;
        }
    }
    return ;
}

#define TASK "C-large"

int main() {
    if (strlen(TASK)) {
        freopen(TASK".in", "r", stdin);
        freopen(TASK".out", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        work(cas);
    }
    return 0;
}
