#include <bits/stdc++.h>

using namespace std;

#define long int64_t

#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=a;i<(b);++i)
#define all(u) begin(u),end(u)
#define rall(u) (u).rbegin(),(u).rend()
#define uniq(u) (u).erase(unique(all(u)),end(u))

#define mp make_pair
#define pb push_back
#define eb emplace_back

const int N = 1024;

int n, a[N];

void input()
{
    cin >> n;
    rep(i, n) cin >> a[i];
}

void solve()
{
    int ans = 0;

    int l = 0, r = n;
    rep(i, n) {
        int mn = l;
        repi(j, l, r) if (a[j] < a[mn]) {
            mn = j;
        }

        int ls = mn - l, rs = r - mn - 1;
        if (ls < rs) {
            rep(j, ls) {
                swap(a[mn - j], a[mn - j - 1]);
            }
            ans += ls, ++l;
        } else {
            rep(j, rs) {
                swap(a[mn + j], a[mn + j + 1]);
            }
            ans += rs, --r;
        }
    }

    cout << ans << endl;
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int T, cnt = 0;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << ++cnt << ": ";
        input();
        solve();
    }

    return 0;
}
