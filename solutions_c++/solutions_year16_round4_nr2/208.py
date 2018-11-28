// * Today I screwed up, but not as much as I could've
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
#include <iomanip>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef long long ll;
const int N = 222;

double check(vector<double> a, int k) {
    double odds[N], next[N];
    memset(odds, 0, sizeof(odds));
    odds[0] = 1;
    rep(i, 0, a.size()) {
        memset(next, 0, sizeof(next));
        rep(j, 0, N - 1) {
            next[j] += odds[j] * (1 - a[i]);
            next[j+1] += odds[j] * a[i];
        }
        swap(odds, next);
    }
    return odds[k / 2];
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<double> a(n);
    rep(i, 0, n)cin >> a[i];
    sort(a.begin(), a.end());
    double res = 0;
    rep(i, 0, k + 1) {
        vector<double> cur;
        //cout<<i<<" "<<(k-i)<<endl;
        rep(j, 0, i) cur.push_back(a[j]);
        rep(j, 0, k - i) cur.push_back(a[n - j - 1]);
        res = max(res, check(cur, k));
    }
    cout << res;
}

int main() {
    freopen("large.in", "r", stdin);
    freopen("outl.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    cout<<fixed<<setprecision(12);
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
