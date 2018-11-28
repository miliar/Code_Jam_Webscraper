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

const int X = 1024;

int n, x, hist[X];

void input()
{
    memset(hist, 0, sizeof(hist));

    cin >> n >> x;
    rep(i, n) {
        int s;
        cin >> s;
        ++hist[s];
    }
}

void solve()
{
    int ans = 0;
    for (int i = x; i > 0; --i) {
        for (int j = min(x - i, i - 1); j > 0; --j) {
            int d = min(hist[j], hist[i]);
            ans += d;
            hist[j] -= d;
            hist[i] -= d;
        }
        if (2 * i <= x) ans += (hist[i] + 1) / 2;
        else ans += hist[i];
        hist[i] = 0;
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
