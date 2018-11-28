#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>

using namespace std;

#define y1 ym37s62rw
#define x1 xm2ash4ad
#define pb push_back
#define mp make_pair
#define F first
#define S second

const int INF = 1000000007;
const long long INFll = 1000000007000000007ll;
const int MOD = 1000000007;

long double a[100500];
long double d[202][201][201];

long double prob(vector<long double> h, int n) {
    d[0][0][0] = 1;
    for (int g = 1; g <= n; ++g) {
        for (int w = 0; w <= n; ++w) {
            for (int l = 0; l <= n; ++l) {
                long double d1 = 0;
                if (g - 1 >= 0 && w - 1 >= 0) d1 = d[g - 1][w - 1][l];
                long double d2 = 0;
                if (g - 1 >= 0 && l - 1 >= 0) d2 = d[g - 1][w][l - 1];
                d[g][w][l] = d1 * h[g - 1] + d2 * (1. - h[g - 1]);
            }
        }
    }
    return d[n][n / 2][n / 2];
}

int main() {

    ios_base::sync_with_stdio(0);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
#endif
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cout << "Case #" << i + 1 << ": ";
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        long double ans = 0;
        for (int i = 0; i < (1 << n); ++i) {
            int l = 0;
            vector<long double> b;
            for (int j = 0; j < n; ++j) {
                if (((1 << j) & i) > 0) {
                    l++;
                    b.pb(a[j]);
                }
            }
            if (l == k)
                ans = max(ans, prob(b, k));
        }
        cout << fixed << setprecision(7) << ans << endl;
    }

    return 0;
}
