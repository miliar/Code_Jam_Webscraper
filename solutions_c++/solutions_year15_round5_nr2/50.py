/*
 * dnkywin's template
 */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

int m, n;

ll sums[1005];
ll diffs[1005];
ll mindiffs[105];
ll maxdiffs[105];

ll k;
void solve_case(int test_case) {
    cout << "Case #" << test_case << ": ";
    /* %%% */
    cin >> n >> k;
    mset(mindiffs, 0);
    mset(maxdiffs, 0);
    mset(diffs, 0);
    rep(i, n - k + 1) {
        cin >> sums[i];
        if (i) {
            diffs[i - 1] = sums[i] - sums[i - 1];
        }
    }
    rep(mo, k) {
        ll tdiff = 0;
        for (int i = mo; i < n - k; i += k) {
            tdiff += diffs[i];
            mindiffs[mo] = min(mindiffs[mo], tdiff);
            maxdiffs[mo] = max(maxdiffs[mo], tdiff);
        }
        //cout << "Class " << mo << ": " << mindiffs[mo] << " " << maxdiffs[mo] << endl;
    }

    ll targsum = sums[0];
    ll maxdiff = 0;
    rep(i, k) {
        maxdiffs[i] -= mindiffs[i];
        targsum += mindiffs[i];
        maxdiff = max(maxdiffs[i], maxdiff);
    }
    ll wiggle = 0;
    rep(i, k) {
        wiggle += maxdiff - maxdiffs[i];
    }
    ll ans = maxdiff;
    if (wiggle < (targsum + k * (1LL << 50)) % k) {
        ans++;
    }
    cout << ans;
    cout << "\n";
}

int main(){
    int T;
    cin >> T;
    rep(tt, T) solve_case(tt + 1);
    return 0;
}

