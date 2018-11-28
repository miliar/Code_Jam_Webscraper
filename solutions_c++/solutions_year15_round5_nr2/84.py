#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <utility>
#include <functional>

using namespace std;

typedef long long ll;

vector< ll > a, b;
int n, k;
ll c;

ll
up(ll p, ll q)
{
    if (p >= 0) {
        return (p + q - 1) / q;
    } else if (p % q == 0) {
        return p / q;
    }
    return -((-p) / q);
}

ll
down(ll p, ll q)
{
    if (p >= 0 || p % q == 0) {
        return p / q;
    }
    return -((-p) / q + 1);
}

bool
can(ll diff, int pos)
{
    for (int i = 0; i < k; ++i) {
        if (b[i] - a[i] > diff) {
            return false;
        }
    }
    ll sum_r = 0ll, sum_l = 0ll;
    for (int i = 0; i < k; ++i) {
        if (i == pos) {
            continue;
        }
        sum_l += a[i] + diff - b[pos];
        sum_r += b[i] - b[pos];
    }
    return (sum_l - sum_r >= k) 
        || up(c + sum_r, k) <= down(c + sum_l, k);
}

void
process(int id)
{
    cin >> n >> k;
    vector< ll > sums(n - k + 1);
    vector< ll > diff(n, 0ll);
    for (int i = 0; i < n - k + 1; ++i) {
        cin >> sums[i];
    }
    a.assign(k, 0);
    b.assign(k, 0);
    for (int i = 0; i < n - k; ++i) {
        diff[i + k] = diff[i] + sums[i + 1] - sums[i];
    }
    for (int pos = 0; pos < k; ++pos) {
        int id = pos;
        do {
            a[pos] = min(a[pos], diff[id]);
            b[pos] = max(b[pos], diff[id]);
            id += k;
        } while (id < n);
    }
    c = sums[0];
    ll l = -1, r = 0;
    // fing right border
    {
        vector< ll > x(n, 0);
        x[0] = sums[0];
        for (int i = k; i < n; ++i) {
            x[i] = x[i % k] + diff[i];
        }
        auto it = std::minmax_element(x.begin(), x.end());
        r = *(it.second) - *(it.first);
        assert(r >= 0);
    }
    while (l < r - 1) {
        ll mid = (l + r) / 2;
        bool ok = false;
        for (int i = 0; i < k && !ok; ++i) {
            if (can(mid, i)) {
                ok = true;
            }
        }
        if (ok) {
            r = mid;
        } else {
            l = mid;
        }
    }
    ll ans = r;
    cout << "Case #" << id << ": " << ans << '\n';
}

int
main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        process(i + 1);
    }
    return 0;
}
