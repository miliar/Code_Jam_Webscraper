#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

typedef pair<int, int> PII;

int T;
int n, p;

bool check0(long long x) {
    long long ret = 0;
    long long u = x;
    long long d = (1ll << n) - x - 1;
    while (u || d) {
        if (u) {
            ret <<= 1;
            ++ret;
            --u;
            u >>= 1;
            d = (d + 1) >> 1;
        } else {
            ret <<= 1;
            d >>= 1;
        }
    }
    return ret <= p;
}

bool check1(long long x) {
    long long ret = 0;
    long long u = x;
    long long d = (1ll << n) - x - 1;
    while (u || d) {
        if (d) {
            ret <<= 1;
            --d;
            d >>= 1;
            u = (u + 1) >> 1;
        } else {
            ret <<= 1;
            ++ret;
            u >>= 1;
        }
    }
    return ret <= p;
}

int main() {
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        scanf("%d%d", &n, &p);
        --p;
        long long l = 0, r = (1ll << n);
        while (l + 1 < r) {
            long long m = (l + r) >> 1;
            if (check0(m)) {
                l = m;
            } else {
                r = m;
            }
        }
        long long ans0 = l;
        l = 0, r = (1ll << n);
        while (l + 1 < r) {
            long long m = (l + r) >> 1;
            if (check1(m)) {
                l = m;
            } else {
                r = m;
            }
        }
        printf("Case #%d: %I64d %I64d\n", test, ans0, l);
    }
    return 0;
}

