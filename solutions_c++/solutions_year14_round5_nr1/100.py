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

const int N = 1000010;

long n, p, q, r, s, a[N], S;

void input()
{
    cin >> n >> p >> q >> r >> s;
    rep(i, n) a[i] = (i * p + q) % r + s;
    S = accumulate(a, a + n, 0LL);
}

bool can(long m)
{
    int cnt = 1;
    long cur = 0;
    rep(i, n) {
        if (a[i] > m) return false;
        cur += a[i];
        if (cur > m) {
            ++cnt, cur = a[i];
            if (cnt > 3) return false;
        }
    }
    return true;
}

long solve()
{
    if (n == 1) return 0;
    if (n == 2) return min(a[0], a[1]);

    long l = 0, r = 1e16;
    while (l + 1 < r) {
        long m = (l + r) / 2;
        if (can(m)) r = m;
        else l = m;
    }
    return S - r;
}

int main()
{
    int T;
    cin >> T;
    rep(i, T) {
        input();

        cout << "Case #" << i + 1 << ": ";
        double ans = (double) solve() / S;
        printf("%.10f\n", ans);
    }

    return 0;
}
