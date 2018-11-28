#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "vector"
#include "queue"
#include "stack"
#include "cmath"
#include "string"
#include "cctype"
#include "map"
#include "iomanip"
#include "set"
#include "utility"
using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
const int inf = 1 << 29;
const double dinf = 1e30;
const ll linf = 1LL << 55;

ll n, p;
ll all;

ll getBadest(ll sum, ll cnt) {
    if (cnt == 0) return 1;
    return sum / 2 + getBadest(sum / 2, (cnt - 1) / 2);
}

ll getBest(ll sum, ll cnt) {
    if (cnt == 0) return 0;
    return sum / 2 + getBest(sum / 2, (cnt - 1) / 2);
    //return sum / 2 + getBest(sum / 2, cnt / 2);
}
bool check1(ll mid) {
    return getBadest(all, mid) <= p;
}

bool check2(ll mid) {
    return all - getBest(all, all - 1 - mid) <= p;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("bout.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> p;
        all = 1LL << n;
        ll l = 0, r = all - 1;
        ll ans1 = -1, ans2 = -1;
        while (l <= r) {
            ll mid = (l + r) >> 1;
            if (check1(mid)) ans1 = mid, l = mid + 1;
            else r = mid - 1;
        }
        l = 0, r = all - 1;
        while (l <= r) {
            ll mid = (l + r) >> 1;
            if (check2(mid)) ans2 = mid, l = mid + 1;
            else r = mid - 1;
        }
        printf("Case #%d: ", Case++);
        cout << ans1 << " " << ans2 << endl;
    }
    return 0;
}
