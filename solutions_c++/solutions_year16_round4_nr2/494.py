#include <fstream>
#include <algorithm>

using namespace std;

const int MAXN = 205;
double p[MAXN], dp[MAXN][MAXN];

double solve(int n) {
    dp[0][0] = 1;
    for(int i = 1; i <= n; i++) {
        dp[i][0] = (1 - p[i - 1]) * dp[i - 1][0];
        for(int j = 1; j <= i; j++)
            dp[i][j] = p[i - 1] * dp[i - 1][j - 1] + (1 - p[i - 1]) * dp[i - 1][j];
    }
    return dp[n][n / 2];
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    out.setf(ios::fixed);
    out.precision(12);
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int n, k;
        in >> n >> k;
        for(int i = 0; i < n; i++)
            in >> p[i];
        sort(p, p + n);
        double ans = 0;
        for(int i = 0; i <= k; i++) {
            ans = max(ans, solve(k));
            rotate(p, p + n - 1, p + n);
        }
        out << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return  0;
}
