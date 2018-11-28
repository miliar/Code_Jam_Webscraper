#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>


using namespace std;

#define ll long long
#define y1 _dfdfdfd


const int maxn = 1 << 20;
const int inf = 1000000007;
const int mod = 1000000007;

int n, p, q, r, s;
int a[maxn];
ll sum[maxn];

ll f(int l, int r) {
    ll res = 0;
    if (l) res = max(res, sum[l - 1]);
    res = max(res, sum[n - 1] - sum[r]);
    res = max(res, sum[r] - (l ? sum[l - 1] : 0));
    return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        cin >> n >> p >> q >> r >> s;
        for (int i = 0; i < n; i++) {
            a[i] = (1LL * i * p + q) % r + s;
            sum[i] = (i ? sum[i - 1] : 0) + a[i];
        }
        int r = 0;
        ll ans = 0;
        for (int l = 0; l < n; l++) {
            r = max(r, l);
            while (r < n - 1 && f(l, r + 1) <= f(l, r)) {
                r++;
            }
            ans = max(ans, sum[n - 1] - f(l, r));
        }
        printf("%.10lf\n", 1.0 * ans / sum[n - 1]);
    }

	return 0;
}
