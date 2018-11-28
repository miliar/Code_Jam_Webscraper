#include <bits/stdc++.h>

#define NAME "test"

#define EPS (1e-9)
#define INF ((int)(1e+9))
#define LINF ((long long)(1e+18))

#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef unsigned __int128 li;

void solve(int test_number);

int main() {
#ifdef _GEANY
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
    return 0;
}

const int MAXN = 33;
const int D = 12;

int n, m;
int a[MAXN];
li cur[D];
li p[D];
int w[D];

inline bool prime(li n, int num) {
    if (n % 3 == 0) {
        w[num] = 3;
        return false;
    }
    if (n % 5 == 0) {
        w[num] = 5;
        return false;
    }
    if (n % 7 == 0) {
        w[num] = 7;
        return false;
    }
    if (n % 11 == 0) {
        w[num] = 11;
        return false;
    }
    if (n % 13 == 0) {
        w[num] = 13;
        return false;
    }
    return true;
}

void rec(int pos) {
    if (pos <= n - 2) {
        for (int i = 2; i <= 10; i++) {
            p[i] *= (li)i;
        }
        a[pos] = 0;
        rec(pos + 1);

        for (int i = 2; i <= 10; i++) {
            cur[i] += p[i];
        }

        a[pos] = 1;
        rec(pos + 1);
        for (int i = 2; i <= 10; i++) {
            cur[i] -= p[i];
        }
        for (int i = 2; i <= 10; i++) {
            p[i] /= (li)i;
        }
    } else {
        for (int i = 2; i <= 10; i++) {
            p[i] *= (li)i;
        }
        for (int i = 2; i <= 10; i++) {
            cur[i] += p[i];
        }
        bool flag = true;
        for (int i = 2; i <= 10; i++) {
            if (prime(cur[i], i)) {
                flag = false;
                break;
            }
        }
        if (flag) {
            for (int i = n - 1; i >= 0; i--) {
                cout << a[i];
            }
            cout << ' ';
            for (int i = 2; i <= 10; i++) {
                cout << w[i] << ' ';
            }
            cout << "\n";
            m--;
            cerr << m << endl;
            if (m == 0) {
                exit(0);
            }
        }
        for (int i = 2; i <= 10; i++) {
            cur[i] -= p[i];
        }
        for (int i = 2; i <= 10; i++) {
            p[i] /= (li)i;
        }
    }
}

void solve(int test_number) {
    cin >> n >> m;
    cout << "Case #1:" << endl;
    a[0] = a[n - 1] = 1;
    for (int i = 0; i < D; i++) {
        cur[i] = 1;
        p[i] = 1;
    }
    rec(1);
}

