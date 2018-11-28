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

void solve(int test_number) {
    string s;
    cin >> s;
    int res = 0;
    for (int i = 1; i < (int)s.length(); i++) {
        if (s[i] != s[i - 1]) {
            res++;
        }
    }
    if (s.back() == '-')
        res++;
    cout << "Case #" << test_number << ": " << res << endl;
}

