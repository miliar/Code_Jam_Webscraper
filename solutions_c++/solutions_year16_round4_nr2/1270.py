#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;

void preprocess() {

}

long double compute_probability(const vector<long double>& v) {
    const int n = v.size();
    long double dp[n][2*n+1];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < 2*n+1; ++j)
            dp[i][j] = 0;
    dp[0][n+1] = v[0];
    dp[0][n-1] = 1-v[0];
    for (int i = 1; i < n; ++i) {
        for (int k = -n; k <= n; ++k) {
            // i votes YES
            if (k != n)
                dp[i][n+k+1] += dp[i-1][n+k]*v[i];
            // i votes NO
            if (k != -n)
                dp[i][n+k-1] += dp[i-1][n+k]*(1-v[i]);
        }
    }
    return dp[n-1][n];
}

void process_testcase(const int testcase, const int should_run){
    int n, k;
    cin>>n>>k;
    long double p[n];
    for (int i = 0; i < n; ++i)
        cin>>p[i];

    if (should_run) {
        long double ans = 0;
        for (int stt = 0, end_stt = (1<<n); stt < end_stt; ++stt)
        if (__builtin_popcount(stt) == k)
        {
            vector<long double> v;
            for (int i = 0; i < n; ++i)
                if (stt&(1<<i))
                    v.push_back(p[i]);
            ans = max(ans, compute_probability(v));
        }
        cout<<"Case #"<<testcase<<": "<<fixed<<setprecision(10)<<ans<<endl;
    }
}
