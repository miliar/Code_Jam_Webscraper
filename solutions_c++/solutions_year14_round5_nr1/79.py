#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef pair <int, int> PII;
const int N = 1e7 + 5;
int Tc;
ll n, p, q, r, ss;
int a[N];
ll s[N];

int main() {
    scanf("%d", &Tc);
    rep (ri, Tc) {
        printf("Case #%d: ", ri + 1);
        cin >> n >> p >> q >> r >> ss;
        rep (i, n) {
            a[i] = (i * (ll)(p) + q) % r + ss;
        }
        s[0] = 0;
        rep (i, n) s[i + 1] = s[i] + a[i];
        ll ans = 0;
        ll l = 0, r = s[n];
        while (l < r) {
            ll mid = (l + r) / 2;
            int i = 1, j = n;
            while (i <= n && s[i] <= mid) i++;
            while (j >= 1 && s[n] - s[j - 1] <= mid) j--;
            if (i > j || s[j] - s[i - 1] <= mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        ans = s[n] - l;
        /*
        rep (a, n) {
            for (int b = a; b < n; b++) {
                ll tmp = 0;
                if (a > 0) tmp = max(tmp, s[a]);
                if (b < n - 1) tmp = max(tmp, s[n] - s[b + 1]);
                tmp = max(tmp, s[b + 1] - s[a]);
                ans = max(ans, s[n] - tmp);
            }
        }
        */
        cout << fixed << setprecision(12) << ans / (double)(s[n]) << endl;
    }
}

