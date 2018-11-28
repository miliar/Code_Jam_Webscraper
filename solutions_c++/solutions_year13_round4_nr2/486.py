#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 2048

using namespace std;

typedef __int64 i64;

i64 win(int n, i64 x) {
    i64 t = (1LL << n) - x;
    int cnt = 0;
    for ( ; t; t >>= 1) ++cnt;
    return (1LL << (n - cnt + 1)) - 1LL;
}

i64 lose(int n, i64 x) {
    i64 t = x + 1;
    int cnt = 0;
    for ( ; t; t >>= 1) ++cnt;
    return (((1LL << (n - cnt + 1)) - 1LL) ^ ((1LL << n) - 1LL));
}

i64 getWorst(int n, i64 p) {
    i64 low = 0, high = (1LL << n) - 1, mid, ret = -1;

    while (low <= high) {
        mid = (low + high) >> 1;
        if (lose(n, mid) < p) {
            ret = mid; low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ret;
}

i64 getBest(int n, i64 p) {
    i64 low = 0, high = (1LL << n) - 1, mid, ret = -1;

    while (low <= high) {
        mid = (low + high) >> 1;
        if (win(n, mid) < p) {
            ret = mid; low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ret;
}

int main() {
    int t, ct = 0, n;
    i64 p;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        cin >> n >> p;
        printf("Case #%d: ", ++ct);
        cout << getWorst(n, p) << " " << getBest(n, p) << endl;
    }

    return 0;
}
