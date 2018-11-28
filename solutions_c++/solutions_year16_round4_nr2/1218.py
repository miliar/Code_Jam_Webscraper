/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 350;
const int M = 30110;
const long long MOD = 1000000007;
const double eps = 1e-10;
typedef vector<double> Array;
int n, m;

Array dp[N][N];

Array Update(const Array &last, const double &p) {
    Array cur(last.size() + 1, 0.0);
    
    for (int i = 0; i < last.size(); ++i) {
        cur[i] += last[i] * (1 - p);
        cur[i + 1] += last[i] * p;
    }
    
    return cur;
}

double prob[N];

double Calc(const Array &p) {
    Array dp(1, 1.0);
    
    for (int i = 0; i < p.size(); ++i) {
        dp = Update(dp, p[i]);
    }
    //for (int i = 0; i < dp.size(); ++i) { cout << dp[i] << ' '; } cout << endl;
    
    return dp[dp.size() / 2];
}

double DFS(int rem, int pos, int tail, Array p) {
    if (0 == rem) {
        return Calc(p);
    }
    if (pos > tail) {
        return 0;
    }
    double ret = 0;
    
    ret = max(ret, DFS(rem, pos + 1, tail, p));
    p.push_back(prob[pos]);
    ret = max(ret, DFS(rem - 1, pos + 1, tail, p));
    
    return ret;
    
}

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        printf("Case #%d: ",cas);
        cin >> n >> m;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= n; ++j) {
                dp[i][j] = Array(j + 1, 0.0);
                dp[i][j][0] = 1.0;
            }
        }
        double p;
        for (int i = 1; i <= n; ++i) {
            cin >> p;
            prob[i] = p;
            for (int j = 0; j <= i; ++j) {
                dp[i][j] = dp[i - 1][j];
                if (j > 0) {
                    Array temp = Update(dp[i - 1][j - 1], p);
                    
                    if (temp[temp.size() / 2] > dp[i][j][dp[i][j].size() / 2]) {
                        dp[i][j] = temp;
                    }
                }
            }
        }
        printf("%.6lf\n",DFS(m, 1, n, Array(0)));
    }
    return 0;
}
