#include <bits/stdc++.h>

#define mp make_pair
#define fs first
#define sc second
#define pb push_back
#define eb emplace_back

#define y0 yy0
#define y1 yy1
#define next _next
#define prev _prev
#define link _link
#define hash _hash

#define sz(s) int((s).size())
#define len(s) int((s).size())
#define all(s) (s).begin(), (s).end()

#ifdef WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ll lINF = 1e18;
const double EPS = 1e-12;

using namespace std;

struct quat{
    int a;
    quat(char c = '1') {
        if (c == '1') {
            a = 0;
        } else if (c == 'i') {
            a = 1;
        } else if (c == 'j') {
            a = 2;
        } else if (c == 'k') {
            a = 3;
        }
    }
    quat(int i) {
        a = i;
    }
    quat operator*(quat b) {
        int ans = 0;
        int c = a & 3, d = b.a & 3;
        if (c == 0) {
            ans = d;
        } else if (d == 0) {
            ans = c;
        } else if (c == d) {
            ans = 4;
        } else if (c == 1 && d == 2) {
            ans = 3;
        } else if (c == 2 && d == 3) {
            ans = 1;
        } else if (c == 3 && d == 1) {
            ans = 2;
        } else if (c == 2 && d == 1) {
            ans = 3 + 4;
        } else if (c == 3 && d == 2) {
            ans = 1 + 4;
        } else if (c == 1 && d == 3) {
            ans = 2 + 4;
        }
        if (((a & 4) != 0) ^ ((b.a & 4) != 0)) {
            ans ^= 4;
        }
        return quat(ans);
    }

    bool operator==(quat b) {
        return a == b.a;
    }
};

quat power(quat a, ll x) {
    x = x % 4;
    quat ans(0);
    for (int i = 0; i < x; i++) {
        ans = ans * a;
    }
    return ans;
}

const int N = 11111;

int ttt, l;
ll x;
char s[N];

int main()
{
#ifdef DEBUG
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
#endif

    scanf("%d", &ttt);

    for (int tt = 1; tt <= ttt; tt++) {
        scanf("%d"LLD" ", &l, &x);
        scanf("%s", s);
        printf("Case #%d: ", tt);
        quat prod(0), prod_all(0);
        for (int i = 0; i < l; i++) {
            prod = prod * quat(s[i]);
        }
        prod_all = power(prod, x);
//        cout << prod.a << ' ' << prod_all.a << endl;
        ll mn = lINF, mx = -lINF;
        quat i('i'), j('j'), k('k'), cur(0);
        for (int r = 0; r < l; r++) {
            quat cur2 = cur;
            for (int q = 0; q < 4 && r + l * q <= l * x; q++) {
                if (cur2 == i) {
                    mn = min(mn, r + l * q + 0ll);
                }
                cur2 = prod * cur2;
            }
            cur = cur * quat(s[r]);
        }
        cur = quat(0);
        for (int r = 0; r < l; r++) {
            quat cur2 = cur;
            for (int q = 0; q < 4 && r + l * q <= l * x; q++) {
                if (cur2 == k) {
                    mx = max(mx, x * l - r - l * q);
                }
                cur2 = cur2 * prod;
            }
            cur = quat(s[l - 1 - r]) * cur;
        }
//        cout << mn << ' ' << mx << endl;
        if (mx > mn && prod_all == i * j * k) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
