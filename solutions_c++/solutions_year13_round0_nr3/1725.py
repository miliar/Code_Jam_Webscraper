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
const int N = 1111;
int sum[N];
vector<ll> vec;

ll check(ll x) {
    int tot = 0;
    int digit[20];
    while (x) {
        digit[tot++] = x % 10;
        x /= 10;
    }
    for (int i = 0; i < tot; i++) {
        if (digit[i] != digit[tot - 1 - i]) return false;
    }
    return true;
}

void init() {
    vec.clear();
    for (ll i = 1; i <= 10000000LL; i++) {
        if (check(i) && check(i * i)) vec.pb(i * i);
    }
}

int main() {
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.txt", "w", stdout);
    init();
    int T, Case = 1;
    cin >> T;
    ll A, B;
    while (T--) {
        cin >> A >> B;
        int ans = 0;
        for (int i = 0; i < vec.size(); i++) {
            if (vec[i] >= A && vec[i] <= B) ans++;
        }
        printf("Case #%d: ", Case++);
        cout << ans << endl;
    }
    return 0;
}
