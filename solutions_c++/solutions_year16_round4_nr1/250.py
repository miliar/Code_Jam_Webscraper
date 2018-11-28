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

const int MAXN = 1001000;

int n;
int a[3];
string s[MAXN];

void build(int v, int vl, int vr, int val) {
    if (vl + 1 == vr) {
        a[val]--;
        if (val == 0) {
            s[v] = "P";
        } else if (val == 1) {
            s[v] = "R";
        } else {
            s[v] = "S";
        }
        return;
    }
    int d = (vl + vr) / 2;
    int l = val, r = (val + 1) % 3; 
    build(2 * v, vl, d, l);
    build(2 * v + 1, d, vr, r);
    s[v] = min(s[v * 2] + s[v * 2 + 1], s[v * 2 + 1] + s[v * 2]);
}

string build(int t) {
    build(1, 0, (1 << n), t);
    for (int i = 0; i < 3; i++) {
        if (a[i] < 0)
            return "";
    }
    return s[1];
}

void solve(int test_number) {
    int a[3];
    cin >> n >> a[1] >> a[0] >> a[2];
    cout << "Case #" << test_number << ": ";
    string ans = "ZZZ";
    for (int i = 0; i < 3; i++) {
        ::a[0] = a[0], ::a[1] = a[1], ::a[2] = a[2];
        string res = build(i);
        if (res != "") {
            ans = min(ans, res);
        }
    }
    if (ans == "ZZZ") {
        ans = "IMPOSSIBLE";
    }
    cout << ans << endl;
}

