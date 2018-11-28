#include <cstdio>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int n, k;
double p[256];
double dp[205][405];

void read() {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
}
vector<double> a;

double go(int x, int z) {
    double &ans = dp[x][z + 200];
    if (ans > -0.5) return ans;

    if (x == k) return !z;

    ans = a[x] * go(x + 1, z + 1) + (1 - a[x]) * go(x + 1, z - 1);


    return ans;
}


double get(vector<double> b) {
    a = b;
    memset(dp, -1, sizeof dp);
    return go(0, 0);
}

void solve() {
    sort(p, p + n);
    double ans = 0;

    for (int i = 0; i <= k; i++) {
        vector<double> b;
        for (int j = 0; j < i; j++) b.push_back(p[j]);
        for (int j = 0; j < k - i; j++) b.push_back(p[n - j - 1]);

        for (int j = 0; j < (int)b.size(); j++) {
            //printf ("%lf ", b[j]);
        }

        //printf ("   %lf\n", ans);
        ans = max(ans, get(b));
    }

    printf ("%lf\n", ans);
}
int main() {
    int cases;

    scanf("%d", &cases);
    for (int i=1; i<=cases; i++) {
        read();
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

