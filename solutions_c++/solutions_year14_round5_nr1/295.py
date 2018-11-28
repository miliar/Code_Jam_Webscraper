#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
//#
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>

long double prob(lint a, lint b, lint c) {
    if (a < 0 || b < 0 || c < 0) return 0;
    return 1 - (max(max(a, b), c) / ((long double)a + b + c));
}

#define MAXN 1001000

lint a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        {   
            lint p, q, r, s; cin >> n >> p >> q >> r >> s;
            for (int j = 0; j < n; j++) {
                a[j] = (j * p + q) % r + s;
                //printf("%lld ", a[j]);
            }
            //printf("\n");
        }
        long double ans = 0;
        lint s1 = 0, s2 = 0, s3 = 0;
        for (int i = 0; i < n; i++)
            s3 += a[i];
        int r = 0;
        for (int l = 0; l <= n; l++) {
            while (r <= n && (r < l || s2 < s3)) {
                ans = max(ans, prob(s1, s2, s3));
                s3 -= a[r];
                s2 += a[r];
                r++;
                if (r > 0 && l < r)
                    ans = max(ans, prob(s1, s2 - a[r - 1], s3 + a[r - 1]));
                ans = max(ans, prob(s1, s2 + a[r], s3 - a[r]));
                ans = max(ans, prob(s1, s2, s3));
            }
            s2 -= a[l];
            s1 += a[l];
            ans = max(ans, prob(s1, s2, s3));
        }
        printf("Case #%d: %.12Lf\n", i + 1, ans);
        //cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
