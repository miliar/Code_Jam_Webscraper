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

const int MAXN = 5;

int n;
int a1[MAXN][MAXN];
int a[MAXN][MAXN];
int order[MAXN];
bool used[MAXN];

inline bool check(int pos) {
    if (pos == n) {
        return true;
    } else {
        bool res = true;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (!used[i] && a[order[pos]][i]) {
                used[i] = true;
                res = res & check(pos + 1);
                used[i] = false;
                cnt++;
            }
        }
        return res & (cnt != 0);
    }
}

void solve(int test_number) {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            a[i][j] = s[j] - '0';
            a1[i][j] = a[i][j];
        }
    }        
    int res = INF;

    for (int msk = 0; msk < (1 << (n * n)); msk++) {
        int cur = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (msk & (1 << (i * n + j))) {
                    a[i][j] = 1;
                    cur++;
                } else {
                    a[i][j] = a1[i][j];
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            order[i] = i;
        }
        memset(used, 0, sizeof(used));
        bool flag = true;
        do {
            if (!check(0)) {
                flag = false;
                break;
            }
        } while (next_permutation(order, order + n));
        if (flag) {
            res = min(res, cur);
        }
    }

    cout << "Case #" << test_number << ": " << res << endl;
    cerr << test_number << endl;
}
