#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

typedef long long ll;

int e, r, n, ans;
int v[10], ene[10];

void check()
{
    int rem = e, gain = 0;
    rep (i, n) {
        rem -= ene[i];
        if (rem < 0) return;
        gain += v[i] * ene[i];
        rem = min(rem + r, e);
    }
    ans = max(ans, gain);
}

bool next(int i)
{
    if (i == 1 && ene[0] == e) { return false; }
    if (ene[i-1] == e) { ene[i-1] = 0; return next(i - 1); }
    ++ene[i-1]; return true;
}

int main()
{
    int T;
    cin >> T;
    rep (caseno, T) {
        cin >> e >> r >> n;
        rep (i, n) cin >> v[i];
        ans = 0;
        fill_n(ene, n, 0);
        do check(); while (next(n));
        cout << "Case #" << caseno + 1 << ": " << ans << endl;
    }
}
