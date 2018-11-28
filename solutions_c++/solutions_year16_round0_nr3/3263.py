#include <cstdio>
#include <queue>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <ctime>
#define LL long long
using namespace std;

const int N = 1000100, INF = 0x3f3f3f3f;

//LL res[N];
int d[4200];
int is[N], p[N], pn;

char s[N];

LL change (int x, int n, int y) {
    LL r = 0, t = 0;
//    while (x) {
//        t *= 2;
//        t += x % 2;
//        x /= 2;
//    }
    for (int i = 1; i <= n; i++) {
        t *= 2;
        t += x % 2;
        x /= 2;
//        cout << i << ' ' << x << endl;
    }
    x = t;
//    cout << x << endl;
//    cout << t << endl;
//    while (x) {
    for (int i = 1; i <= n; i++) {
        r *= y;
        if (x & 1) r++;
        x >>= 1;
    }
    return r;
}

int cal (LL x) {
    if (x <= 1000000000000LL) {
//    if (1) {
        for (int i = 2; 1LL * i * i <= x; i++) {
            if (x % i == 0) return i;
        }
        return 0;
    }
    for (int i = 1; i <= pn && 1LL * p[i] * p[i] <= x; i++) {
        if (x % p[i] == 0) return p[i];
    }
    return 0;
}

int jug (LL x, int n, int k, int p) {
    LL r = 0, t = 0;
//    while (x) {
//        t *= 2;
//        t += x % 2;
//        x /= 2;
//    }
    for (int i = 1; i <= n; i++) {
        t *= 2;
        t += x % 2;
        x /= 2;
//        cout << i << ' ' << x << endl;
    }
    x = t;
//    cout << x << endl;
//    cout << t << endl;
//    while (x) {
    for (int i = 1; i <= n; i++) {
        (r *= k) %= p;
        if (x & 1) (r += 1) %= p;
        x >>= 1;
    }
    return r == 0;
}

int jug (LL x, int n, int k) {
    if (n <= 16) return cal (change (x, n, k));
    for (int i = 1; i <= 1000; i++) if (jug (x, n, k, p[i])) return p[i];
//    if (jug (x, n, k, 2)) return 2;
//    if (jug (x, n, k, 3)) return 3;
//    if (jug (x, n, k, 5)) return 5;
    return 0;
}

void change2 (LL x, int n) {
    LL r = 0, t = 0;
//    while (x) {
//        t *= 2;
//        t += x % 2;
//        x /= 2;
//    }
    for (int i = 1; i <= n; i++) {
        t *= 2;
        t += x % 2;
        x /= 2;
//        cout << i << ' ' << x << endl;
    }
    x = t;
//    cout << x << endl;
//    cout << t << endl;
//    while (x) {
    for (int i = 1; i <= n; i++) {
//        r *= y;
        if (x & 1) cout << 1; else cout << 0;
        x >>= 1;
    }
//    return r;
}

int main () {
    freopen ("C-large.in", "r", stdin);
//    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    for (int i = 2; i < N; i++) if (!is[i]) {
        p[++pn] = i;
        for (int j = i; j < N; j += i) is[j] = 1;
    }
//    for (int i = 2; i <= 10; i++) cout << change (9, i) << ' ';
    int T, cas = 1;
    cin >> T;
//    cout << (int)'+' << ' ' << (int)'-' << endl;
    while (T--) {
        printf ("Case #%d:\n", cas++);
        int n, m;
        cin >> n >> m;
//        cout << (1 << n - 1) << ' ' << change ((1 << n - 1), n, 10) << endl;
//        return 0;
        for (LL i = (1LL << n - 1); i < (1LL << n); i++) if (i & 1) {
            int flag = 1;
            for (int j = 2; j <= 10 && flag; j++) {
//                if (cal (change (i, n, j)) == 0) {
                if (jug (i, n, j) == 0) {
                    flag = 0;
                }
            }
            if (flag) {
                change2 (i, n);
//                cout << change (i, n, 10);
//                for (int j = 2; j <= 10; j++) cout << " " << cal (change (i, n, j));
                for (int j = 2; j <= 10; j++) cout << " " << jug (i, n, j);
                cout << endl;
                m--;
            }
            if (!m) break;
        }
    }
}
