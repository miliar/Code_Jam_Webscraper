#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

typedef long long ll;

int p[7], guess[3], ans, best;

void check()
{
    map<int, int> m;
    rep (i, 8) {
        int t = 1;
        rep (j, 3) if (i & (1 << j)) t *= guess[j];
        ++m[t];
    }
    int a = 1;
    rep (i, 7) {
        if (m[p[i]] == 0) return;
        a *= m[p[i]];
    }
    if (a > best) {
        best = a;
        ans = 100 * guess[0] + 10 * guess[1] + guess[2];
    }
}

bool next(int i)
{
    if (i == 1 && guess[0] == 5) { guess[0] = 2; return false; }
    if (guess[i-1] == 5) { guess[i-1] = 2; return next(i - 1); }
    ++guess[i-1]; return true;
}

int main()
{
    int t, r, n, m, k;
    cin >> t >> r >> n >> m >> k;
    guess[0] = guess[1] = guess[2] = 2;
    cout << "Case #1:" << endl;
    rep (i, r) {
        rep (j, 7) cin >> p[j];
        best = 0;
        do check(); while (next(3));
        cout << ans << endl;
    }
}
