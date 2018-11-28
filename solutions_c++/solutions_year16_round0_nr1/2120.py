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

typedef long long li;

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

const li D = 10;
const li OVER = 1000;

bool used[D];
int unused;

inline void run(li m) {
    while (m > 0) {
        li d = m % 10;
        m /= 10;
        if (!used[d]) {
            unused--;
            used[d] = true;
        }
    }
}

void solve(int test_number) {
    cout << "Case #" << test_number << ": ";
    li n;
    cin >> n;
    memset(used, 0, sizeof(used));
    unused = D;
    li cur = 1;
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }
    while (cur < OVER) {
        li m = n * cur;
        run(m);
        if (unused == 0) {
            cout << n * cur << endl;
            return ;
        }
        cur++;
    }
    cout << "INSOMNIA" << endl;
}

