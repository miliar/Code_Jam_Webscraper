#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

int n, k;
double ps[201];
double tbl[201][201];

/*

double tbl[201][201][201];

double rec(int cur, int rest, int yes)
{
    if (yes < 0) return 0;

    if (cur == n) {
        assert(rest == 0);
        return yes == 0 ? 1 : 0;
    }

    double &ret = tbl[cur][rest][yes];
    if (ret >= 0) return ret;

    ret = 0;

    if (rest > 0) {
        double a = rec(cur + 1, rest - 1, yes - 1);
        double b = rec(cur + 1, rest - 1, yes);

        ret = a * ps[cur] + b * (1 - ps[cur]);
    }

    if (n - cur > rest) {
        ret = max(ret, rec(cur + 1, rest, yes));
    }

    return ret;
}

void solve()
{
    int k; cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> ps[i];

    memset(tbl, -1, sizeof(tbl));

    cout << setiosflags(ios::fixed) << setprecision(12);
    cout << rec(0, k, k / 2) << endl;
}
*/

double rec(int cur, int yes, int no, const vector<double> &tt)
{
    if (cur == tt.size()) return yes == no ? 1 : 0;

    double &ret = tbl[cur][yes];
    if (ret >= 0) return ret;

    double a = rec(cur + 1, yes + 1, no, tt);
    double b = rec(cur + 1, yes, no + 1, tt);

    return ret = a * tt[cur] + b * (1 - tt[cur]);
}

void solve()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> ps[i];

    sort(ps, ps + n);

    double ans = 0;

    for (int sm = 0; sm <= k; sm++) {
        vector<double> selp;
        for (int i = 0; i < sm; i++) selp.push_back(ps[i]);
        for (int i = 0; i < k - sm; i++) selp.push_back(ps[n - 1 - i]);

        // cout << selp.size() << endl;

        // cout << "* ";
        // for (int i = 0; i < selp.size(); i++)
        //     cout << selp[i] << " ";
        // cout << endl;

        memset(tbl, -1, sizeof(tbl));
        ans = max(ans, rec(0, 0, 0, selp));
    }

    cout << setiosflags(ios::fixed) << setprecision(12);
    cout << ans << endl;
}

int main()
{
    int t; cin >> t;
    for (int cn = 1; cn <= t; cn++) {
        cout << "Case #" << cn << ": ";
        solve();
    }

    return 0;
}
