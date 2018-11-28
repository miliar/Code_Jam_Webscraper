#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <iomanip>

using namespace std;

int n, k;
double p[1111];
double q[1111];
double dp[1111];

int main() {
    cout<<fixed<<setprecision(10);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
        
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        sort(p, p + n);
        double ans = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int m = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    q[m] = p[i];
                    m++;
                }
            }
            if (m != k) {
                continue;
            }           
            for (int i = 0; i <= k; i++) {
                dp[i] = 0;
            }
            dp[0] = 1;
            for (int i = 0; i < k; i++) {
                for (int j = k; j > 0; j--) {
                    dp[j] = dp[j] * (1 - q[i]) + dp[j - 1] * q[i]; 
                }
                dp[0] *= (1 - q[i]);
            }
            if (dp[k / 2] > ans) {
                ans = dp[k / 2];
            }
        }        
        cout << ans << endl;
    } 
    return 0;
}