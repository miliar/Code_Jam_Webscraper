#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>

using namespace std;
const int inf = 1000000007;
const int N = 205;
int n , k;
double p[N];
long double dp[N][N];
long double gao(vector<double> &p) {
    for(int i = 0 ; i <= k ; i ++) {
        for (int j = 0 ; j <= k ; j ++) {
            dp[i][j] = 0.0;
        }
    }
    dp[0][0] = 1.0;
    for (int i = 0 ; i < k ; i ++) {
        for (int j = 0 ; j <= i ; j ++) {
            dp[i + 1][j] += dp[i][j] * (1 - p[i]);
            dp[i + 1][j + 1] += dp[i][j] * p[i];
        }
    }
    return dp[k][k / 2];
}
int main () {
    // freopen ("input.txt", "r" , stdin);
    // freopen ("output.txt", "w", stdout);
    int t, cas = 0;scanf ("%d" , &t);   
    while (t --) {
        scanf ("%d %d" , &n, &k);
        for (int i = 0 ; i < n ; i ++) {
            scanf ("%lf" , &p[i]);
        }
        sort(p , p + n);
        long double ans = 0;
        for(int i = 0 ; i <= k ; i ++) {
            vector<double> a;
            for (int j = 0 ; j < i ; j ++) {
                a.push_back (p[j]);
            }
            for (int j = 0 ; j < k - i ; j ++) {
                a.push_back (p[n - 1 - j]);
            }
            ans = max (ans , gao(a));
        }
        printf ("Case #%d: %.10f\n", ++ cas , (double)ans);

    }

    return 0;
}