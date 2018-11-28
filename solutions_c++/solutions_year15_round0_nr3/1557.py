#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 10000005

enum _Q { _1, _i, _j, _k };

struct Q {
    _Q x;
    int sign;
    Q () {}
    Q (_Q x, int sign = 1) : x(x), sign(sign) {}
    Q operator* (const Q& o) const {
        if (x == _1)
            return Q(o.x, sign * o.sign);
        if (o.x == _1)
            return Q(x, sign * o.sign);
        if (x == o.x)
            return Q(_1, -1 * sign * o.sign);
        if (x == _i) {
            if (o.x == _j)
                return Q(_k, sign * o.sign);
            return Q(_j, -1 * sign * o.sign);
        }
        if (x == _j) {
            if (o.x == _i)
                return Q(_k, -1 * sign * o.sign);
            return Q(_i, sign * o.sign);
        }
        if (o.x == _i)
            return Q(_j, sign * o.sign);
        return Q(_i, -1 * sign * o.sign);
    }
    bool operator== (const Q& o) const {
        return x == o.x && sign == o.sign;
    }
};

const Q Q_1(_1), Q_i(_i), Q_j(_j), Q_k(_k);
const Q q[4] = { Q_1, Q_i, Q_j, Q_k };

long long l, x;
char s[MAX];
Q a[MAX], left[MAX], right[MAX], all[4];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld %lld %s", &l, &x, s+1);
        for (long long i = 1; i <= l; i++)
            a[i] = q[s[i] - 'i' + 1];
        left[0] = Q_1;
        for (long long i = 1; i <= l; i++)
            left[i] = left[i-1] * a[i];
        right[l+1] = Q_1;
        for (long long i = l; i >= 1; i--)
            right[i] = a[i] * right[i+1];
        all[0] = Q_1;
        for (int i = 1; i < 4; i++)
            all[i] = all[i-1] * right[1];
        long long first_i = l * x + 10;
        for (long long i = 1; i <= l; i++) {
            if (left[i] == Q_i)
                first_i = min(first_i, i);
            if (x > 1 && all[1] * left[i] == Q_i)
                first_i = min(first_i, l + i);
            if (x > 2 && all[2] * left[i] == Q_i)
                first_i = min(first_i, l + l + i);
            if (x > 3 && all[3] * left[i] == Q_i)
                first_i = min(first_i, l + l + l + i);
        }
        long long last_kk = -1;
        for (long long i = l; i >= 1; i--) {
            if (right[i] == Q_k && all[(x-1) % 4] * left[i-1] == Q_k)
                last_kk = max(last_kk, (x-1)*l + (i-1));
            if (x > 1 && right[i] * all[1] == Q_k && all[(x-2) % 4] * left[i-1] == Q_k)
                last_kk = max(last_kk, (x-2)*l + (i-1));
            if (x > 2 && right[i] * all[2] == Q_k && all[(x-3) % 4] * left[i-1] == Q_k)
                last_kk = max(last_kk, (x-3)*l + (i-1));
            if (x > 3 && right[i] * all[3] == Q_k && all[(x-4) % 4] * left[i-1] == Q_k)
                last_kk = max(last_kk, (x-4)*l + (i-1));
        }
        printf("Case #%d: ", t);
        if (first_i == -1 || last_kk == -1 || last_kk < first_i)
            puts("NO");
        else
            puts("YES");
    }
}
