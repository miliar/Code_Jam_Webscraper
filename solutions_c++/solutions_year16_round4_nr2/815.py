#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int T, n, k;
double p[210];
double dp[210][210];

double calc(int w) {
    vector<double> pp;
    for (int i = 0; i < n; ++ i)
        if (w & (1 << i)) pp.push_back(p[i]);
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= k; ++ i)
        for (int j = 0; j <= i; ++ j) {
            dp[i][j] = dp[i-1][j]*pp[i - 1];
            if (j > 0)
                dp[i][j] += dp[i-1][j-1]*(1-pp[i-1]);
        }
    return dp[k][k/2];
}

int count(int w) {
    int cnt = 0;
    for (int i = 0; i < n; ++ i)
        if ((1 << i) & w) cnt ++ ;
    return cnt;
}

double getans() {
    double ans = 0;
    for (int i = 0; i < (1 << n); ++ i) {
        if (count(i) == k) ans = max(ans, calc(i));
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>T;
    for (int ca = 1; ca <= T; ++ ca) {
        cin>>n>>k;
        for (int i = 0; i < n; ++ i) {
            cin>>p[i];
        }
        cout<<"Case #"<<ca<<": " << getans() << endl;
    }
    return 0;
}
