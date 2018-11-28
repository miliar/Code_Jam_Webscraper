#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

double calcProb(const vector<double>& p)
{
    int n = p.size();
    vector<double> dp(1, 1.0);
    for(int i=0; i<n; ++i){
        vector<double> nextDp(i+2, 0.0);
        for(int j=0; j<=i; ++j){
            nextDp[j+1] += dp[j] * p[i];
            nextDp[j] += dp[j] * (1.0 - p[i]);
        }
        dp.swap(nextDp);
    }
    return dp[n/2];
}

double solve(int n, int k, vector<double> p)
{
    sort(p.begin(), p.end());

    vector<double> p2 = p;
    p2.resize(k);
    double ans = calcProb(p2);

    for(int i=0; i<k; ++i){
        p2[k-1-i] = p[n-1-i];
        ans = max(ans, calcProb(p2));
    }

    return ans;
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int n, k;
        cin >> n >> k;
        vector<double> p(n);
        for(int i=0; i<n; ++i)
            cin >> p[i];

        double ans = solve(n, k, p);
        cout.setf(ios_base::fixed, ios_base::floatfield);
        cout << setprecision(10);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}