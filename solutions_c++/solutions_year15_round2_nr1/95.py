#include <bits/stdc++.h>
using namespace std;

typedef long long int64;

int64 f[10000000];
vector<int64> q;

int64 reverse(int64 n) {
    int64 ret = 0;
    while (n > 0) {
        ret = ret * 10 + n % 10;
        n /= 10;
    }
    return ret;
}

int64 greedy(int64 n) {
    int64 k = 1, ret = 1;
    while (k < n) {
        bool is_reverse = true;
        int64 add = 1;
        while (add <= k) {
            if (k + add <= n && reverse(k + add) <= n && reverse(k + add) - reverse(k) > add) {
                k += add;
                is_reverse = false;
                ret += add;
                break;
            }
            add *= 10;
        }
        if (k < n && is_reverse) {
            if (reverse(k) > k && reverse(k) <= n)
                k = reverse(k);
            else
                k++;
            ret++;
        }
    }
    return ret;
}

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    memset(f, 63, sizeof f);
    f[1] = 1;
    q.push_back(1);

    for (int i = 0; i < q.size(); i++) {
        int64 v = q[i];
        if (v < 1000000 && f[v + 1] > f[v] + 1) {
            f[v + 1] = f[v] + 1;
            q.push_back(v + 1);
        }
        if (f[reverse(v)] > f[v] + 1) {
            f[reverse(v)] = f[v] + 1;
            q.push_back(reverse(v));
        }
    }

    int nTest;
    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++) {
        int64 n;
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", test, greedy(n));
        // printf("Case #%d: %lld\n", test, f[n]);
    }

    return 0;
}
